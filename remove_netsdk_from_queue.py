import json
import re

def remove_netsdk_items():
    # File path
    file_path = 'queue.json'

    # Read the JSON file
    with open(file_path, 'r') as file:
        queue_items = json.load(file)

    print(f"Original queue size: {len(queue_items)}")

    # Remove items containing 'netsdk' (case-insensitive)
    updated_queue = [url for url in queue_items if not re.search(r'netsdk', url, re.IGNORECASE)]

    print(f"Updated queue size: {len(updated_queue)}")
    print(f"Removed {len(queue_items) - len(updated_queue)} items")

    # Write the updated queue back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(updated_queue, file, indent=2)

    print(f"Updated queue saved to {file_path}")

if __name__ == "__main__":
    remove_netsdk_items()