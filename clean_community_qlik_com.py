import os
import re
from bs4 import BeautifulSoup


def clean_content(content):
    # Remove HTML tags
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()

    # Remove navigation links
    text = re.sub(r'\[.*?\]', '', text)

    # Remove footer information
    text = re.sub(r'©.*?Reserved', '', text)

    # Remove cookie consent information
    text = re.sub(r'General Information on Cookies.*?Confirm My Choices',
                  '', text, flags=re.DOTALL)

    # Remove search bar descriptions
    text = re.sub(r'Auto-suggest helps you.*', '', text)

    # Remove UI elements
    text = re.sub(r'(Mark as New|Subscribe|Bookmark|Mute)', '', text)

    # Remove view counts and likes
    text = re.sub(r'\d+ Views|\d+ Likes?', '', text)

    # Remove repeated boilerplate text
    text = re.sub(r'(word\s*){10,}', '', text)
    text = re.sub(r'(mmMwWLliI0fiflO&1\s*){2,}', '', text)

    # Remove tracking pixels and scripts
    text = re.sub(r'!\[Image \d+\].*', '', text)

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = clean_content(content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)


def main():
    data_dir = 'data/'
    for filename in os.listdir(data_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(data_dir, filename)
            process_file(file_path)
            print(f"Processed: {filename}")


if __name__ == "__main__":
    main()
