        for conn in list(players.keys()):
            if conn in eliminated:
                try:
                    conn.send("LOSE".encode())
                except:
                    pass
                to_remove.append(conn)
                continue

            try:
                packet = "|".join([f"{p["id"]},{p["x"]},{p["y"]},{p["r"]},{p["name"]}"
                                   for c, p in players.items() if c != conn and c not in eliminated]) + "|"
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
