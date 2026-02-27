# Simple Data Analysis Tool
A lightweight data analysis tool that generates comprehensive statistics, correlation analysis, and categorical insights from Excel/CSV data files. Designed for quick data exploration and Python data analysis practice.

## 📋 Features
- **Basic Statistics**: Descriptive stats (mean, std, min/max, quartiles) for numeric columns
- **Missing Value Analysis**: Count and percentage of missing values per column
- **Correlation Analysis**: Pearson correlation matrix for numeric columns
- **Categorical Analysis**: Frequency counts and unique value counts for text columns
- **Report Generation**: Save comprehensive analysis to timestamped text file
- **Encoding Support**: Auto-detect CSV encodings (UTF-8, GBK, GB2312, Latin-1)
- **Error Handling**: Robust error catching for file operations and data processing
- **Cross-Platform**: Compatible with Windows/macOS/Linux

## 🛠️ How to Run
### 1. Install Dependencies
```bash
pip install pandas numpy openpyxl xlrd
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd Data-Processing/Simple-Analysis

# Run analysis tool
python simple_analysis.py
```

### 3. Follow the Prompts
1. Enter Excel/CSV data file path
2. View real-time analysis results
3. Choose to save comprehensive report to `analysis_reports/` directory

## 📸 Running Example
```
===== Python Simple Data Analysis Tool v1.0 =====
Generate comprehensive statistics and analysis from Excel/CSV data

Enter Excel/CSV data file path: ./sales_data.csv
✅ Successfully loaded data: ./sales_data.csv
   - Rows: 500, Columns: 6

🚀 Starting data analysis...

===== Basic Descriptive Statistics =====
           count   mean    std    min    25%    50%    75%    max  missing_values  missing_percent
sales      500.0  452.3  215.7   99.0  289.0  421.0  587.0  999.0               0              0.0
profit     500.0   89.5   45.2   10.0   55.0   85.0  120.0  250.0               0              0.0
quantity   500.0   12.3    5.1    1.0    8.0   12.0   16.0   25.0               0              0.0

===== Correlation Analysis =====
          sales  profit  quantity
sales     1.000   0.872     0.654
profit    0.872   1.000     0.589
quantity  0.654   0.589     1.000

===== Categorical Column Analysis =====

--- region ---
North    150
South    120
East     130
West     100
Name: region, dtype: int64
Unique values: 4

--- product ---
A        200
B        150
C        100
D         50
Name: product, dtype: int64
Unique values: 4

Save analysis report to file? (Y/N): Y
✅ Analysis report saved to: analysis_reports/data_analysis_report_20260226_183045.txt

🎉 Analysis completed successfully!
👋 Thank you for using Simple Data Analysis Tool!
```

## 📝 Development Details
- Uses `pandas` for professional data analysis (industry standard)
- Comprehensive missing value analysis (count + percentage)
- Pearson correlation matrix for numeric column relationships
- Frequency counts for categorical data (top 10 values)
- Timestamped report filenames (avoid overwriting existing files)
- Modular design (separate functions for different analysis types)
- Cross-platform compatibility (Windows/macOS/Linux)

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Libraries:
  ```bash
  pip install pandas numpy openpyxl xlrd
  ```

## ⚠️ Important Notes
- Correlation analysis requires at least 2 numeric columns
- Categorical analysis shows top 10 values for readability
- Large datasets (>10,000 rows) may take longer to process
- Analysis reports are saved as plain text files for easy sharing
