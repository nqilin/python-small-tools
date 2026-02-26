import requests
from bs4 import BeautifulSoup
import os
import time
import random

# Configure request headers to simulate browser access
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://bing.com"  # Required for some image websites
}

# Target wallpaper URL (Bing daily wallpaper - stable and legal)
BING_WALLPAPER_URL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-US"

def create_download_directory():
    """Create wallpaper download directory if not exists"""
    download_dir = "downloaded_wallpapers"
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    return download_dir

def fetch_wallpaper_list():
    """Fetch Bing daily wallpaper list with API"""
    try:
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(1, 2))
        response = requests.get(BING_WALLPAPER_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract wallpaper info (url, title, copyright)
        wallpapers = []
        for item in data.get("images", []):
            # Convert relative URL to absolute URL
            wallpaper_url = "https://www.bing.com" + item.get("url", "")
            wallpaper_title = item.get("title", "unknown_wallpaper")
            wallpaper_copyright = item.get("copyright", "")
            
            wallpapers.append({
                "url": wallpaper_url,
                "title": wallpaper_title,
                "copyright": wallpaper_copyright
            })
        
        return wallpapers
    
    except requests.exceptions.Timeout:
        print("❌ Request timed out! Please check your network.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.JSONDecodeError:
        print("❌ Failed to parse JSON response!")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def download_wallpaper(wallpaper_info, download_dir):
    """Download single wallpaper with error handling"""
    try:
        # Get wallpaper URL and title
        wallpaper_url = wallpaper_info["url"]
        wallpaper_title = wallpaper_info["title"]
        
        # Create safe filename (remove special characters)
        safe_title = "".join(c for c in wallpaper_title if c.isalnum() or c in (" ", "_")).strip()
        filename = f"{safe_title}_{int(time.time())}.jpg"
        file_path = os.path.join(download_dir, filename)
        
        # Download wallpaper (stream mode for large files)
        response = requests.get(wallpaper_url, headers=HEADERS, timeout=15, stream=True)
        response.raise_for_status()
        
        # Save binary content to file
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"✅ Downloaded: {filename}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to download {wallpaper_info['title']}: {e}")
        return False
    except Exception as e:
        print(f"❌ Error saving {wallpaper_info['title']}: {e}")
        return False

def main():
    """Main function: run wallpaper crawler"""
    print("===== Python Wallpaper Crawler v1.0 =====")
    print("Downloads Bing daily wallpapers (8 latest wallpapers)")
    print("Note: For personal use only - respect copyright laws\n")
    
    # Create download directory
    download_dir = create_download_directory()
    print(f"📁 Download directory: {os.path.abspath(download_dir)}\n")
    
    # Fetch wallpaper list
    print("🔍 Fetching latest Bing wallpapers...")
    wallpapers = fetch_wallpaper_list()
    
    if not wallpapers:
        print("❌ No wallpapers found!")
        return
    
    print(f"✅ Found {len(wallpapers)} wallpapers\n")
    
    # Download all wallpapers
    print("📥 Starting download...")
    success_count = 0
    for wallpaper in wallpapers:
        if download_wallpaper(wallpaper, download_dir):
            success_count += 1
        # Add delay between downloads
        time.sleep(random.uniform(0.5, 1.5))
    
    # Summary
    print(f"\n🎉 Download completed!")
    print(f"✅ Success: {success_count}/{len(wallpapers)}")
    print(f"📂 All wallpapers saved to: {os.path.abspath(download_dir)}")
    print("\n👋 Thank you for using Wallpaper Crawler!")

if __name__ == "__main__":
    main()
