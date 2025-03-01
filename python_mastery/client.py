from socket import *

client = socket(AF_INET, SOCK_STREAM)
name = input('Введіть ім`я:')

client.connect(('localhost', 12345))
client.send(name.encode())

while True:
   try:
       print(client.recv(1024).decode())
   except:
       break