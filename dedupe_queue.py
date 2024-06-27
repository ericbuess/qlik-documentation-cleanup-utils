import json

def remove_duplicates_from_json():
    # File path
    file_path = 'queue.json'

    # Read the JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Remove duplicates using a set
    unique_data = list(set(data))

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(unique_data, file, indent=2)

    print(f"Duplicates removed. Updated file saved to {file_path}")
    print(f"Original count: {len(data)}, New count: {len(unique_data)}")

if __name__ == "__main__":
    remove_duplicates_from_json()