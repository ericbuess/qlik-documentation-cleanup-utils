import os
import re


def clean_md_file(content):
    # Remove navigation links and menus
    content = re.sub(r'\n\* \(.*?\)\n', '\n', content)
    content = re.sub(r'\(javascript:.*?\)', '', content)

    # Remove "ON THIS PAGE" section and its content
    content = re.sub(r'ON THIS PAGE\n------------\n\n.*?\n\n',
                     '', content, flags=re.DOTALL)

    # Remove feedback section
    content = re.sub(r'Leave your feedback here.*?javascript:void\\\(0\\\)\)',
                     '', content, flags=re.DOTALL)

    # Remove social media links
    content = re.sub(
        r'\]\(https://twitter\.com/qlik\).*?Legal\n-----\n', '', content, flags=re.DOTALL)

    # Remove header navigation
    content = re.sub(r'\(javascript:skipToMain.*?\n\n',
                     '', content, flags=re.DOTALL)

    # Remove footer navigation
    content = re.sub(r'\n\(http://help\.qlik\.com/.*?Home\.htm\)\n',
                     '\n', content, flags=re.DOTALL)

    # Remove language selection
    content = re.sub(r'\* \(http://help\.qlik\.com/.*?/RepositoryServiceAPI-.*?\.htm.*?\)\n',
                     '', content, flags=re.MULTILINE)

    # Clean up extra newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                cleaned_content = clean_md_file(content)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)

                print(f"Processed: {file_path}")


# Usage
process_directory('data/')
