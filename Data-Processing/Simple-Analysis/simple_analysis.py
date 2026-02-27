import pandas as pd
import numpy as np
import os
from datetime import datetime

# Supported file formats
SUPPORTED_FORMATS = ['.xlsx', '.xls', '.csv']

def validate_file_path(file_path):
    """Validate input data file path"""
    if not os.path.exists(file_path):
        print(f"❌ File does not exist: {file_path}")
        return False
    
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext not in SUPPORTED_FORMATS:
        print(f"❌ Unsupported file format: {file_ext} (only Excel/CSV supported)")
        return False
    
    return True

def load_data_file(file_path):
    """Load Excel/CSV data file with encoding detection"""
    file_ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_ext in ['.xlsx', '.xls']:
            df = pd.read_excel(file_path, sheet_name=0)
        elif file_ext == '.csv':
            encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    break
                except UnicodeDecodeError:
                    continue
            else:
                print(f"❌ Failed to decode CSV file: {file_path}")
                return None
        
        if df.empty:
            print("❌ Loaded data file is empty!")
            return None
        
        print(f"✅ Successfully loaded data: {file_path}")
        print(f"   - Rows: {len(df)}, Columns: {len(df.columns)}")
        return df
    
    except Exception as e:
        print(f"❌ Failed to load data file: {e}")
        return None

def generate_basic_stats(df):
    """Generate basic descriptive statistics for numeric columns"""
    print("\n===== Basic Descriptive Statistics =====")
    numeric_df = df.select_dtypes(include=[np.number])
    
    if numeric_df.empty:
        print("❌ No numeric columns found for statistics!")
        return None
    
    stats = numeric_df.describe().T
    stats['missing_values'] = df[numeric_df.columns].isnull().sum()
    stats['missing_percent'] = (df[numeric_df.columns].isnull().sum() / len(df)) * 100
    
    print(stats.round(2))
    return stats

def generate_correlation_analysis(df):
    """Generate correlation matrix for numeric columns"""
    print("\n===== Correlation Analysis =====")
    numeric_df = df.select_dtypes(include=[np.number])
    
    if len(numeric_df.columns) < 2:
        print("❌ Need at least 2 numeric columns for correlation analysis!")
        return None
    
    corr_matrix = numeric_df.corr()
    print(corr_matrix.round(2))
    return corr_matrix

def generate_categorical_analysis(df):
    """Generate frequency analysis for categorical columns"""
    print("\n===== Categorical Column Analysis =====")
    cat_df = df.select_dtypes(include=['object'])
    
    if cat_df.empty:
        print("❌ No categorical columns found!")
        return None
    
    for col in cat_df.columns:
        print(f"\n--- {col} ---")
        freq = df[col].value_counts().head(10)
        print(freq)
        print(f"Unique values: {df[col].nunique()}")

def generate_analysis_report(df, output_dir="analysis_reports"):
    """Generate comprehensive analysis report and save to file"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"data_analysis_report_{timestamp}.txt"
    report_path = os.path.join(output_dir, report_filename)
    
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write("===== DATA ANALYSIS REPORT =====\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Data shape: {len(df)} rows, {len(df.columns)} columns\n\n")
            
            f.write("===== Basic Statistics =====\n")
            stats = generate_basic_stats(df)
            if stats is not None:
                f.write(stats.round(2).to_string())
            
            f.write("\n\n===== Correlation Analysis =====\n")
            corr = generate_correlation_analysis(df)
            if corr is not None:
                f.write(corr.round(2).to_string())
            
            f.write("\n\n===== Categorical Analysis =====\n")
            generate_categorical_analysis(df)
            # Re-run to capture output for file (simplified)
            cat_df = df.select_dtypes(include=['object'])
            if not cat_df.empty:
                for col in cat_df.columns:
                    f.write(f"\n--- {col} ---\n")
                    freq = df[col].value_counts().head(10)
                    f.write(freq.to_string())
                    f.write(f"\nUnique values: {df[col].nunique()}\n")
        
        print(f"\n✅ Analysis report saved to: {report_path}")
        return True
    
    except Exception as e:
        print(f"\n❌ Failed to save analysis report: {e}")
        return False

def main():
    """Main function: run simple data analysis tool"""
    print("===== Python Simple Data Analysis Tool v1.0 =====")
    print("Generate comprehensive statistics and analysis from Excel/CSV data\n")
    
    # Get input file
    while True:
        file_path = input("Enter Excel/CSV data file path: ").strip()
        if validate_file_path(file_path):
            break
    
    # Load data
    df = load_data_file(file_path)
    if df is None:
        return
    
    # Generate analysis
    print("\n🚀 Starting data analysis...")
    
    generate_basic_stats(df)
    generate_correlation_analysis(df)
    generate_categorical_analysis(df)
    
    # Save report
    save_report = input("\nSave analysis report to file? (Y/N): ").strip().upper()
    if save_report == "Y":
        generate_analysis_report(df)
    
    print("\n🎉 Analysis completed successfully!")
    print("👋 Thank you for using Simple Data Analysis Tool!")

if __name__ == "__main__":
    main()
