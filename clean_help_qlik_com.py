import os
import re


def clean_md_file(content):
    # Remove specific navigation menu items
    content = re.sub(
        r'\n\* \((https?://.*?(?:qlik\.com|community\.qlik\.com|learning\.qlik\.com).*?)\)', '', content)

    # Remove language selection options
    content = re.sub(r'English \(Change\).*?Close',
                     '', content, flags=re.DOTALL)

    # Remove copyright and legal information
    content = re.sub(r'Copyright © .*?$', '', content, flags=re.MULTILINE)
    content = re.sub(r'Legal.*?terms\)', '', content, flags=re.DOTALL)

    # Remove social media links
    content = re.sub(r'\* \(http://help\.qlik\.com/img/social/.*?\)',
                     '', content, flags=re.MULTILINE)

    # Remove company information and contact details
    content = re.sub(r'Company.*?\+18666164960\)',
                     '', content, flags=re.DOTALL)

    # Remove repeated header and footer content
    content = re.sub(r'Help Resources.*?resource-library\)',
                     '', content, flags=re.DOTALL)

    # Remove specific tracking pixels and analytics code
    content = re.sub(
        r'!\(https://(?:cdn\.bizible\.com|s\.ml-attr\.com|cdn\.cookielaw\.org).*?\)', '', content)

    # Remove "DID THIS PAGE HELP YOU?" sections and similar feedback content
    content = re.sub(r'DID THIS PAGE HELP YOU\?.*?Leave your feedback here',
                     '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'Did this page help you\?.*?how we can improve!',
                     '', content, flags=re.DOTALL | re.IGNORECASE)

    # Remove navigation breadcrumbs
    content = re.sub(r'\d+\. \(http://help\.qlik\.com/.*?\)',
                     '', content, flags=re.MULTILINE)

    # Remove "ON THIS PAGE" sections
    content = re.sub(r'ON THIS PAGE.*?\n\n', '', content, flags=re.DOTALL)

    # Remove "Search" and "Menu" instructions
    content = re.sub(r'Search.*?knowledge articles',
                     '', content, flags=re.DOTALL)
    content = re.sub(r'Menu.*?Close', '', content, flags=re.DOTALL)

    # Remove navigation instructions
    content = re.sub(r'Navigate.*?Back', '', content, flags=re.DOTALL)

    # Remove empty lines and extra whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    content = content.strip()

    return content


def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                cleaned_content = clean_md_file(content)

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)

                print(f"Processed: {file_path}")


if __name__ == "__main__":
    data_directory = "data/"
    process_directory(data_directory)
    print("Finished processing all .md files in the data/ directory.")
