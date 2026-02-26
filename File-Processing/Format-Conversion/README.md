# Format Conversion Tool
A versatile, batch-supported file format conversion tool that handles text and image files with encoding detection and complete error handling. Designed for daily file processing and Python multi-format file handling practice.

## 📋 Features
- **Text Conversion**:
  - TXT → Markdown (with basic formatting)
  - CSV → TXT (custom delimiter support)
- **Image Conversion**:
  - JPG → PNG (lossless conversion)
  - PNG → JPG (RGBA to RGB handling)
- **Batch Processing**: Support single file or directory batch conversion
- **Encoding Detection**: Auto-detect file encoding (supports Chinese/English files)
- **Error Handling**: Comprehensive error catching for file operations
- **Output Organization**: All converted files saved to `converted_files/` directory
- **Cross-Platform**: Compatible with Windows/macOS/Linux

## 🛠️ How to Run
### 1. Install Dependencies
```bash
# Install required libraries
pip install pillow chardet
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd File-Processing/Format-Conversion

# Run conversion tool
python format_conversion.py
```

### 3. Follow the Prompts
1. Select conversion type (1-4)
2. Enter input file path or directory path
3. Check converted files in `converted_files/` directory

## 📸 Running Example
```
===== Python File Format Conversion Tool v1.0 =====
Supported conversions:
1. Text file to Markdown (txt_to_md)
2. CSV file to Text (csv_to_txt)
3. JPG image to PNG (jpg_to_png)
4. PNG image to JPG (png_to_jpg)

Enter conversion type (1-4): 1

Enter input file/directory path: ./test.txt
✅ Converted: ./test.txt → converted_files/test.md

🎉 Conversion completed!
✅ Success: 1/1
📂 All converted files saved to: /Users/yourname/python-small-tools/File-Processing/Format-Conversion/converted_files

👋 Thank you for using Format Conversion Tool!
```

## 📝 Development Details
- Uses `chardet` for automatic file encoding detection (supports multi-language files)
- Uses `Pillow (PIL)` for image processing (handles transparency for JPG conversion)
- Uses `csv` module for CSV file parsing (standard library)
- Batch processing support (single file or entire directory)
- Encoding compatibility (UTF-8, GBK, GB2312, etc.)
- Modular design (separate functions for different conversion types)
- Comprehensive error handling for file operations

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Libraries:
  ```bash
  pip install pillow chardet
  ```

## ⚠️ Important Notes
- For PNG → JPG conversion: PNG transparency will be lost (converted to white background)
- Large image files may take longer to convert (depends on file size)
- Ensure input files are not open in other programs (may cause write errors)
- Encoding detection works best for files larger than 10KB (more accurate results)
