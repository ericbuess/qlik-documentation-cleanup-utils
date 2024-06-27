import os
import re
from collections import defaultdict

def extract_domain(filename):
    domains = [
        "qlik.dev", "help.qlik.com", "www.qlik.com",
        "community.qlik.com", "res.cloudinary.com", "staige.qlik.com"
    ]
    for domain in domains:
        if filename.startswith(f"{domain}_") or filename.startswith(f"{domain}"):
            return domain
    return None

def create_merged_dir():
    merged_dir = "merged"
    if not os.path.exists(merged_dir):
        os.makedirs(merged_dir)
    return merged_dir

def generate_delimiter(filename):
    return f"\n\n{'='*50}\n[DOCUMENT_BREAK: {filename}]\n{'='*50}\n\n"

def merge_md_files(directory):
    merged_dir = create_merged_dir()
    md_files = [f for f in os.listdir(directory) if f.endswith('.md')]

    domain_groups = defaultdict(list)
    for file in md_files:
        domain = extract_domain(file)
        if domain:
            domain_groups[domain].append(file)

    for domain, files in domain_groups.items():
        files.sort()
        output_file = os.path.join(merged_dir, f"{domain}.md")
        
        print(f"Merging files for domain: {domain}")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(f"# Merged Markdown files for {domain}\n")
            outfile.write("This document contains multiple Markdown files merged together. ")
            outfile.write("Each file is separated by a distinctive delimiter for easy parsing.\n\n")
            
            for file in files:
                input_file = os.path.join(directory, file)
                print(f"  Adding: {file}")
                try:
                    with open(input_file, 'r', encoding='utf-8') as infile:
                        outfile.write(generate_delimiter(file))
                        outfile.write(infile.read())
                except Exception as e:
                    print(f"Error processing {file}: {str(e)}")

        print(f"Created: {output_file}")
        print(f"Total files merged: {len(files)}")
        print()

if __name__ == "__main__":
    data_dir = "data"
    if not os.path.isdir(data_dir):
        print(f"Error: {data_dir} directory not found.")
    else:
        merge_md_files(data_dir)
        print("Merging process completed.")