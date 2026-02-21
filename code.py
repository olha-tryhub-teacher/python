from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('localhost', 12345))

name = input("Для підключення на сервер введіть своє ім'я: ")
client_socket.send(name.encode())

print(client_socket.recv(1024).decode()) # отримали вітання

client_socket.close()

