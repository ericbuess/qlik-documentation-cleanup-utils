import os
import re
import json


def clean_content(content):
    # Remove links at the beginning
    cleaned = re.sub(r'^(\* \(https?://.*?\)\n)+',
                     '', content, flags=re.MULTILINE)

    # Remove empty lines at the beginning
    cleaned = re.sub(r'^\s*\n', '', cleaned)

    # Find the first meaningful content
    match = re.search(r'\n\n([A-Z].*?)\n=+\n', cleaned)
    if match:
        return cleaned[match.start():]

    # If no title is found, return the cleaned content as is
    return cleaned


def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find all data sections
        data_matches = list(re.finditer(
            r'event: data data: ({.*?})', content, re.DOTALL))

        if not data_matches:
            print(f"No data sections found in {file_path}")
            return

        modified = False
        new_content = content

        for i, data_match in enumerate(data_matches):
            data_str = data_match.group(1)

            try:
                data = json.loads(data_str)
                if 'content' in data:
                    content_text = data['content']

                    # Clean the content
                    new_content_text = clean_content(content_text)

                    if new_content_text != content_text:
                        # Replace the old content with the new content
                        data['content'] = new_content_text
                        new_data_str = json.dumps(data)
                        new_content = new_content.replace(
                            data_str, new_data_str)
                        modified = True
                        print(f"Processed content section {
                              i+1} in {file_path}")
                    else:
                        print(f"No changes needed in section {
                              i+1} of {file_path}")
                else:
                    print(f"No 'content' field found in section {
                          i+1} of {file_path}")
            except json.JSONDecodeError:
                print(f"Invalid JSON in section {i+1} of {file_path}")

        if modified:
            # Write the modified content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Processed: {file_path}")
        else:
            print(f"Skipped: {file_path} (No changes needed)")

    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")


def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)


# Specify the directory path
data_directory = 'data'

# Process all files in the directory
process_directory(data_directory)

print("Processing complete.")
