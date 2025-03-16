# HEX File Analysis Project

## Overview
This project analyzes a HEX file (`119324.hex`) to extract configuration and test data for 8 chips. The file contains XML-formatted data with calibration parameters and test results.

## Files
- `analyze_hex.py`: Extracts non-FF bytes from the HEX file.
- `parse_xml.py`: Parses XML data blocks.
- `split_chips.py`: Splits the file into 8KB chunks for each chip.
- `output/`: Contains parsed results (e.g., non-FF bytes, XML data).

## Requirements
- Python 3.x
- `intelhex` library (`pip install intelhex`)

## Usage
1. Run `analyze_hex.py` to extract non-FF bytes:
   ```bash
   python analyze_hex.py