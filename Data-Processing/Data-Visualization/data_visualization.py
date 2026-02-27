import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from datetime import datetime

# Set matplotlib to support Chinese characters (cross-platform)
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'SimHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # Fix negative sign display

# Supported chart types
CHART_TYPES = {
    "bar": "Bar Chart (categorical data comparison)",
    "line": "Line Chart (trend over time)",
    "pie": "Pie Chart (proportion distribution)",
    "hist": "Histogram (numeric data distribution)",
    "scatter": "Scatter Plot (correlation analysis)"
}

def create_output_directory():
    """Create output directory for visualization charts"""
    output_dir = "data_visualization_charts"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def validate_file_path(file_path):
    """Validate input data file path"""
    if not os.path.exists(file_path):
        print(f"❌ File does not exist: {file_path}")
        return False
    
    # Check file format
    file_ext = os.path.splitext(file_path)[1].lower()
    if file_ext not in ['.xlsx', '.xls', '.csv']:
        print(f"❌ Unsupported file format: {file_ext} (only Excel/CSV supported)")
        return False
    
    return True

def load_data_file(file_path):
    """Load Excel/CSV data file with encoding detection"""
    file_ext = os.path.splitext(file_path)[1].lower()
    
    try:
        if file_ext in ['.xlsx', '.xls']:
            # Load Excel file (first sheet)
            df = pd.read_excel(file_path, sheet_name=0)
        elif file_ext == '.csv':
            # Try different encodings for CSV
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
        
        # Basic data validation
        if df.empty:
            print("❌ Loaded data file is empty!")
            return None
        
        print(f"✅ Successfully loaded data: {file_path}")
        print(f"   - Rows: {len(df)}, Columns: {len(df.columns)}")
        print(f"   - Columns: {', '.join(df.columns)}")
        return df
    
    except Exception as e:
        print(f"❌ Failed to load data file: {e}")
        return None

def get_column_choice(df, column_type="all"):
    """Let user select column from dataframe"""
    # Filter columns by type if needed
    if column_type == "numeric":
        columns = df.select_dtypes(include=[np.number]).columns.tolist()
        if not columns:
            print("❌ No numeric columns found in data!")
            return None
    elif column_type == "categorical":
        columns = df.select_dtypes(include=['object']).columns.tolist()
        if not columns:
            print("❌ No categorical columns found in data!")
            return None
    else:
        columns = df.columns.tolist()
    
    # Show column options
    print(f"\nAvailable {column_type} columns:")
    for i, col in enumerate(columns, 1):
        print(f"{i}. {col}")
    
    # Get user choice
    while True:
        try:
            choice = int(input(f"\nSelect {column_type} column (1-{len(columns)}): ")) - 1
            if 0 <= choice < len(columns):
                return columns[choice]
            else:
                print(f"❌ Please enter a number between 1 and {len(columns)}!")
        except ValueError:
            print("❌ Please enter a valid number!")

def generate_chart(df, chart_type, x_col, y_col=None, output_dir):
    """Generate specified chart type with professional styling"""
    # Create figure with good size
    plt.figure(figsize=(12, 8))
    
    # Set professional style
    sns.set_style("whitegrid")
    colors = sns.color_palette("husl", 8)
    
    # Generate chart based on type
    chart_title = f"{chart_type.capitalize()} Chart: {x_col} vs {y_col if y_col else 'Value'}"
    filename = f"{chart_type}_chart_{x_col}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    file_path = os.path.join(output_dir, filename)
    
    try:
        if chart_type == "bar":
            # Bar chart
            if y_col:
                sns.barplot(x=x_col, y=y_col, data=df, palette=colors)
            else:
                # Count plot if no y column
                sns.countplot(x=x_col, data=df, palette=colors)
        
        elif chart_type == "line":
            # Line chart
            if y_col:
                # Sort by x column if numeric
                if pd.api.types.is_numeric_dtype(df[x_col]):
                    df_sorted = df.sort_values(by=x_col)
                else:
                    df_sorted = df
                sns.lineplot(x=x_col, y=y_col, data=df_sorted, marker='o', color=colors[0])
            else:
                print("❌ Line chart requires Y column for values!")
                return False
        
        elif chart_type == "pie":
            # Pie chart (only x column needed)
            if y_col:
                # Use y column as values
                pie_data = df.groupby(x_col)[y_col].sum()
            else:
                # Use count of x column
                pie_data = df[x_col].value_counts()
            
            # Filter small slices (<5%) for better readability
            threshold = 0.05
            pie_data_filtered = pie_data[pie_data / pie_data.sum() >= threshold]
            other_sum = pie_data[pie_data / pie_data.sum() < threshold].sum()
            
            if other_sum > 0:
                pie_data_filtered['Other'] = other_sum
            
            # Create pie chart
            plt.pie(pie_data_filtered, labels=pie_data_filtered.index, autopct='%1.1f%%',
                    colors=colors, startangle=90)
            plt.axis('equal')  # Equal aspect ratio for circular pie
        
        elif chart_type == "hist":
            # Histogram (only x column needed, must be numeric)
            if not pd.api.types.is_numeric_dtype(df[x_col]):
                print(f"❌ Histogram requires numeric column ('{x_col}' is non-numeric)!")
                return False
            
            sns.histplot(df[x_col], bins=20, kde=True, color=colors[0])
        
        elif chart_type == "scatter":
            # Scatter plot (requires both x and y columns)
            if not y_col:
                print("❌ Scatter plot requires Y column!")
                return False
            
            # Both columns must be numeric
            if not (pd.api.types.is_numeric_dtype(df[x_col]) and pd.api.types.is_numeric_dtype(df[y_col])):
                print("❌ Scatter plot requires numeric X and Y columns!")
                return False
            
            sns.scatterplot(x=x_col, y=y_col, data=df, s=100, color=colors[0], alpha=0.7)
            
            # Add correlation coefficient
            corr = df[[x_col, y_col]].corr().iloc[0, 1]
            plt.annotate(f"Correlation: {corr:.2f}", xy=(0.05, 0.95), xycoords='axes fraction',
                        fontsize=12, bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.8))
        
        # Customize chart
        plt.title(chart_title, fontsize=16, pad=20)
        plt.xlabel(x_col, fontsize=12)
        if y_col and chart_type != "pie":
            plt.ylabel(y_col, fontsize=12)
        
        # Rotate x labels for better readability
        plt.xticks(rotation=45, ha='right')
        
        # Tight layout to prevent label cutoff
        plt.tight_layout()
        
        # Save chart
        plt.savefig(file_path, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"✅ Chart saved: {file_path}")
        return True
    
    except Exception as e:
        print(f"❌ Failed to generate {chart_type} chart: {e}")
        plt.close()
        return False

def main():
    """Main function: run data visualization tool"""
    print("===== Python Data Visualization Tool v1.0 =====")
    print("Generate professional charts from Excel/CSV data files\n")
    
    # Get input file
    while True:
        file_path = input("Enter Excel/CSV data file path: ").strip()
        if validate_file_path(file_path):
            break
    
    # Load data
    df = load_data_file(file_path)
    if df is None:
        return
    
    # Create output directory
    output_dir = create_output_directory()
    print(f"\n📁 Chart output directory: {os.path.abspath(output_dir)}")
    
    # Select chart type
    print("\nAvailable chart types:")
    for i, (key, desc) in enumerate(CHART_TYPES.items(), 1):
        print(f"{i}. {desc}")
    
    while True:
        try:
            chart_choice = int(input(f"\nSelect chart type (1-{len(CHART_TYPES)}): ")) - 1
            if 0 <= chart_choice < len(CHART_TYPES):
                chart_type = list(CHART_TYPES.keys())[chart_choice]
                break
            else:
                print(f"❌ Please enter a number between 1 and {len(CHART_TYPES)}!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Select columns
    print("\n=== Column Selection ===")
    
    # Determine column type for X
    if chart_type in ["hist", "scatter"]:
        x_col = get_column_choice(df, "numeric")
    elif chart_type == "pie":
        x_col = get_column_choice(df, "categorical")
    else:
        x_col = get_column_choice(df)
    
    if not x_col:
        return
    
    # Select Y column (if needed)
    y_col = None
    if chart_type in ["bar", "line", "scatter", "pie"]:
        use_y_col = input("\nUse Y column for values? (Y/N, default: N): ").strip().upper()
        if use_y_col == "Y":
            if chart_type == "scatter":
                y_col = get_column_choice(df, "numeric")
            else:
                y_col = get_column_choice(df)
    
    # Generate chart
    print("\n🚀 Generating chart...")
    success = generate_chart(df, chart_type, x_col, y_col, output_dir)
    
    # Summary
    if success:
        print("\n🎉 Chart generation completed successfully!")
        print(f"📂 Chart saved to: {os.path.abspath(output_dir)}")
    else:
        print("\n❌ Chart generation failed!")
    
    print("\n👋 Thank you for using Data Visualization Tool!")

if __name__ == "__main__":
    main()
