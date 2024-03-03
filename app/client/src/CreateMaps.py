import json
import os
import MapStates
import random

def generate_and_append_maps(x, res, width, height, file_path):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            json.dump({}, f)
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    for i in range(x):
        map_key = f"map_{len(data) + 1}"
        map_data = MapStates.gen_map(res, width, height)
        data[map_key] = map_data
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"MAP GENERATED: map_{len(data)}")
def choose_random_map(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    random_key = random.choice(list(data.keys()))
    print("Map:", random_key)
    
    return data[random_key]

def choose_map(file_path, idx):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    print("Map:", data[idx])
    
    return data[idx]

def get_last_map(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    
    last_map_key = f"map_{len(data)}"
    print("Map:", last_map_key)
    
    return data[last_map_key]

def delete_last_map(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    last_map_key = f"map_{len(data)}"
    if last_map_key in data:
        del data[last_map_key]
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"{last_map_key} has been deleted.")

# untested
def delete_map(file_path, idx):
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    map_key = f"map_{idx}"
    if map_key in data:
        del data[map_key]
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    
    print(f"{map_key} has been deleted.")

def main():
    map_count = 1
    res = 50
    width = 1000
    height = 600
    #delete_last_map("maps.json")
    #generate_and_append_maps(map_count, res, width, height, "maps.json")

if __name__ == "__main__":
    main()