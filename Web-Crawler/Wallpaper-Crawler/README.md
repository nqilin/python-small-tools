# Wallpaper Crawler
A lightweight, legal wallpaper crawler that downloads the latest Bing daily wallpapers (8 images) with complete error handling and batch download support. Designed for learning binary file processing and API-based web crawling in Python.

## 📋 Features
- Fetches latest 8 Bing daily wallpapers via official API (stable & legal)
- Creates dedicated download directory (`downloaded_wallpapers/`)
- Safe filename generation (remove special characters)
- Batch download with random delay (avoid rate limiting)
- Stream mode download (supports large image files)
- Complete error handling (timeout, HTTP errors, file saving errors)
- Download summary (success/failure count)
- Copyright reminder (for personal use only)

## 🛠️ How to Run
### 1. Install Dependencies
This tool requires `requests` (same as Simple-Crawler):
```bash
pip install requests
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd Web-Crawler/Wallpaper-Crawler

# Run crawler
python wallpaper_crawler.py
```

### 3. Check Results
- All downloaded wallpapers are saved to `downloaded_wallpapers/` directory
- Filenames are generated from wallpaper titles (safe characters only)

## 📸 Running Example
```
===== Python Wallpaper Crawler v1.0 =====
Downloads Bing daily wallpapers (8 latest wallpapers)
Note: For personal use only - respect copyright laws

📁 Download directory: /Users/yourname/python-small-tools/Web-Crawler/Wallpaper-Crawler/downloaded_wallpapers

🔍 Fetching latest Bing wallpapers...
✅ Found 8 wallpapers

📥 Starting download...
✅ Downloaded: Winter_in_the_Bavarian_Alps_1739987654.jpg
✅ Downloaded: Red_squirrel_in_snow_1739987656.jpg
✅ Downloaded: Northern_lights_over_Iceland_1739987658.jpg
...

🎉 Download completed!
✅ Success: 8/8
📂 All wallpapers saved to: /Users/yourname/python-small-tools/Web-Crawler/Wallpaper-Crawler/downloaded_wallpapers

👋 Thank you for using Wallpaper Crawler!
```

## 📝 Development Details
- Uses Bing's official API (HPImageArchive) for legal wallpaper fetching
- Stream mode download to handle large image files efficiently
- Random delay between requests to follow web etiquette
- Safe filename generation (avoids special characters/OS issues)
- Binary file handling (wb mode for image saving)
- Cross-platform compatible (Windows/macOS/Linux)
- Follows modular design principles (single responsibility per function)

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Library:
  ```bash
  pip install requests
  ```

## ⚠️ Important Notes
- This tool is for **personal use only** - respect Bing's wallpaper copyright
- The crawler uses Bing's official API (not web scraping) to ensure stability
- Do not modify the delay settings to avoid overwhelming the server
- All downloaded wallpapers are property of their respective copyright holders
