import os
import sys

# Constants
DATA_DIR = "data"
SIZE_THRESHOLD = 332  # bytes

def get_md_files(directory):
    """Return a list of .md files in the given directory."""
    try:
        return [f for f in os.listdir(directory) if f.endswith('.md')]
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: No permission to access directory '{directory}'.")
        sys.exit(1)

def delete_if_small(file_path):
    """Delete the file if its size is less than SIZE_THRESHOLD bytes."""
    try:
        if os.path.getsize(file_path) < SIZE_THRESHOLD:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        else:
            print(f"Skipped: {file_path} (size >= {SIZE_THRESHOLD} bytes)")
    except FileNotFoundError:
        print(f"Warning: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: No permission to delete '{file_path}'.")
    except OSError as e:
        print(f"Error deleting '{file_path}': {e}")

def main():
    """Main function to delete small .md files in the data directory."""
    data_path = os.path.join(os.getcwd(), DATA_DIR)
    md_files = get_md_files(data_path)
    
    if not md_files:
        print(f"No .md files found in '{data_path}'.")
        return

    print(f"Processing {len(md_files)} .md files in '{data_path}'...")
    
    for md_file in md_files:
        file_path = os.path.join(data_path, md_file)
        delete_if_small(file_path)

    print("Operation completed.")

if __name__ == "__main__":
    main()