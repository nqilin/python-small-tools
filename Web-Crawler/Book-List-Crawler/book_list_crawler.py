import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import random

# Configure request headers to simulate browser access
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# Target URL (Book list from Project Gutenberg - legal & stable)
BASE_URL = "https://www.gutenberg.org/browse/scores/top"

def create_output_directory():
    """Create output directory for crawled book data"""
    output_dir = "book_crawler_results"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def fetch_book_list():
    """Fetch top book list from Project Gutenberg with pagination support"""
    try:
        # Add random delay to avoid rate limiting
        time.sleep(random.uniform(1, 2))
        
        # Fetch main page
        response = requests.get(BASE_URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract top books (today's top 100)
        book_list = []
        top_books_section = soup.find("div", {"class": "pgdbbyl-content"})
        
        if top_books_section:
            # Get today's top books list
            book_links = top_books_section.find_all("a", href=True)[:100]  # Limit to top 100
            
            for rank, link in enumerate(book_links, 1):
                # Extract book info
                book_title = link.get_text(strip=True)
                book_url = f"https://www.gutenberg.org{link['href']}"
                
                # Skip non-book links
                if "/ebooks/" not in book_url:
                    continue
                
                book_list.append({
                    "rank": rank,
                    "title": book_title,
                    "url": book_url,
                    "author": "Unknown"  # Will be filled in detail fetching
                })
        
        return book_list
    
    except requests.exceptions.Timeout:
        print("❌ Request timed out! Please check your network.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error fetching book list: {e}")
        return None

def fetch_book_details(book_url):
    """Fetch detailed book information (author, language, release date)"""
    try:
        # Add random delay
        time.sleep(random.uniform(0.5, 1.5))
        
        response = requests.get(book_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract author
        author_tag = soup.find("a", {"href": lambda x: x and "/authors/" in x})
        author = author_tag.get_text(strip=True) if author_tag else "Unknown"
        
        # Extract language
        language_tag = soup.find("th", string="Language")
        language = language_tag.find_next_sibling("td").get_text(strip=True) if language_tag else "Unknown"
        
        # Extract release date
        release_tag = soup.find("th", string="Release Date")
        release_date = release_tag.find_next_sibling("td").get_text(strip=True) if release_tag else "Unknown"
        
        return {
            "author": author,
            "language": language,
            "release_date": release_date
        }
    
    except Exception as e:
        print(f"❌ Failed to fetch details for {book_url}: {e}")
        return {
            "author": "Unknown",
            "language": "Unknown",
            "release_date": "Unknown"
        }

def save_books_to_csv(book_list, output_dir):
    """Save crawled book data to CSV file (structured format)"""
    # Generate filename with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    csv_filename = f"top_books_{timestamp}.csv"
    csv_path = os.path.join(output_dir, csv_filename)
    
    # Define CSV headers
    headers = ["rank", "title", "author", "language", "release_date", "url"]
    
    try:
        # Write to CSV file
        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()
            
            # Write each book's data
            for book in book_list:
                writer.writerow({
                    "rank": book["rank"],
                    "title": book["title"],
                    "author": book["author"],
                    "language": book["language"],
                    "release_date": book["release_date"],
                    "url": book["url"]
                })
        
        print(f"✅ Book data saved to: {csv_path}")
        print(f"📊 Total books saved: {len(book_list)}")
        return True
    
    except Exception as e:
        print(f"❌ Failed to save CSV file: {e}")
        return False

def main():
    """Main function: run book list crawler"""
    print("===== Python Book List Crawler v1.0 =====")
    print("Crawls top books from Project Gutenberg (legal & free public domain books)")
    print("Extracts structured data: title, author, language, release date\n")
    
    # Create output directory
    output_dir = create_output_directory()
    print(f"📁 Output directory: {os.path.abspath(output_dir)}\n")
    
    # Fetch top book list
    print("🔍 Fetching top book list from Project Gutenberg...")
    book_list = fetch_book_list()
    
    if not book_list:
        print("❌ No books found! Exiting...")
        return
    
    print(f"✅ Found {len(book_list)} top books\n")
    
    # Fetch detailed information for each book
    print("📄 Fetching book details (this may take a few minutes)...")
    for i, book in enumerate(book_list):
        print(f"🔄 Processing book {i+1}/{len(book_list)}: {book['title'][:50]}...")
        details = fetch_book_details(book["url"])
        book["author"] = details["author"]
        book["language"] = details["language"]
        book["release_date"] = details["release_date"]
    
    # Save to CSV
    print("\n💾 Saving book data to CSV...")
    save_books_to_csv(book_list, output_dir)
    
    print("\n🎉 Crawling completed successfully!")
    print("👋 Thank you for using Book List Crawler!")

if __name__ == "__main__":
    main()
