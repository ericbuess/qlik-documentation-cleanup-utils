import os
import json


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace "event: data data:" with an empty string
    content = content.replace("event: data data:", "")

    # Ensure the content starts with "{"
    if not content.strip().startswith("{"):
        content = "{" + content

    # Ensure the content ends with "}"
    if not content.strip().endswith("}"):
        content = content + "}"

    # Validate JSON
    try:
        json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Warning: File {
              file_path} contains invalid JSON after processing. Error: {str(e)}")

    # Write the processed content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                process_file(file_path)
                print(f"Processed: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")


if __name__ == "__main__":
    data_directory = "data"
    process_directory(data_directory)
    print("Processing complete.")
