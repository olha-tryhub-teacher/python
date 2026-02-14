from socket import *
print("Server started...")
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)

connection, address = server_socket.accept()
client_name = connection.recv(1024).decode()

print(f"Користувач {client_name} під'єднався!")
connection.send(f"Вітаю {client_name} на сервері".encode())

server_socket.close()
