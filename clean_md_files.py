import os
import re
from pathlib import Path


def clean_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove navigation links at the beginning of the document
    content = re.sub(r'^(\* \(http.*?\)\n)+', '', content)

    # Remove navigation links at the end of the document
    content = re.sub(r'\n(\* \(http.*?\)\n)+$', '', content)

    # Remove "ON THIS PAGE" section and its content
    content = re.sub(r'ON THIS PAGE\n------------\n\n.*?\n\n',
                     '', content, flags=re.DOTALL)

    # Remove "Leave your feedback here" section
    content = re.sub(
        r'Leave your feedback here.*?]\(javascript:void\\\(0\\\)\)\n\n', '', content, flags=re.DOTALL)

    # Remove language selection links at the end of the document
    content = re.sub(
        r'\n( \* \(http://help\.qlik\.com/.*?/cloud-services/.*?\)\n)+$', '', content)

    # Remove redundant headers
    content = re.sub(r'===============\n \n', '', content)
    content = re.sub(r'--------------------------\n\n', '', content)

    # Remove "Digital Help SIte Assets Survey" section
    content = re.sub(
        r'Digital Help SIte Assets Survey\n===============', '', content)

    # Remove extraneous newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Write the cleaned content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = Path(root) / file
                print(f"Processing: {file_path}")
                clean_markdown_file(file_path)


if __name__ == "__main__":
    data_directory = Path("data")
    if data_directory.exists() and data_directory.is_dir():
        process_directory(data_directory)
        print("Processing complete.")
    else:
        print("The 'data' directory does not exist or is not a directory.")
