client_socket = connect()


def send_message():
    while True:
        msg = input()
        if msg.lower() == "exit" or msg.lower() == "вихід":
            client_socket.close()
            break
        client_socket.send(msg.encode())


threading.Thread(target=send_message, daemon=True).start()


while True:
    try:
        message = client_socket.recv(1024).decode().strip()
        if message:
            print(message)
        else:
            break
    except:
        print("Від'єднано від сервера")
        break
