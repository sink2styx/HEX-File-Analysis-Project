"""
hex_non_ff_extractor.py

Extracts and prints the positions and values of non-FF bytes from an Intel HEX file.
Also calculates and displays the total number of bytes, non-FF byte count, and percentage.

Usage:
    python hex_non_ff_extractor.py <input_file>

Requirements:
    - Python 3.x
    - intelhex library (`pip install intelhex`)

Input:
    - Path to an Intel HEX file

Output:
    - Prints offsets and values of non-FF bytes to console
    - Displays statistics (total bytes, non-FF count, percentage)
    - Saves results to 'non_ff_bytes.txt' (optional)
"""

from intelhex import IntelHex
import os
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Extract non-FF bytes from a HEX file.")
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

# Print positions and values of non-FF bytes
print("Positions and values of non-FF bytes:")
for i, byte in enumerate(data):
    if byte != 0xFF:
        # Format output: offset (hex) and byte value (hex)
        print(f"Offset: 0x{i:08x}, Value: 0x{byte:02x} ({byte})")

# Calculate statistics for non-FF bytes
non_ff_count = sum(1 for byte in data if byte != 0xFF)
total_bytes = len(data)
print(f"\nTotal bytes: {total_bytes}")
print(f"Non-FF byte count: {non_ff_count}")
print(f"Non-FF byte percentage: {non_ff_count / total_bytes * 100:.2f}%")

# Save results to file (optional)
with open("non_ff_bytes.txt", "w") as f:
    print("Positions and values of non-FF bytes:", file=f)
    for i, byte in enumerate(data):
        if byte != 0xFF:
            print(f"Offset: 0x{i:08x}, Value: 0x{byte:02x} ({byte})", file=f)
    print(f"\nTotal bytes: {total_bytes}", file=f)
    print(f"Non-FF byte count: {non_ff_count}", file=f)
    print(f"Non-FF byte percentage: {non_ff_count / total_bytes * 100:.2f}%", file=f)

print("Extraction results have been saved to non_ff_bytes.txt")