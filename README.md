# HEX File Analysis Project

## Overview
This project analyzes a HEX file (`119324.hex`) to extract configuration and test data for 8 chips. The file contains XML-formatted data with calibration parameters and test results.

## Files
- `analyze_hex.py`: Extracts non-FF bytes from the HEX file.
- `parse_xml.py`: Parses XML data blocks.
- `split_chips.py`: Splits the file into 8KB chunks for each chip.
- `output/`: Contains parsed results (e.g., non-FF bytes, XML data).
- `ascii_from_hex.py`: Main script to extract ASCII strings.

## Requirements
- Python 3.x
- `intelhex` library (`pip install intelhex`)

## Usage

Run the script with the path to your HEX file:

```bash
python ascii_from_hex.py path/to/your/file.hex
```

