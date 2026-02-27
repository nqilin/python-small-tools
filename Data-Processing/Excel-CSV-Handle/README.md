# Excel/CSV Data Processing Tool
A powerful batch data processing tool for Excel and CSV files that automates common data cleaning tasks: duplicate removal, missing value handling, format standardization, and cross-format conversion. Designed for data analysts and Python data processing practice.

## 📋 Features
- **Batch Processing**: Support single file or entire directory (recursive scan)
- **Multi-Format Support**:
  - Input: Excel (.xlsx/.xls) and CSV files
  - Output: Excel (.xlsx) or CSV (UTF-8 encoded)
- **Comprehensive Data Cleaning**:
  - Remove empty rows/columns
  - Remove duplicate rows (with count tracking)
  - Handle missing values (numeric: mean fill; text: "N/A" fill)
  - Standardize column names (lowercase, replace spaces with underscores)
- **Encoding Compatibility**: Auto-detect CSV encodings (UTF-8, GBK, GB2312, Latin-1)
- **Error Handling**: Robust error catching for file loading/saving
- **Progress Tracking**: Real-time processing progress and summary report
- **Data Preservation**: Process copies (original files remain unchanged)
- **Cross-Platform**: Compatible with Windows/macOS/Linux

## 🛠️ How to Run
### 1. Install Dependencies
```bash
# Install required libraries
pip install pandas openpyxl numpy xlrd
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd Data-Processing/Excel-CSV-Handle

# Run processing tool
python excel_csv_handle.py
```

### 3. Follow the Prompts
1. Enter input file path or directory path
2. Select output format (xlsx/csv, default: xlsx)
3. Wait for processing to complete
4. Check cleaned files in `processed_data_files/` directory

## 📸 Running Example
```
===== Python Excel/CSV Data Processing Tool v1.0 =====
Batch process Excel/CSV files: clean data, remove duplicates, standardize format

Enter input file/directory path: ./raw_data

Select output format (xlsx/csv, default: xlsx): xlsx

📁 Output directory: /Users/yourname/python-small-tools/Data-Processing/Excel-CSV-Handle/processed_data_files

🔍 Scanning for Excel/CSV files...
✅ Found 5 data files to process

🚀 Starting data processing...

🔄 Processing file 1/5: sales_data.csv
✅ Processed: ./raw_data/sales_data.csv
   - Duplicates removed: 12
   - Cleaned rows: 488
   - Saved to: processed_data_files/sales_data_cleaned_20260226_143022.xlsx

🔄 Processing file 2/5: customer_info.xlsx
✅ Processed: ./raw_data/customer_info.xlsx
   - Duplicates removed: 8
   - Cleaned rows: 245
   - Saved to: processed_data_files/customer_info_cleaned_20260226_143025.xlsx

...

🎉 Processing completed!
✅ Successfully processed: 5/5 files
📂 All processed files saved to: /Users/yourname/python-small-tools/Data-Processing/Excel-CSV-Handle/processed_data_files

👋 Thank you for using Excel/CSV Data Processing Tool!
```

## 📝 Development Details
- Uses `pandas` for professional data manipulation (industry standard)
- Multi-encoding support for CSV files (solves Chinese garbled text issue)
- Non-destructive processing (original files remain unchanged)
- Timestamped output filenames (avoid overwriting existing files)
- Detailed processing metrics (duplicate count, cleaned rows)
- Modular design (separate functions for load/clean/save)
- Comprehensive error handling for file operations
- Support for multiple sheets in Excel files

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Libraries:
  ```bash
  pip install pandas openpyxl numpy xlrd
  ```

## ⚠️ Important Notes
- For large Excel files (>100MB), processing may take longer (depends on system resources)
- CSV encoding detection supports common encodings (UTF-8, GBK, GB2312, Latin-1)
- Numeric missing values are filled with column mean (statistically reasonable)
- Text missing values are filled with "N/A" (clear identification of missing data)
- Column names are standardized to lowercase with underscores (consistent format)
