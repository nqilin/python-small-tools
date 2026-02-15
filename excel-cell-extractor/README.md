# Excel Cell Extractor
A simple Python tool to extract specified column data from Excel files and save to a text file.

## Problem Description
This tool helps users quickly extract data from a specific column in an Excel spreadsheet and save the results to a text file. It is designed for data processing tasks where column extraction is needed.

## Environment Requirements
- Python 3.8 or higher
- openpyxl library (install: `pip install openpyxl`)

## How to Run
1. Prepare your Excel file (e.g., `test_data.xlsx`) with a header row.
2. Modify the test code in `extractor.py`:
   ```python
   extract_excel_column("your_excel_path.xlsx", "Your_Column_Name", "output.txt")
