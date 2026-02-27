# Python-Small-Tools

A collection of practical, lightweight Python small tools for daily use and basic development practice. All tools are runnable, with simple UI prototype design (PS/AI integration) and focus on solving real-world small problems while improving Python development skills.

Key features:
- 🚀 All tools are independent of each other
- 📝 Clear running steps + detailed code comments
- 🛠️ Easy to use & support secondary development
- 🎨 UI prototype/visual design integration (PS/AI)

---

## 📁 Repository Structure
Classified by functional scenarios, each tool has an independent directory (including code files, README, and design files):

```
Python-Small-Tools/
├── File-Processing/
│   ├── Batch-Rename/ ✅ Completed
│   ├── Format-Conversion/ ✅ Completed
│   └── File-Filter/ ✅ Completed
├── Data-Processing/
│   ├── Excel-CSV-Handle/ ✅ Completed
│   ├── Excel-Cell-Extractor/ ✅ Completed
│   ├── Data-Visualization/ ✅ Completed
│   ├── Simple-Analysis/ ✅ Completed
│   └── List-Utils/ ✅ Completed
├── Web-Crawler/
│   ├── Simple-Crawler/ ✅ Completed
│   ├── Wallpaper-Crawler/ ✅ Completed
│   └── Book-List-Crawler/ ✅ Completed
└── Daily-Tools/
    ├── To-Do-List/ ✅ Completed
    ├── Simple-Calculator/ ✅ Completed
    └── Password-Generator/ ✅ Completed
```

---

## ✅ Finished Tools
All completed tools follow strict development standards (independent directory + full comments + detailed usage docs):

### [1. Simple-Calculator (Daily-Tools)](Daily-Tools/simple-calculator)
- Basic arithmetic operations (+-*/)
- V2.0: Loop run + manual exit
- Complete input validation & error handling

### [2. List-Utils (Data-Processing)](Data-Processing/list-utils)
- Numeric list duplicate removal
- Custom ascending/descending sort
- Comprehensive input validation

### [3. Batch-Rename (File-Processing)](File-Processing/Batch-Rename)
- Batch rename files in a directory
- Support custom prefix/suffix & numbering rules
- Preview mode before renaming

### [4. Excel-Cell-Extractor (Data-Processing)](Data-Processing/excel-cell-extractor)
- Extract specific cells/ranges from Excel files
- Support CSV/Excel output
- Handle multiple sheets

### [5. Password-Generator (Daily-Tools)](Daily-Tools/Password-Generator)
- Customizable password length (8-20 characters)
- Support character types: uppercase, lowercase, digits, special symbols
- Complete input validation & secure random generation
- Loop run + manual exit

### [6. To-Do-List (Daily-Tools)](Daily-Tools/To-Do-List)
- Task CRUD operations (add/view/complete/delete)
- Data persistence via file I/O (saved to todo_list.txt)
- Timestamp tracking for each task
- Interactive menu system with input validation

### [7. Simple-Crawler (Web-Crawler)](Web-Crawler/Simple-Crawler)
- HTTP requests with headers, timeout, and error handling
- HTML parsing with BeautifulSoup4 (title, paragraphs, links)
- Responsible crawling with 1-second delay
- Results saved to structured text files
- Chinese character encoding support

### [8. Wallpaper-Crawler (Web-Crawler)](Web-Crawler/Wallpaper-Crawler)
- Fetch latest Bing daily wallpapers via official API (legal & stable)
- Batch download with stream mode (supports large image files)
- Safe filename generation + dedicated download directory
- Random delay between requests to avoid rate limiting
- Complete error handling for network & file operations

### [9. Format-Conversion (File-Processing)](File-Processing/Format-Conversion)
- Support TXT→MD, CSV→TXT, JPG→PNG, PNG→JPG conversions
- Auto file encoding detection (supports multi-language files)
- Batch processing for single file or entire directory
- Image transparency handling (RGBA to RGB for JPG)
- Organized output directory + conversion summary report

### [10. File-Filter (File-Processing)](File-Processing/File-Filter)
- Multi-condition filtering: size, extension, modified time
- Recursive directory scanning with detailed file attributes
- Support list/copy/move actions (duplicate filename handling)
- No external dependencies (Python standard library only)
- Human-readable output with progress & success summary

### [11. Excel-CSV-Handle (Data-Processing)](Data-Processing/Excel-CSV-Handle)
- Batch processing for Excel/CSV files (recursive directory scan)
- Comprehensive data cleaning (duplicates/missing values/empty rows)
- Multi-encoding support for CSV (solve garbled text issue)
- Cross-format conversion (Excel ↔ CSV) + timestamped output

### [12. Simple-Analysis (Data-Processing)](Data-Processing/Simple-Analysis)
- Generate descriptive stats, correlation matrix, and categorical insights
- Missing value analysis (count + percentage) for all columns
- Comprehensive report generation (timestamped text files)
- Auto CSV encoding detection + cross-platform support

### [13. Book-List-Crawler (Web-Crawler)](Web-Crawler/Book-List-Crawler)
- Crawl public domain books from Project Gutenberg (legal data source)
- Two-level crawling (list → detail page) for structured data
- Extract author/language/release date + CSV export with timestamps
- Random delay + progress tracking + complete error handling

### [14. Data-Visualization (Data-Processing)](Data-Processing/Data-Visualization)
- Generate 5 chart types (bar/line/pie/histogram/scatter) from Excel/CSV
- Professional styling with seaborn + high DPI (300) output
- Cross-platform Chinese character support + smart column filtering
- Correlation coefficient for scatter plots + small slice filtering for pie charts
---

## 🎯 Development Objectives
- Master Python core skills (file I/O, network requests, data processing, etc.)
- Cultivate problem-solving ability with code for real small scenarios
- Integrate PS/AI design skills to complete tool visual design (UI prototype, interface display)
- Accumulate reusable code snippets and development experience for complex projects

---

## 🎨 UI/Visual Design (PS/AI Integration)
Combine coding & design to achieve "function + vision" dual presentation:
- Design simple UI prototypes for each tool with Illustrator (layout + interaction)
- Create high-definition running interface screenshots with Photoshop (typesetting + optimization)
- Store design files (AI/PNG) in corresponding tool directories (linked with code)
- Optimize tool output display for better usability

---

## 🔧 Development Environment & Dependencies
- Python Version: 3.8+ (recommended)
- Common Dependencies: requests, pandas, openpyxl, beautifulsoup4 (detailed in each tool's README)
- Design Tools: Photoshop, Illustrator (UI prototype & visual design)
- Running Environment: Windows/macOS/Linux (cross-platform compatible)

---

## 📝 Development Standards
- Single function per tool, clear logic (50-500 lines of code)
- Standard code comments (key logic + function explanation)
- Independent detailed README for each tool (running steps, environment, effect display)
- Include design files (UI prototype/screenshots) and running effect display

---

## 📈 Update Plan
- Current Progress: 2 lightweight tools completed (Simple-Calculator/List-Utils)
- Development Rhythm: 1 small function per day (1 tool module in 3-5 days)
- Documentation: Supplement design files & running docs during development
- Optimization: Regularly refine existing tool code/design (1 per week)

---

## 📌 For Job & Cooperation
These small tools demonstrate practical Python development ability and problem-solving thinking, with design skills integrated for more complete presentation.

Open to cooperation in:
- Lightweight Python tool development
- Visual design of small projects
