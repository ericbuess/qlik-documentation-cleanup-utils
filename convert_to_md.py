import os


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove leading and trailing braces
    content = content.strip().strip('{}')

    # Split the content into key-value pairs
    pairs = content.split('","')

    # Process each key-value pair
    processed_content = ""
    for pair in pairs:
        key, value = pair.split('":"', 1)
        key = key.strip('"')
        value = value.strip('"')

        # Convert keys to Markdown headers
        processed_content += f"# {key.capitalize()}: {value}\n\n"

    # Write the processed content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                try:
                    process_file(file_path)
                    print(f"Processed: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")


if __name__ == "__main__":
    data_directory = input("Enter the path to your data directory: ")
    process_directory(data_directory)
    print("Processing complete.")
