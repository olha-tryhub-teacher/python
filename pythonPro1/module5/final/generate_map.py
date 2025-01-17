import random

# Function to generate a terrain map with sharper transitions
def generate_sharp_terrain(rows, cols, min_height=-1, max_height=5):
    return [[random.choice([min_height] + list(range(max_height + 1))) for _ in range(cols)] for _ in range(rows)]

# Generate a 40x60 terrain map with sharper transitions
sharp_terrain = generate_sharp_terrain(40, 20)

# Convert the terrain map into a string for better display
terrain_map = "\n".join(" ".join(f"{val:2}" for val in row) for row in sharp_terrain)
print(terrain_map)  # Display a portion of the map for preview
