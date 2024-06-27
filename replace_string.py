import os
import shutil

# Configuration
TARGET = "\n\n\n\n\n\n](https://twitter.com/qlik)\n](https://www.linkedin.com/company/qlik)\n](https://www.facebook.com/qlik)\n\nLegal\n-----\n\n"
REPLACEMENT = "]]]"
DIRECTORY = "data"
DRY_RUN = False  # Set to True to preview changes without modifying files


def replace_in_file(file_path, target, replacement, dry_run=False):
    """Replace target string with replacement string in the given file."""
    # Create a backup of the original file
    backup_path = file_path + '.bak'
    shutil.copy2(file_path, backup_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Perform the replacement
        new_content = content.replace(target, replacement)

        if not dry_run:
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Processed: {file_path}")
        else:
            print(f"Would process (dry run): {file_path}")
            # In a real-world scenario, you might want to show a diff here

        return True
    except IOError as e:
        print(f"Error processing {file_path}: {e}")
        # Restore the backup
        if not dry_run:
            shutil.move(backup_path, file_path)
        return False
    finally:
        # Clean up the backup file in dry run mode
        if dry_run and os.path.exists(backup_path):
            os.remove(backup_path)


def main(target, replacement, directory, dry_run=False):
    """Main function to process all .md files in the given directory."""
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' not found.")
        return

    md_files = [f for f in os.listdir(directory) if f.endswith('.md')]

    if not md_files:
        print(f"No .md files found in {directory}")
        return

    success_count = 0
    for md_file in md_files:
        file_path = os.path.join(directory, md_file)
        if replace_in_file(file_path, target, replacement, dry_run):
            success_count += 1

    action = "Would process" if dry_run else "Processed"
    print(f"Replacement complete. {action} {success_count} out of {
          len(md_files)} files successfully.")


if __name__ == "__main__":
    main(TARGET, REPLACEMENT, DIRECTORY, DRY_RUN)
