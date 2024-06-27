import os
import re


def clean_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove navigation menu links (typically short links in parentheses)
    content = re.sub(r'\*\s*\((http[^)]{1,100}?)\)\n', '', content)

    # Remove language selection options
    content = re.sub(r'\*\s*\(.*?\?l=.*?\)\n', '', content)

    # Remove social media links
    content = re.sub(
        r'\]\(https?://(?:www\.)?(?:twitter|linkedin|facebook)\.com/.*?\)\n', '', content)

    # Remove legal footer
    content = re.sub(r'Legal\n-----\n', '', content)

    # Remove feedback links
    content = re.sub(r'Leave your feedback here.*?javascript:void\\\(0\\\)\)',
                     '', content, flags=re.DOTALL)

    # Remove table of contents links
    content = re.sub(r'ON THIS PAGE.*?\n-+\n.*?\n\n',
                     '', content, flags=re.DOTALL)

    # Remove skip to main content links
    content = re.sub(r'\(javascript:skipToMain.*?\n', '', content)

    # Remove Qlik logo and branding elements
    content = re.sub(
        r'\(http://help\.qlik\.com/img/logos/Qlik-Help-.*?\.svg\)\].*?\n', '', content)

    # Remove empty lines and whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = content.strip()

    return content


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}")
                cleaned_content = clean_md_file(file_path)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)


if __name__ == "__main__":
    data_directory = "data/"
    process_directory(data_directory)
    print("Finished processing all .md files in the data/ directory.")
