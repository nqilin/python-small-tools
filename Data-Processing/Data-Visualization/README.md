# Data Visualization Tool
A professional data visualization tool that generates high-quality charts (bar/line/pie/histogram/scatter) from Excel/CSV data files with automatic styling and cross-platform compatibility. Designed for data analysts and Python visualization practice.

## 📋 Features
- **Multiple Chart Types**:
  - Bar Chart (categorical comparison)
  - Line Chart (trend analysis)
  - Pie Chart (proportion distribution)
  - Histogram (numeric distribution)
  - Scatter Plot (correlation analysis)
- **Data Source Support**:
  - Excel (.xlsx/.xls) files (first sheet)
  - CSV files (auto-detect encoding: UTF-8/GBK/GB2312/Latin-1)
- **Professional Styling**:
  - Seaborn whitegrid style with custom color palette
  - Optimal figure size (12x8) and high DPI (300) output
  - Automatic label rotation and tight layout
  - Chinese character support (cross-platform)
- **Smart Features**:
  - Numeric/categorical column filtering
  - Small slice filtering for pie charts (<5% → "Other")
  - Correlation coefficient for scatter plots
  - Timestamped filenames (avoid overwriting)
- **User-Friendly**:
  - Interactive column selection
  - Real-time progress feedback
  - Comprehensive error handling
  - Cross-platform compatibility (Windows/macOS/Linux)

## 🛠️ How to Run
### 1. Install Dependencies
```bash
# Install required libraries
pip install pandas matplotlib seaborn openpyxl numpy xlrd
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd Data-Processing/Data-Visualization

# Run visualization tool
python data_visualization.py
```

### 3. Follow the Prompts
1. Enter Excel/CSV data file path
2. Select chart type (bar/line/pie/hist/scatter)
3. Select X column (and Y column if needed)
4. View generated chart in `data_visualization_charts/` directory

## 📸 Running Example
```
===== Python Data Visualization Tool v1.0 =====
Generate professional charts from Excel/CSV data files

Enter Excel/CSV data file path: ./sales_data.csv
✅ Successfully loaded data: ./sales_data.csv
   - Rows: 500, Columns: 6
   - Columns: date, region, product, sales, profit, quantity

📁 Chart output directory: /Users/yourname/python-small-tools/Data-Processing/Data-Visualization/data_visualization_charts

Available chart types:
1. Bar Chart (categorical data comparison)
2. Line Chart (trend over time)
3. Pie Chart (proportion distribution)
4. Histogram (numeric data distribution)
5. Scatter Plot (correlation analysis)

Select chart type (1-5): 1

=== Column Selection ===
Available all columns:
1. date
2. region
3. product
4. sales
5. profit
6. quantity

Select all column (1-6): 2

Use Y column for values? (Y/N, default: N): Y

Available all columns:
1. date
2. region
3. product
4. sales
5. profit
6. quantity

Select all column (1-6): 4

🚀 Generating chart...
✅ Chart saved: data_visualization_charts/bar_chart_region_20260226_164530.png

🎉 Chart generation completed successfully!
📂 Chart saved to: /Users/yourname/python-small-tools/Data-Processing/Data-Visualization/data_visualization_charts

👋 Thank you for using Data Visualization Tool!
```

## 📝 Development Details
- Uses `matplotlib` and `seaborn` for professional visualization (industry standards)
- Cross-platform Chinese character support (fixes common display issues)
- Smart data validation (numeric/categorical column filtering)
- High-quality output (300 DPI) with optimized styling
- Error handling for common visualization issues (non-numeric columns, empty data)
- Modular design (separate functions for load/chart generation/saving)
- Automatic layout adjustment (prevents label cutoff)

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Libraries:
  ```bash
  pip install pandas matplotlib seaborn openpyxl numpy xlrd
  ```

## ⚠️ Important Notes
- Scatter/histogram charts require numeric columns (tool auto-filters non-numeric)
- Pie charts work best with categorical columns (limited categories recommended)
- Line charts show best results with time/numeric X columns (auto-sorted)
- Large datasets (>10,000 rows) may take longer to process (reduce data size if needed)
- Generated charts are saved as high-resolution PNG files (300 DPI)
