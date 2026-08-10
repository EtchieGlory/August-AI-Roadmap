# 🌐 Day 7 - Web Scraper

A command-line Web Scraper built with Python, **requests**, and **BeautifulSoup** as part of my **August AI Automation Roadmap**.

This application collects quotes, authors, and tags from a practice website and saves the scraped data into a CSV file.

---

## 🚀 Features

- 🌐 Fetch data from a website
- 🔍 Parse HTML using BeautifulSoup
- 💬 Extract quotes
- 👤 Extract authors
- 🏷️ Extract tags
- 📊 Store scraped data in a structured format
- 💾 Save scraped data to a CSV file
- ⚠️ Handle connection and HTTP errors
- 📁 Automatically create the output directory

---

## 🛠️ Technologies Used

- Python 3
- requests
- BeautifulSoup4
- csv

---

## 📂 Project Structure

```text
Day07-Web-Scraper/
│
├── main.py
├── requirements.txt
├── README.md
│
└── output/
    └── quotes.csv
```

---
	
	
## 📦 Installation

Clone the repository:
```bash
git clone <https://github.com/EtchieGlory/August-AI-Roadmap>
```
Navigate into the project:
```bash
cd Day07-Web-Scraper
```

Install the required packages:
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

You'll see:
```text
==============================
       QUOTE SCRAPER
==============================
```

The program connects to the practice website, extracts the available quotes, authors, and tags, and saves the results automatically.

---

## 📌 Example
Scraping Data
The scraper collects information such as:

```text
Quote: “The world as we have created it is a process of our thinking...”
Author: Albert Einstein
Tags: change, deep-thoughts, thinking
```

The extracted information is saved as:

```text
output/quotes.csv
```

The CSV file contains:
quote,author,tags

---

## 📚 What I Learned

This project helped me learn:
- HTTP requests
- requests.get()
- HTTP status codes
- raise_for_status()
- HTML parsing
- BeautifulSoup
- find()
- find_all()
- HTML classes
- Extracting text from HTML
- Lists
- Dictionaries
- List comprehensions
- CSV files
- csv.DictWriter
- Exception handling
- Creating directories with os.makedirs()

---

## 🔮 Future Improvements

- Scrape multiple pages automatically
- Add user-provided URLs
- Add a command-line menu
- Scrape different types of websites
- Export data to Excel
- Add filtering and searching
- Add scheduled scraping
- Store scraped data in a database
- Build a graphical user interface (GUI)
- Add AI-powered data analysis

---

## 📅 August AI Automation Roadmap

- ✅ Day 1 – Smart File Organizer
- ✅ Day 2 – Bulk File Renamer
- ✅ Day 3 – PDF Toolkit
- ✅ Day 4 – Image Processing Toolkit
- ✅ Day 5 – Excel Grade Automation
- ✅ Day 6 – Email Automation Tool
- ✅ Day 7 – Web Scraper
- ⏳ Day 8 – Coming Next

---

## 👨‍💻 Author

**Etchie Glory Edonyabo**
Petroleum Engineering graduate transitioning into AI, Python, Automation, and Data Analytics.
Building one practical Python project every day throughout the **August AI Automation Roadmap**.