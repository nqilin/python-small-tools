import requests
from bs4 import BeautifulSoup
import os
import time

# Configure request headers to simulate browser access
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def validate_url(url):
    """Validate if the input URL is valid (basic check)"""
    if not url.startswith(("http://", "https://")):
        print("❌ Invalid URL! Please include http:// or https://")
        return False
    return True

def fetch_webpage(url):
    """Fetch webpage content with error handling"""
    try:
        # Add delay to avoid overwhelming the server
        time.sleep(1)
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors (4xx/5xx)
        response.encoding = response.apparent_encoding  # Handle Chinese characters
        return response.text
    except requests.exceptions.Timeout:
        print("❌ Request timed out! Please check the URL or network.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return None

def extract_page_info(html_content, url):
    """Extract key information from webpage (title, paragraphs, links)"""
    if not html_content:
        return None
    
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Extract page title
    title = soup.title.string if soup.title else "No Title"
    
    # Extract all paragraph text (cleaned)
    paragraphs = []
    for p in soup.find_all("p"):
        p_text = p.get_text(strip=True)
        if p_text and len(p_text) > 10:  # Filter short/empty paragraphs
            paragraphs.append(p_text)
    
    # Extract all valid links
    links = []
    for a in soup.find_all("a", href=True):
        link = a["href"]
        # Convert relative links to absolute links
        if link.startswith("/"):
            link = url + link if url.endswith("/") else url + "/" + link
        if link not in links and link.startswith(("http://", "https://")):
            links.append(link)
    
    return {
        "url": url,
        "title": title,
        "paragraph_count": len(paragraphs),
        "link_count": len(links),
        "paragraphs": paragraphs[:5],  # Only return first 5 paragraphs to avoid clutter
        "links": links[:10]  # Only return first 10 links
    }

def save_results(page_info, output_dir="crawler_results"):
    """Save crawled results to a text file"""
    if not page_info:
        return False
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Generate safe filename from URL
    safe_filename = page_info["url"].replace("https://", "").replace("http://", "").replace("/", "_").replace("?", "_") + ".txt"
    file_path = os.path.join(output_dir, safe_filename[:50] + ".txt")  # Limit filename length
    
    # Write results to file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"=== Web Crawler Results for: {page_info['url']} ===\n")
        f.write(f"Page Title: {page_info['title']}\n")
        f.write(f"Total Paragraphs: {page_info['paragraph_count']}\n")
        f.write(f"Total Links: {page_info['link_count']}\n\n")
        
        f.write("=== First 5 Paragraphs ===\n")
        for i, para in enumerate(page_info["paragraphs"], 1):
            f.write(f"{i}. {para}\n\n")
        
        f.write("=== First 10 Links ===\n")
        for i, link in enumerate(page_info["links"], 1):
            f.write(f"{i}. {link}\n")
    
    print(f"✅ Results saved to: {file_path}")
    return True

def main():
    """Main function: run simple web crawler"""
    print("===== Python Simple Web Crawler v1.0 =====")
    print("This tool crawls a webpage and extracts key information (title, text, links)")
    print("Note: Please use this tool responsibly and respect website robots.txt\n")
    
    # Get and validate URL from user
    while True:
        url = input("Enter the URL to crawl (or 'q' to quit): ").strip()
        if url.lower() == "q":
            print("\n👋 Thank you for using Simple Web Crawler!")
            break
        
        if validate_url(url):
            # Crawl webpage
            print(f"\n🔍 Crawling {url}...")
            html_content = fetch_webpage(url)
            
            # Extract and save info
            if html_content:
                page_info = extract_page_info(html_content, url)
                if page_info:
                    print(f"\n📊 Extracted Info:")
                    print(f"Title: {page_info['title']}")
                    print(f"Paragraphs: {page_info['paragraph_count']}")
                    print(f"Links: {page_info['link_count']}")
                    save_results(page_info)
            print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
