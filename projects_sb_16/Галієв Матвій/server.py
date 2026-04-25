# ngrok.exe tcp 8080
from socket import *
import threading

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(12)
print("Сервер запущений...")

clients = []


def broadcast(message):
    for client in clients:
        try:
            client.send(f"{message}\n".encode())
        except:
            pass


def handle_client(client_socket):
    name = client_socket.recv(1024).decode().strip()
    broadcast(f"{name} приєднався до чату!")

    while True:
        try:
            message = client_socket.recv(1024).decode().strip()
            print(f"{name}: {message}")
            broadcast(f"{name}: {message}")
        except:
            clients.remove(client_socket)
            broadcast(f"{name} вийшов із чату!")
            client_socket.close()
            break


while True:
    client_socket, addr = server_socket.accept()
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()




# ngrok.exe tcp номер порта