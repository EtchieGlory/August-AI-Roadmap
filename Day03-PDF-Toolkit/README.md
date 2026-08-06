# 📄 Day 3 - PDF Toolkit

A command-line PDF Toolkit built with Python and **pypdf** as part of my **August AI Automation Roadmap**.

This application allows users to perform common PDF operations through an interactive menu.

---

## 🚀 Features

- 📖 Count the number of pages in a PDF
- 📝 Extract text from every page
- 📎 Merge multiple PDFs into one file
- ✂️ Split a PDF into individual pages
- 📋 Interactive command-line menu
- ⚠️ Basic error handling for missing files
- 📁 Automatically saves output files

---

## 🛠️ Technologies Used

- Python 3
- pypdf

---

## 📂 Project Structure

```text
Day03-PDF-Toolkit/
│
├── main.py
├── requirements.txt
├── README.md
├── pdfs/
│   ├── sample.pdf
│   ├── sample1.pdf
│   └── sample2.pdf
│
└── output/
```

---

## 📦 Installation

Clone the repository:

```bash
git clone <https://github.com/EtchieGlory/August-AI-Roadmap>
```

Navigate into the project:

```bash
cd Day03-PDF-Toolkit
```

Install the required package:

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
============================== PDF TOOLKIT ==============================

1. Count Pages
2. Extract Text
3. Merge PDFs
4. Split PDF
5. Exit
```

Simply choose an option and follow the prompts.

---

## 📌 Example

### Count Pages

Input:

```text
sample.pdf
```

Output:

```text
Number of pages: 15
```

---

### Merge PDFs

Input:

```text
sample1.pdf
sample2.pdf
```

Output:

```text
merged.pdf
```

Saved in:

```text
output/
```

---

### Split PDF

Input:

```text
sample.pdf
```

Output:

```text
sample_1.pdf
sample_2.pdf
sample_3.pdf
...
```

Saved in:

```text
output/
```

---

## 📚 What I Learned

This project helped me learn:

- Functions
- Menu-driven applications
- Loops
- Exception handling (`try` / `except`)
- Working with external Python libraries
- Reading and writing PDF files
- User input validation
- Code organization and reusable functions

---

## 🔮 Future Improvements

- Merge every PDF inside a folder automatically
- Password-protected PDF support
- Rotate PDF pages
- Delete selected pages
- Extract images from PDFs
- Encrypt and decrypt PDFs
- Add a graphical user interface (GUI)
- Package as a desktop application

---

## 📅 August AI Automation Roadmap

- ✅ Day 1 – Smart File Organizer
- ✅ Day 2 – Bulk File Renamer
- ✅ Day 3 – PDF Toolkit
- ⏳ Day 4 – Image Processing Toolkit

---

## 👨‍💻 Author

**Etchie Glory Edonyabo**

Petroleum Engineering graduate transitioning into AI, Python, Automation, and Data Analytics.

Building one practical Python project every day throughout the **August AI Automation Roadmap**.