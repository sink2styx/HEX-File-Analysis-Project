"""
extract_ascii_strings.py

Extracts continuous ASCII printable strings from an Intel HEX file.
Outputs the offset (in hex) and the string content to console and a file.

Usage:
    python ascii_from_hex.py <input_file>

Requirements:
    - Python 3.x
    - intelhex library (`pip install intelhex`)

Input:
    - Path to an Intel HEX file

Output:
    - Prints offsets and ASCII strings to console
    - Saves results to 'ascii_strings.txt'
"""

from intelhex import IntelHex
import os
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Extract ASCII strings from a HEX file.")
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

# Extract continuous ASCII characters and save to file
with open("ascii_strings.txt", "w") as f:
    current_string = ""
    for i, byte in enumerate(data):
        if 0x20 <= byte <= 0x7e:  # ASCII printable character range
            current_string += chr(byte)
        else:
            if current_string:
                print(f"Offset: 0x{i-len(current_string):08x}, String: {current_string}", file=f)
                print(f"Offset: 0x{i-len(current_string):08x}, String: {current_string}")
                current_string = ""
    if current_string:
        print(f"Offset: 0x{i-len(current_string)+1:08x}, String: {current_string}", file=f)
        print(f"Offset: 0x{i-len(current_string)+1:08x}, String: {current_string}")

print("Extraction results have been saved to ascii_strings.txt")