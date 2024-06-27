import json
import re


def parse_sitemap(input_file, output_file):
    # Regular expression to split the content based on the timestamp pattern
    split_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z'

    # Read the input file
    with open(input_file, 'r') as file:
        content = file.read()

    # Split the content and filter out empty strings
    parts = re.split(split_pattern, content)
    urls = [part for part in parts if part.strip()]

    # Clean up URLs (remove any remaining timestamps and whitespace)
    urls = [url.strip() for url in urls]

    # Write URLs to JSON file
    with open(output_file, 'w') as file:
        json.dump(urls, file, indent=2)

    print(f"Parsed {len(urls)} URLs and saved to {output_file}")


# File paths
input_file = 'qlik_com_sitemap.txt'
output_file = 'sitemap_queue.json'

# Run the parser
parse_sitemap(input_file, output_file)
