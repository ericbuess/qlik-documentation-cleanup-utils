import os
import re


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split content into sections
    sections = content.split('\n\n# ')

    processed_content = ""
    for i, section in enumerate(sections):
        if i == 0:
            # First section (Title) doesn't need modification
            processed_content += section + "\n\n"
        else:
            # For other sections, add the '# ' back and process
            lines = section.split('\n', 1)
            if len(lines) > 1:
                header, body = lines
                processed_content += f"# {header}\n\n{body}\n\n"
            else:
                processed_content += f"# {section}\n\n"

    # Process bullet points
    processed_content = re.sub(
        r'^(\s*)\*', r'\n\1*', processed_content, flags=re.MULTILINE)

    # Remove extra newlines
    processed_content = re.sub(r'\n{3,}', '\n\n', processed_content)

    # Write the processed content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content.strip())


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
