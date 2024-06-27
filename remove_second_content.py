import os
import glob
import logging
import argparse
import shutil
from typing import List

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(file_path: str, search_string: str, dry_run: bool = False, backup: bool = False) -> None:
    """Process a single file, removing content from search_string to the end."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        index = content.find(search_string)
        if index != -1:
            new_content = content[:index]
            if not dry_run:
                if backup:
                    backup_path = f"{file_path}.bak"
                    shutil.copy2(file_path, backup_path)
                    logging.info(f"Backup created: {backup_path}")

                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                logging.info(f"Processed: {file_path}")
            else:
                logging.info(f"Would process (dry run): {file_path}")
        else:
            logging.info(f"Search string not found in: {file_path}")
    except IOError as e:
        logging.error(f"Error processing {file_path}: {str(e)}")

def find_md_files(directory: str) -> List[str]:
    """Find all .md files in the given directory and its subdirectories."""
    return glob.glob(os.path.join(directory, '**', '*.md'), recursive=True)

def main() -> None:
    parser = argparse.ArgumentParser(description="Clean .md files by removing content after a specified string.")
    parser.add_argument('--dry-run', action='store_true', help="Perform a dry run without modifying files")
    parser.add_argument('--backup', action='store_true', help="Create backups of modified files")
    args = parser.parse_args()

    search_string = '{"title":'
    data_dir = 'data/'

    if not os.path.isdir(data_dir):
        logging.error(f"Directory not found: {data_dir}")
        return

    md_files = find_md_files(data_dir)
    total_files = len(md_files)
    logging.info(f"Found {total_files} .md files")

    for i, file_path in enumerate(md_files, 1):
        process_file(file_path, search_string, args.dry_run, args.backup)
        if i % 10 == 0 or i == total_files:
            logging.info(f"Progress: {i}/{total_files} files processed")

    logging.info("Processing complete")

if __name__ == "__main__":
    main()