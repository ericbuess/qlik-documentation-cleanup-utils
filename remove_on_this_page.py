import re
import os
import logging
from typing import List


def get_md_files(directory: str) -> List[str]:
    """
    Get all .md files in the specified directory.

    Args:
    directory (str): Path to the directory to search for .md files.

    Returns:
    List[str]: List of paths to .md files in the directory.
    """
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files


def process_file(file_path: str) -> None:
    """
    Process a single .md file, removing content between '# Content: ' and the last 'ON THIS PAGE'.

    Args:
    file_path (str): Path to the .md file to process.
    """
    logging.info(f"Processing file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        logging.info(f"Original content length: {len(content)}")

        # Normalize newlines to handle different formats
        content = content.replace('\r\n', '\n').replace('\r', '\n')

        # Find the position of "# Content: " to ensure we're looking in the right place
        content_start = content.find("# Content: ")
        if content_start != -1:
            logging.info(f"'# Content: ' found at position {content_start}.")

            # Use regex to find all occurrences of the target pattern
            target_pattern = re.compile(r'ON THIS PAGE', re.MULTILINE)
            matches = list(target_pattern.finditer(content))

            if matches:
                # Get the last occurrence
                last_match = matches[-1]
                logging.info(f"Last 'ON THIS PAGE' found at position {
                             last_match.start()}.")

                # Keep everything before "# Content: " and everything after the last "ON THIS PAGE" pattern
                modified_content = content[:content_start +
                                           len("# Content: ")] + content[last_match.start():]
                logging.info(f"Modified content length: {
                             len(modified_content)}")

                # Write the modified content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(modified_content)
                logging.info(f"Processed and modified file: {file_path}")
            else:
                logging.warning(
                    "'ON THIS PAGE' pattern not found. No modifications made.")
        else:
            logging.warning(f"'# Content: ' not found in file: {file_path}")
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {str(e)}")


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    data_directory = 'data/'
    md_files = get_md_files(data_directory)

    if not md_files:
        logging.warning(f"No .md files found in {data_directory}")
        return

    logging.info(f"Found {len(md_files)} .md files to process.")

    for file_path in md_files:
        process_file(file_path)

    logging.info("Processing complete.")


if __name__ == "__main__":
    main()
