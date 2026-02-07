import socket
import threading
import struct
from random import randint

HOST = "0.0.0.0"
PORT = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = {}     # player_id -> socket
players = {}     # player_id -> (x, y, r)
next_id = 1

lock = threading.Lock()  # 🔒 захист від потоків


def recv_full(sock, size):
    data = b''
    while len(data) < size:
        packet = sock.recv(size - len(data))
        if not packet:
            return None
        data += packet
    return data


def broadcast_state():
    """Розсилає стан усіх гравців"""
    with lock:
        packet = struct.pack("!BI", 3, len(players))
        for pid, (x, y, r) in players.items():
            packet += struct.pack("!Ifff", pid, x, y, r)

        dead = []

        for pid, c in list(clients.items()):
            try:
                c.sendall(packet)
            except:
                dead.append(pid)

        # чистимо мертвих
        for pid in dead:
            print("Removing dead client:", pid)
            clients[pid].close()
            del clients[pid]
            if pid in players:
                del players[pid]


def handle_client(conn, player_id):
    print(f"Player {player_id} handler started")

    # 📤 Надсилаємо ID (тип 1)
    conn.sendall(struct.pack("!BI", 1, player_id))

    with lock:
        players[player_id] = (
            randint(-300, 300),
            randint(-300, 300),
            20
        )

    try:
        while True:
            header = recv_full(conn, 1)
            if not header:
                break

            packet_type = struct.unpack("!B", header)[0]

            # Тип 2 = позиція гравця
            if packet_type == 2:
                data = recv_full(conn, 12)
                if not data:
                    break

                x, y, r = struct.unpack("!fff", data)

                with lock:
                    players[player_id] = (x, y, r)

                broadcast_state()

    except Exception as e:
        print(f"Error with player {player_id}:", e)

    finally:
        print(f"Player {player_id} disconnected")
        with lock:
            if player_id in clients:
                clients[player_id].close()
                del clients[player_id]
            if player_id in players:
                del players[player_id]


print("Server started...")

while True:
    conn, addr = server.accept()

    with lock:
        player_id = next_id
        next_id += 1
        clients[player_id] = conn

    print("Connected:", addr, "ID:", player_id)

    threading.Thread(
        target=handle_client,
        args=(conn, player_id),
        daemon=True
    ).start()
