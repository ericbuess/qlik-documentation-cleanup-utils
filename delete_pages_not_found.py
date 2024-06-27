import os
import glob


def find_and_delete_files(directory, search_string):
    # Get all .md files in the specified directory
    md_files = glob.glob(os.path.join(directory, '*.md'))

    # Array to store file paths containing the search string
    files_to_delete = []

    # Check each file for the search string
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            if search_string in content:
                files_to_delete.append(file_path)

    # Delete the files
    for file_path in files_to_delete:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except OSError as e:
            print(f"Error deleting {file_path}: {e}")

    print(f"Total files deleted: {len(files_to_delete)}")


# Specify the directory and search string
directory = 'data/'
search_string = "Qlik | Page Not Found"

# Run the function
find_and_delete_files(directory, search_string)
