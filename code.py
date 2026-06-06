def receive_data():
    global all_players, lose
    while True:
        try:
            data = sock.recv(4096).decode()
            if "LOSE" in data:
                lose = True
            elif data:
                # Оновлюємо дані ворогів
                for p in data.split("|"):
                    if "," in p:
                        parts = p.split(",")
                        if len(parts) >= 4:
                            pid = int(parts[0])
                            if pid != my_id:
                                all_players[pid] = [int(parts[1]), int(parts[2]), int(parts[3])]
        except:
            break
