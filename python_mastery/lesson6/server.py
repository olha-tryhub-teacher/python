import socket
import threading

HOST = '0.0.0.0'
PORT = 8080

clients = []


def broadcast(data, exclude_socket=None):
   for client in clients:
       if client != exclude_socket:
           try:
               client.sendall(data)
           except:
               pass


def handle_client(client_socket):
   while True:
       try:
           data = client_socket.recv(4096)
           if not data:
               break
           broadcast(data, exclude_socket=client_socket)
       except:
           break
   if client_socket in clients:
       clients.remove(client_socket)
   client_socket.close()


def main():
   server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   server_socket.bind((HOST, PORT))
   server_socket.listen(5)
   print(f"Сервер запущено на {HOST}:{PORT}")

   while True:
       client_socket, addr = server_socket.accept()
       print(f"Підключився клієнт: {addr}")
       clients.append(client_socket)

       t = threading.Thread(target=handle_client, args=(client_socket,))
       t.start()


if __name__ == "__main__":
   main()
