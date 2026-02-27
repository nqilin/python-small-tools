import pandas as pd
import os
import numpy as np
from datetime import datetime

# Supported file formats
SUPPORTED_FORMATS = ['.xlsx', '.xls', '.csv']

def create_output_directory():
    """Create output directory for processed files"""
    output_dir = "processed_data_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def validate_file_path(input_path):
    """Validate input file/directory path"""
    if not os.path.exists(input_path):
        print(f"❌ Path does not exist: {input_path}")
        return False
    return True

def get_data_files(input_path):
    """Get all supported data files (Excel/CSV) from path"""
    data_files = []
    
    if os.path.isfile(input_path):
        # Single file
        file_ext = os.path.splitext(input_path)[1].lower()
        if file_ext in SUPPORTED_FORMATS:
            data_files.append(input_path)
        else:
            print(f"❌ Unsupported file format: {input_path}")
    else:
        # Directory - recursive scan
        for root, _, files in os.walk(input_path):
            for file in files:
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in SUPPORTED_FORMATS:
                    data_files.append(os.path.join(root, file))
    
    if not data_files:
        print("❌ No supported data files found (Excel/CSV)")
        return None
    return data_files

def load_data_file(file_path):
    """Load Excel/CSV file with error handling and encoding detection"""
    file_ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_ext in ['.xlsx', '.xls']:
            # Load Excel file (all sheets)
            df_dict = pd.read_excel(file_path, sheet_name=None)
            return df_dict, "excel"
        elif file_ext == '.csv':
            # Try different encodings for CSV files
            encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    return {"Sheet1": df}, "csv"
                except UnicodeDecodeError:
                    continue
            print(f"❌ Failed to decode CSV file: {file_path} (tried multiple encodings)")
            return None, None
    except Exception as e:
        print(f"❌ Failed to load {file_path}: {e}")
        return None, None

def clean_data(df):
    """Clean data with common operations (missing values, duplicates, data types)"""
    # Create a copy to avoid modifying original data
    cleaned_df = df.copy()
    
    # 1. Remove completely empty rows/columns
    cleaned_df = cleaned_df.dropna(how='all')
    cleaned_df = cleaned_df.dropna(axis=1, how='all')
    
    # 2. Remove duplicate rows
    initial_rows = len(cleaned_df)
    cleaned_df = cleaned_df.drop_duplicates()
    duplicate_count = initial_rows - len(cleaned_df)
    
    # 3. Handle missing values (numeric columns: fill with mean; text: fill with "N/A")
    for col in cleaned_df.columns:
        if cleaned_df[col].dtype in ['int64', 'float64']:
            # Numeric column - fill with mean
            cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())
        else:
            # Text column - fill with N/A
            cleaned_df[col] = cleaned_df[col].fillna("N/A")
    
    # 4. Standardize column names (lowercase, replace spaces with underscores)
    cleaned_df.columns = [col.strip().lower().replace(' ', '_') for col in cleaned_df.columns]
    
    return cleaned_df, duplicate_count

def process_data_file(file_path, output_dir, output_format='xlsx'):
    """Process single data file (load → clean → save)"""
    # Load file
    data_dict, file_type = load_data_file(file_path)
    if not data_dict:
        return False
    
    # Generate output filename
    file_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(file_name)[0]
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"{name_without_ext}_cleaned_{timestamp}.{output_format}"
    output_path = os.path.join(output_dir, output_filename)
    
    # Process each sheet
    total_duplicates = 0
    total_rows_cleaned = 0
    
    try:
        if output_format == 'xlsx':
            # Save to Excel with multiple sheets
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                for sheet_name, df in data_dict.items():
                    cleaned_df, duplicates = clean_data(df)
                    cleaned_df.to_excel(writer, sheet_name=sheet_name, index=False)
                    total_duplicates += duplicates
                    total_rows_cleaned += len(cleaned_df)
        elif output_format == 'csv':
            # Save to CSV (only first sheet for CSV output)
            first_sheet_name = next(iter(data_dict.keys()))
            df = data_dict[first_sheet_name]
            cleaned_df, duplicates = clean_data(df)
            cleaned_df.to_csv(output_path, index=False, encoding='utf-8')
            total_duplicates = duplicates
            total_rows_cleaned = len(cleaned_df)
        
        print(f"✅ Processed: {file_path}")
        print(f"   - Duplicates removed: {total_duplicates}")
        print(f"   - Cleaned rows: {total_rows_cleaned}")
        print(f"   - Saved to: {output_path}\n")
        return True
    
    except Exception as e:
        print(f"❌ Failed to save processed file: {e}\n")
        return False

def main():
    """Main function: run Excel/CSV data processing tool"""
    print("===== Python Excel/CSV Data Processing Tool v1.0 =====")
    print("Batch process Excel/CSV files: clean data, remove duplicates, standardize format\n")
    
    # Get input path
    while True:
        input_path = input("Enter input file/directory path: ").strip()
        if validate_file_path(input_path):
            break
    
    # Get output format
    while True:
        output_format = input("\nSelect output format (xlsx/csv, default: xlsx): ").strip().lower()
        if output_format in ['xlsx', 'csv', '']:
            output_format = output_format if output_format else 'xlsx'
            break
        print("❌ Please enter 'xlsx' or 'csv'!")
    
    # Create output directory
    output_dir = create_output_directory()
    print(f"\n📁 Output directory: {os.path.abspath(output_dir)}")
    
    # Get data files
    print("\n🔍 Scanning for Excel/CSV files...")
    data_files = get_data_files(input_path)
    if not data_files:
        return
    
    print(f"✅ Found {len(data_files)} data files to process\n")
    
    # Process files
    print("🚀 Starting data processing...\n")
    success_count = 0
    for i, file_path in enumerate(data_files, 1):
        print(f"🔄 Processing file {i}/{len(data_files)}: {os.path.basename(file_path)}")
        if process_data_file(file_path, output_dir, output_format):
            success_count += 1
    
    # Summary
    print("🎉 Processing completed!")
    print(f"✅ Successfully processed: {success_count}/{len(data_files)} files")
    print(f"📂 All processed files saved to: {os.path.abspath(output_dir)}")
    print("\n👋 Thank you for using Excel/CSV Data Processing Tool!")

if __name__ == "__main__":
    main()
