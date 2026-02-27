# Book List Crawler
A structured data crawler that extracts top book information from Project Gutenberg (legal public domain books) with pagination support, detailed metadata extraction, and CSV export. Designed for learning structured web scraping and data formatting in Python.

## 📋 Features
- **Legal Data Source**: Crawls public domain books from Project Gutenberg (no copyright issues)
- **Structured Data Extraction**:
  - Book rank, title, and URL (top 100 books)
  - Author name, language, and release date (detailed book page)
- **Rate Limiting**: Random delays between requests (respectful crawling)
- **CSV Export**: Structured output with timestamped filenames
- **Complete Error Handling**: Timeout, HTTP errors, and missing data handling
- **Progress Tracking**: Real-time progress updates for book detail fetching
- **Data Validation**: Default values for missing information (no broken CSV)
- **Cross-Platform**: Compatible with Windows/macOS/Linux

## 🛠️ How to Run
### 1. Install Dependencies
```bash
# Install required libraries
pip install requests beautifulsoup4
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd Web-Crawler/Book-List-Crawler

# Run crawler
python book_list_crawler.py
```

### 3. Check Results
- All crawled book data is saved to `book_crawler_results/` directory
- CSV files are named with timestamps (e.g., `top_books_20260226_103045.csv`)
- CSV contains columns: rank, title, author, language, release_date, url

## 📸 Running Example
```
===== Python Book List Crawler v1.0 =====
Crawls top books from Project Gutenberg (legal & free public domain books)
Extracts structured data: title, author, language, release date

📁 Output directory: /Users/yourname/python-small-tools/Web-Crawler/Book-List-Crawler/book_crawler_results

🔍 Fetching top book list from Project Gutenberg...
✅ Found 100 top books

📄 Fetching book details (this may take a few minutes)...
🔄 Processing book 1/100: The Adventures of Sherlock Holmes by Ar...
🔄 Processing book 2/100: Pride and Prejudice by Jane Austen...
🔄 Processing book 3/100: Alice's Adventures in Wonderland by Lewi...
...

💾 Saving book data to CSV...
✅ Book data saved to: book_crawler_results/top_books_20260226_103045.csv
📊 Total books saved: 100

🎉 Crawling completed successfully!
👋 Thank you for using Book List Crawler!
```

## 📝 Development Details
- Uses Project Gutenberg's public API (legal & stable data source)
- Two-level crawling: list page → detail page (structured data)
- Random delay implementation (1-2s between requests)
- CSV export with proper headers and encoding (UTF-8)
- Timestamped filenames to avoid overwriting existing files
- Graceful handling of missing data (default "Unknown" values)
- Progress tracking for long-running operations
- Modular design (separate functions for fetch/save/processing)

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Libraries:
  ```bash
  pip install requests beautifulsoup4
  ```

## ⚠️ Important Notes
- This tool crawls only public domain books (no copyright infringement)
- The crawler includes random delays to respect Project Gutenberg's servers
- Book detail fetching may take 2-3 minutes (100 books × 1s delay)
- Some books may have missing metadata (marked as "Unknown" in CSV)
- Do not modify delay settings to avoid being blocked by the server
