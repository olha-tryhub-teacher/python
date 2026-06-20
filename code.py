from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(("0.0.0.0", 5000))
sock.listen(15)
sock.setblocking(False)

players = {} # 1: (x, y, r, conn_ids)
conn_ids = {}
id_counter = 0


def handle_data():
    global id_counter
    while True:
        time.sleep(0.01)
        player_data = {}
        to_remove = []

        for conn in list(players):
            try:
                data = conn.recv(64).decode().strip()
                if "," in data:
                    parts = data.split(",")
                    if len(parts) == 5:
                        pid, x, y, r = map(int, parts[:4])
                        name = parts[-1]
                        players[conn] = {"id": pid, "x": x,
                                         "y": y, "r": r,
                                         "name": name}
                        player_data[conn] = players[conn]
            except:
                continue

        eliminated = []
        for conn1 in player_data:
            if conn1 in eliminated: continue
            p1 = player_data[conn1]
            for conn2 in player_data:
                if conn1 == conn2 or conn2 in eliminated: continue
                p2 = player_data[conn2]
                dx, dy = p1["x"] - p2["x"], p1["y"] - p2["y"]
                distance = (dx ** 2 + dy ** 2) ** 0.5
                if (distance < p1["r"] + p2["r"]
                        and p1["r"] > p2["r"] * 1.1):
                    p1["r"] += int(p2["r"] * 0.5)
                    players[conn1] = p1
                    eliminated.append(conn2)

        for conn in list(players.keys()):
            if conn in eliminated:
                try:
                    conn.send("LOSE".encode())
                except:
                    pass
                to_remove.append(conn)
                continue

            try:
                packet = "|".join([f"{p['id']},{p['x']},{p['y']},{p['r']},{p['name']}" for c, p in players.items() if c != conn and c not in eliminated]) + "|"
                conn.send(packet.encode())
            except:
                to_remove.append(conn)

        for conn in to_remove:
            players.pop(conn, None)
            conn_ids.pop(conn, None)


Thread(target=handle_data, daemon=True).start()
print("SERVER running...")

while True:
    try:
        conn, addr = sock.accept()
        conn.setblocking(False)
        id_counter += 1
        players[conn] = {"id": id_counter, "x": 0, "y": 0, "r": 20, "name": None}
        conn_ids[conn] = id_counter
        conn.send(f"{id_counter},0,0,20".encode())
    except:
        pass
