from socket import *
from time import sleep
server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('localhost', 12345))
server_socket.setblocking(False)
server_socket.listen(5)

clients = []

while True:
   try:
       connection, address = server_socket.accept()
       client_name = connection.recv(1024).decode()
       print(f'Підключився клієнт {client_name}')
       connection.setblocking(False)
       clients.append([connection, client_name])
   except:
       pass

   for client in clients:
       try:
           client[0].send(f'Онлайн: {client[1]}'.encode())
       except:
           print(f'Відключився від сервера: {client[1]}')
           clients.remove(client)

   sleep(0.5)