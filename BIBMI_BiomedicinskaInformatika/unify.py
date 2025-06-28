import os
import re

# Directory containing the .md files
directory = '.'

# Pattern to match files like 1_Algoritmizace.md, 2_logika.md, etc.
pattern = re.compile(r'^(\d+)_.*\.md$')

# List of tuples (number, filename)
md_files = []

for filename in os.listdir(directory):
    match = pattern.match(filename)
    if match:
        number = int(match.group(1))
        md_files.append((number, filename))

# Sort files by the number
md_files.sort()

# Output file
with open('merged_output.md', 'w', encoding='utf-8') as outfile:
    for _, filename in md_files:
        with open(filename, 'r', encoding='utf-8') as infile:
            outfile.write(infile.read())
            outfile.write('\n\n')  # Separate files with a blank line
