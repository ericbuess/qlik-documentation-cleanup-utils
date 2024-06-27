import json
import os
from utils import file_exists_for_url, QUEUE_FILE, DATA_DIR

def update_queue():
    # Load the queue from the JSON file
    with open(QUEUE_FILE, 'r') as file:
        queue_items = json.load(file)

    print(f"Original queue size: {len(queue_items)}")

    # Filter out items that already have corresponding files
    updated_queue = [url for url in queue_items if not file_exists_for_url(url)]

    print(f"Updated queue size: {len(updated_queue)}")
    print(f"Removed {len(queue_items) - len(updated_queue)} items")

    # Save the updated queue back to the JSON file
    with open(QUEUE_FILE, 'w') as file:
        json.dump(updated_queue, file, indent=2)

    print(f"Updated queue saved to {QUEUE_FILE}")

if __name__ == "__main__":
    update_queue()