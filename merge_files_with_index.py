import os
import shutil

MAX_FILE_SIZE = 6.1 * 1024 * 1024  # < 10 MB in bytes
OUTPUT_DIR = "merged_with_index"
DATA_DIR = "data"

def get_md_files(directory):
    md_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return sorted(md_files)

def merge_files(file_list, output_file, max_size):
    current_size = 0
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_path in file_list:
            file_size = os.path.getsize(file_path)
            if current_size + file_size > max_size:
                return False
            with open(file_path, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read() + '\n\n')
            current_size += file_size
    return True

def main():
    md_files = get_md_files(DATA_DIR)
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    current_index = 1
    current_file_list = []
    
    for file_path in md_files:
        current_file_list.append(file_path)
        output_file = os.path.join(OUTPUT_DIR, f"qlik_{current_index:02d}.md")
        
        if not merge_files(current_file_list, output_file, MAX_FILE_SIZE):
            # If merging fails due to size limit, start a new file
            current_file_list = [file_path]
            current_index += 1
            output_file = os.path.join(OUTPUT_DIR, f"qlik_{current_index:02d}.md")
            merge_files(current_file_list, output_file, MAX_FILE_SIZE)
    
    print(f"Merged files have been created in the '{OUTPUT_DIR}' directory.")

if __name__ == "__main__":
    main()