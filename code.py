from pygame import *
import json
import os

window_size = 600, 400
window = display.set_mode(window_size)
display.set_caption("Меню зі складністю")
font.init()
main_font = font.Font(None, 36)

# JSON збереження
filename = "settings.json"
difficulties = ["low", "medium", "hard"]
current_index = 0

if os.path.exists(filename):
    with open(filename, "r") as f:
        data = json.load(f)
        if data.get("difficulty") in difficulties:
            current_index = difficulties.index(data["difficulty"])
else:
    with open(filename, "w") as f:
        json.dump({"difficulty": difficulties[0]}, f)
