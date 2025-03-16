"""
hex_xml_parser.py

Parses and extracts XML data blocks from an Intel HEX file, focusing on <i64> tags.
Outputs the offset of each XML block and the numbers within <i64> tags.

Usage:
    python hex_xml_parser.py <input_file>

Requirements:
    - Python 3.x
    - intelhex library (`pip install intelhex`)
    - re (regular expression) module (included in Python standard library)

Input:
    - Path to an Intel HEX file

Output:
    - Prints the offset and parsed <i64> block contents to console
    - Saves results to 'xml_blocks.txt' (optional)
"""

import re
from intelhex import IntelHex
import os
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Parse XML blocks from a HEX file.")
parser.add_argument("input_file", help="Path to the Intel HEX file")
args = parser.parse_args()
input_file = args.input_file

# Check if the file exists
if not os.path.exists(input_file):
    print(f"Error: File {input_file} does not exist!")
    exit(1)

# Read the HEX file
try:
    ih = IntelHex(input_file)
    data = ih.tobinstr()
except Exception as e:
    print(f"Error: Failed to read HEX file, error message: {e}")
    exit(1)

# Extract XML blocks
current_string = ""
xml_blocks = []
for i, byte in enumerate(data):
    if 0x20 <= byte <= 0x7e:  # ASCII printable character range
        current_string += chr(byte)
    else:
        if current_string and "<c>" in current_string:
            xml_blocks.append((i - len(current_string), current_string))
        current_string = ""

# Parse and print XML data
print("Parsed XML blocks:")
for offset, block in xml_blocks:
    print(f"\nOffset: 0x{offset:08x}")
    # Extract all <i64> tags and their numbers
    i64_blocks = re.findall(r"<i64>(.*?)</i64>", block)
    for idx, i64 in enumerate(i64_blocks):
        numbers = i64.strip().split()
        print(f"i64 Block {idx + 1}: {numbers}")

# Save results to file (optional)
with open("xml_blocks.txt", "w") as f:
    print("Parsed XML blocks:", file=f)
    for offset, block in xml_blocks:
        print(f"\nOffset: 0x{offset:08x}", file=f)
        i64_blocks = re.findall(r"<i64>(.*?)</i64>", block)
        for idx, i64 in enumerate(i64_blocks):
            numbers = i64.strip().split()
            print(f"i64 Block {idx + 1}: {numbers}", file=f)

print("Parsing results have been saved to xml_blocks.txt")