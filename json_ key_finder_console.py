import json

# TODO: Recreate this using Vue.js binding the JSON data to a variable and textbox
# TODO: It would also be cool if it would detect the brackets and allow them to be collapsed on click.

def find_key_paths(json_obj, search_key, current_path='', paths=None):
    # Initialize the paths list if it's the first call
    if paths is None:
        paths = []

    # Check if the current JSON object is a dictionary
    if isinstance(json_obj, dict):
        # Iterate through each key-value pair in the dictionary
        for key_name, value in json_obj.items():
            # Construct the path to the current key
            new_path = f"{current_path}['{key_name}']" if current_path else f"event['{key_name}']"
            if key_name == search_key:
                paths.append(new_path)
            find_key_paths(value, search_key, new_path, paths)
    # Check if the current JSON object is a list
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_path = f"{current_path}[{index}]"
            find_key_paths(item, search_key, new_path, paths)

    # Return the collected paths where the key was found
    return paths

# Load JSON data from a file
try:
    with open('object.json', 'r') as file:
        event = json.load(file)
except FileNotFoundError:
    print("File 'object.json' not found.")
    exit()
except json.JSONDecodeError:
    print("Invalid JSON in file. Please ensure the file contains valid JSON.")
    exit()

# Taking the key to find from the console
key_to_find = input("Enter the key to find: ")
paths_to_key = find_key_paths(event, key_to_find)

if paths_to_key:
    print(f"Paths to '{key_to_find}':")
    for path in paths_to_key:
        print(path)
else:
    print(f"Key '{key_to_find}' not found in the JSON.")
