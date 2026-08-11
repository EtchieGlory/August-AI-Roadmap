# 📦 Day 9 - File Backup Automation

A command-line File Backup Tool built with Python as part of my **August AI Automation Roadmap**.

This application automatically copies files from a user-selected source folder into a backup folder.

---

## 🚀 Features

- 📁 Select a source folder
- 🔍 Find files inside the folder
- 📋 Ignore directories and process only files
- 💾 Automatically copy files to a backup folder
- 🗂️ Automatically create the backup folder if it doesn't exist
- 📊 Count the number of files backed up
- ⚠️ Basic error handling for missing folders
- 🔄 Reusable backup function

---

## 🛠️ Technologies Used

- Python 3
- `os`
- `shutil`

---

## 📂 Project Structure

```text
Day09-File-Backup/
│
├── main.py
├── README.md
│
├── documents/
│   ├── report.pdf
│   ├── notes.txt
│   └── image.jpg
│
└── backup/
```

---

## 📦 Installation
Clone the repository:
```bash
git clone <https://github.com/EtchieGlory/August-AI-Roadmap>
```

Navigate into the project:
```bash
cd Day09-File-Backup
```
No external packages are required because the project uses Python's built-in os and shutil modules.

---

## ▶️ Usage
Run the application:
```bash
python main.py
```

The program will ask for the source folder:
```bash
Enter source folder: documents
```
The files inside the folder will then be copied into:
```bash
backup/
```
---

## 📌 Example
Source Folder
documents/
├── report.pdf
├── notes.txt
├── image.jpg
└── projects/
The program processes only the files:
report.pdf
notes.txt
image.jpg
The projects/ directory is ignored.
Output
Enter source folder: documents
```text
✅ report.pdf backed up successfully!
✅ notes.txt backed up successfully!
✅ image.jpg backed up successfully!
```

```text
✅ 3 file(s) backed up successfully!
```
The copied files are saved in:
backup/

---

## 🔄 How It Works
User selects source folder
        ↓
os.listdir()
        ↓
Check each item
        ↓
os.path.isfile()
        ↓
Build source and destination paths
        ↓
shutil.copy2()
        ↓
Backup folder

---

## 📚 What I Learned
This project helped me learn:
- File and folder automation
- os.listdir()
- os.path.join()
- os.path.isfile()
- os.makedirs()
- shutil.copy2()
- Loops
- Functions
- User input
- Counters
- Exception handling
- Working with file paths
- Automating repetitive file operations

---

## 🔮 Future Improvements
- 🔄 Automatically back up subfolders
- 🕒 Schedule automatic backups
- 📅 Create date-based backup folders
- 🔍 Back up only modified files
- 🗜️ Compress backups into ZIP files
- 🗑️ Remove old backups automatically
- 📊 Generate backup reports
- 🔐 Add encrypted backups
- ☁️ Upload backups to cloud storage
- 🖥️ Build a graphical user interface (GUI)

---

## 📅 August AI Automation Roadmap
- ✅ Day 1 – Smart File Organizer
- ✅ Day 2 – Bulk File Renamer
- ✅ Day 3 – PDF Toolkit
- ✅ Day 4 – Image Processing Toolkit
- ✅ Day 5 – Excel Grade Automation
- ✅ Day 6 – Email Automation Tool
- ✅ Day 7 – Web Scraper
- ✅ Day 8 – Weather API Tool
- ✅ Day 9 – File Backup Automation
- ⏳ Day 10 – Coming Next

---

## 👨‍💻 Author
**Etchie Glory Edonyabo**
Petroleum Engineering graduate transitioning into AI, Python, Automation, and Data Analytics.
Building one practical Python project every day throughout the **August AI Automation Roadmap**.