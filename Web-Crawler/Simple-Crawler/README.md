# Simple Web Crawler
A lightweight, responsible web crawler that extracts key information from webpages (title, paragraphs, links) with complete error handling and data persistence. Designed for learning web scraping and HTTP request handling in Python.

## 📋 Features
- URL validation (check for http:///https:// prefix)
- HTTP request with browser-like headers (User-Agent)
- Complete error handling:
  - Timeout errors
  - HTTP errors (4xx/5xx)
  - Network errors
- Respectful crawling (1-second delay between requests)
- Key information extraction:
  - Page title
  - Paragraph text (filtered for meaningful content)
  - Valid links (relative → absolute conversion)
- Chinese character encoding support
- Results saved to text files (organized in `crawler_results` directory)
- Interactive loop execution (crawl multiple URLs or quit)

## 🛠️ How to Run
### 1. Install Dependencies
This tool requires `requests` and `beautifulsoup4` (external libraries):
```bash
pip install requests beautifulsoup4
```

### 2. Run the Script
```bash
# Navigate to tool directory
cd Web-Crawler/Simple-Crawler

# Run crawler
python simple_crawler.py
```

### 3. Usage Steps
1. Enter a valid URL (with http:///https://) when prompted
2. The crawler will extract page info and save results to `crawler_results/`
3. Enter 'q' to quit the program

## 📸 Running Example
```
===== Python Simple Web Crawler v1.0 =====
This tool crawls a webpage and extracts key information (title, text, links)
Note: Please use this tool responsibly and respect website robots.txt

Enter the URL to crawl (or 'q' to quit): https://example.com

🔍 Crawling https://example.com...

📊 Extracted Info:
Title: Example Domain
Paragraphs: 2
Links: 1

✅ Results saved to: crawler_results/example.com.txt

Enter the URL to crawl (or 'q' to quit): q

👋 Thank you for using Simple Web Crawler!
```

## 📝 Development Details
- Uses `requests` library for HTTP requests (with custom headers)
- Uses `BeautifulSoup4` for HTML parsing (html.parser)
- Implements rate limiting (1-second delay) to follow web etiquette
- Handles character encoding issues (apparent_encoding)
- Converts relative links to absolute links for usability
- Saves results to structured text files (organized directory)
- Strict error handling to prevent program crashes

## 📌 Dependencies
- Python Version: 3.8+ (recommended)
- External Libraries:
  ```bash
  pip install requests beautifulsoup4
  ```

## ⚠️ Important Notes
- Use this crawler responsibly and respect the target website's `robots.txt`
- Do not crawl websites excessively (the 1-second delay helps prevent this)
- Some websites may block crawlers (this tool uses browser headers to reduce blocking)
