# File Filter Tool
A powerful, multi-condition file filtering tool that selects files by size, extension, and modified time, with support for listing, copying, or moving filtered files. Designed for daily file management and Python file system handling practice.

## 📋 Features
- **Multi-Condition Filtering**:
  - Size filter (minimum/maximum size in MB)
  - Extension filter (comma-separated, case-insensitive)
  - Time filter (files modified in last N days)
- **Flexible Actions**:
  - List files (with attributes: size/modified time)
  - Copy files to `filtered_files/` directory
  - Move files to `filtered_files/` directory
- **Recursive Scanning**: Scans all subdirectories automatically
- **Duplicate Handling**: Auto-rename duplicate filenames during copy/move
- **Detailed File Attributes**: Shows size (MB), creation/modification time, extension
- **Complete Error Handling**: Catches file access/permission errors
- **Human-Readable Output**: Clear progress and summary reports

## 🛠️ How to Run
### 1. Install Dependencies
- No external dependencies (only Python standard library)
- Python Version: 3.8+ (recommended)

### 2. Run the Script
```bash
# Navigate to tool directory
cd File-Processing/File-Filter

# Run filter tool
python file_filter.py
```

### 3. Follow the Prompts
1. Enter target directory path (to scan files)
2. Choose to filter by size (Y/N) → enter min/max size (MB)
3. Choose to filter by extension (Y/N) → enter comma-separated extensions
4. Choose to filter by modified time (Y/N) → enter number of days
5. Select action (list/copy/move)
6. View results and summary

## 📸 Running Example
```
===== Python File Filter Tool v1.0 =====
Filter files by size/extension/modified time and perform actions (list/copy/move)

Enter target directory path: ./test_files

🔍 Scanning directory: ./test_files
✅ Found 25 total files

Filter by file size? (Y/N): Y
Minimum size (MB, enter 0 for no limit): 0.5
Maximum size (MB, enter 0 for no limit): 10
✅ Filtered to 12 files (size: 0.5-10.0MB)

Filter by file extension? (Y/N): Y
Enter extensions (comma-separated, e.g., .txt,.jpg): .jpg,.png
✅ Filtered to 8 files (extensions: .jpg, .png)

Filter by modified time? (Y/N): Y
Files modified in last N days (enter number): 30
✅ Filtered to 5 files (modified in last 30 days)

Select action to perform on filtered files:
1. List files (default)
2. Copy files to filtered_files/
3. Move files to filtered_files/
Enter choice (1-3): 1

🚀 Processing files...

📋 Found 5 files matching criteria:
- sunset.jpg | Size: 2.4MB | Modified: 2026-02-20 14:30:22
- mountain.png | Size: 4.8MB | Modified: 2026-02-18 09:15:45
- beach.jpg | Size: 1.2MB | Modified: 2026-02-10 16:45:11
- forest.png | Size: 3.5MB | Modified: 2026-02-05 11:20:33
- lake.jpg | Size: 0.8MB | Modified: 2026-02-01 08:50:17

🎉 Processing completed!
✅ Successfully processed: 5/5 files

👋 Thank you for using File Filter Tool!
```

## 📝 Development Details
- Uses Python standard library only (no external dependencies)
- Recursive directory scanning with `os.walk()`
- File attribute extraction with `os.stat()`
- Time handling with `datetime` and `timedelta`
- File operations with `shutil` (copy2/move for preserve metadata)
- Duplicate filename handling (auto-increment counter)
- Comprehensive input validation and error handling
- Cross-platform compatible (Windows/macOS/Linux)

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- No external dependencies (uses only Python standard library)

## ⚠️ Important Notes
- For move action: Ensure files are not open in other programs (may cause errors)
- Permission required: Ensure you have read/write access to target directory
- Recursive scan: Tool scans all subdirectories (may take time for large directories)
- File size calculation: Based on actual file size (MB = 1024*1024 bytes)
- Time filter: Uses local system time (check time zone settings if needed)
