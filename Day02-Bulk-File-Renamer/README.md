# Day 2 - Bulk File Renamer

## 📌 Project Overview

This is Day 2 of my **August AI Automation Roadmap**.

The Bulk File Renamer is a Python automation tool that renames multiple files in a folder automatically using a custom prefix and sequential numbering.

Example:

Before:

cat.jpg
dog.png
bird.jpg

After:

Vacation_001.jpg
Vacation_002.png
Vacation_003.jpg

## 🚀 Features

- Rename multiple files automatically
- Preserve the original file extension
- Add a custom prefix
- Sequential numbering with leading zeros (001, 002, 003...)
- Rename only selected file types (e.g., images)

## 🛠️ Technologies Used

- Python
- pathlib

## 📂 Project Structure

Day02-Bulk-File-Renamer/
├── main.py
├── README.md
└── test_folder/

## ▶️ How to Run

1. Clone the repository.
2. Navigate to the project folder.
3. Place your test files inside `test_folder`.
4. Run:

```bash
python main.py
```

## 📚 What I Learned

- Working with `pathlib`
- Renaming files using Python
- Using `enumerate()`
- String formatting with leading zeros
- Filtering files by extension
- Building a real-world automation script

## 🎯 Future Improvements

- Allow users to choose the prefix from the terminal
- Add a graphical user interface (GUI)
- Support renaming different file types
- Preview changes before renaming
- Add an undo feature

---
**Author:** Etchie Glory  
**Roadmap:** August AI Automation Roadmap (Day 2)