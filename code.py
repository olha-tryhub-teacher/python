from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

# 🟢 Створення TCP-сокета та запуск серверу
sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', 8080))      # Прив’язка до локального хоста і порту 8080
sock.listen(5)                      # Сервер може обробляти до 5 підключень одночасно
sock.setblocking(False)            # Неблокуючий режим (accept() не зависає)

# 🟢 Головні словники:
players = {}      # conn: {'id': int, 'x': int, 'y': int, 'r': int}
conn_ids = {}     # conn: id — для зручного доступу до ID по сокету
id_counter = 0    # Унікальний ID кожному новому гравцю

# 🧠 Потік, який обробляє всі дії в грі
def handle_data():
   global id_counter
   while True:
       time.sleep(0.01)  # Маленька затримка для зниження навантаження CPU
       player_data = {}  # Тимчасовий словник для гравців, які надіслали оновлення
       to_remove = []    # Список клієнтів, яких треба від'єднати

       # 🔁 Читання даних від усіх клієнтів
       for conn in list(players):
           try:
               data = conn.recv(64).decode().strip()
               if ',' in data:
                   parts = data.split(',')
                   if len(parts) == 4:
                       pid, x, y, r = map(int, parts)
                       players[conn] = {'id': pid, 'x': x, 'y': y, 'r': r}
                       player_data[conn] = players[conn]  # Додаємо до активних
           except:
               continue  # Якщо помилка — просто пропускаємо

       # 🧨 Обробка зіткнень між гравцями
       eliminated = []  # Список клієнтів, яких "з’їли"
       for conn1 in player_data:
           if conn1 in eliminated: continue
           p1 = player_data[conn1]
           for conn2 in player_data:
               if conn1 == conn2 or conn2 in eliminated: continue
               p2 = player_data[conn2]
               dx, dy = p1['x'] - p2['x'], p1['y'] - p2['y']
               distance = (dx**2 + dy**2)**0.5
               if distance < p1['r'] + p2['r'] and p1['r'] > p2['r'] * 1.1:
                   # Якщо гравець p1 більший і накрив p2 — поглинає його
                   p1['r'] += int(p2['r'] * 0.5)
                   players[conn1] = p1
                   eliminated.append(conn2)

       # 📤 Відправлення даних клієнтам
       for conn in list(players.keys()):
           if conn in eliminated:
               # Надсилаємо повідомлення поразки
               try:
                   conn.send("LOSE".encode())
               except:
                   pass
               to_remove.append(conn)
               continue

           try:
               # Формуємо список інших гравців (окрім самого себе)
               packet = '|'.join([f"{p['id']},{p['x']},{p['y']},{p['r']}"
                                  for c, p in players.items() if c != conn and c not in eliminated]) + '|'
               conn.send(packet.encode())  # Відправляємо інформацію про інших гравців
           except:
               to_remove.append(conn)  # Якщо не вдалося — від'єднуємо

       # 🔻 Видаляємо гравців, яких поглинули або розірвали з’єднання
       for conn in to_remove:
           players.pop(conn, None)
           conn_ids.pop(conn, None)

# 🧵 Запускаємо обробку в окремому потоці
Thread(target=handle_data, daemon=True).start()
print("SERVER running...")

# 🔁 Прийом нових підключень
while True:
   try:
       conn, addr = sock.accept()       # Приймаємо нове з'єднання
       conn.setblocking(False)          # Робимо сокет неблокуючим
       id_counter += 1                  # Новий ID
       players[conn] = {'id': id_counter, 'x': 0, 'y': 0, 'r': 20}  # Стартові параметри
       conn_ids[conn] = id_counter
       conn.send(f"{id_counter},0,0,20".encode())  # Надсилаємо гравцю його ID і стартові дані
   except:
       pass  # Якщо не вдалося прийняти — просто чекаємо далі
