# 📧 Day 6 - Email Automation Tool

A command-line Email Automation Tool built with Python, **smtplib**, and **EmailMessage** as part of my **August AI Automation Roadmap**.

This application allows users to send personalized emails through an interactive command-line workflow using reusable email templates.

---

## 🚀 Features

- 📧 Send emails programmatically
- 🔐 Secure SMTP connection using TLS
- 🔑 Authenticate using environment variables
- 📝 Reusable email templates
- 👤 Personalize emails with recipient names
- 👥 Support multiple recipients
- 👀 Preview emails before sending
- ✅ Confirm before sending
- ⚠️ Basic error handling
- 🔒 Protect email credentials using `.env` and `.gitignore`

---

## 🛠️ Technologies Used

- Python 3
- smtplib
- EmailMessage
- python-dotenv
- Gmail SMTP

---

## 📂 Project Structure

```text
Day06-Email-Automation/
│
├── main.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
---

##📦 Installation
Clone the repository:

```bash
git clone <https://github.com/EtchieGlory/August-AI-Roadmap>
```
Navigate into the project:
```bash
cd Day06-Email-Automation
```

Install the required package:
```bash
pip install -r requirements.txt
```
---

##🔐 Environment Variables
Create a .env file inside the project folder:
```text
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

For Gmail, use an appropriate App Password rather than putting your normal account password in the program.
Never share or commit your .env file.

The .gitignore file contains:
```text
.env
__pycache__/
```

---

##▶️ Usage
###Run the application:
```bash
python main.py
```
You'll see:

```text============================== EMAIL TEMPLATES ==============================

1. Welcome
2. Follow-up
3. Thank You
```

Choose a template and follow the prompts.
The application will ask for:
Recipient name:
Enter recipient emails separated by commas:
It will then display an email preview before asking for confirmation.

---

##📌 Example

Welcome Email

Input:
Choose template: 1
Recipient name: Glory
Enter recipient emails separated by commas: example@gmail.com
Output:

```text
Subject: Welcome!

Hello Glory,

Welcome! We're glad to have you.

Best regards,
Your Name
```

The program then asks:
Send this email? (y/n):
If y is selected, the email is sent through the configured SMTP server.

Multiple Recipients
Input:
john@example.com, mary@example.com, peter@example.com
The program separates the addresses and sends the email to each recipient.

---

##📚 What I Learned

This project helped me learn:

-SMTP and email automation
-smtplib
-EmailMessage
-TLS encryption
-SMTP authentication
-Environment variables
-python-dotenv
-.gitignore
-Functions
-return
-Dictionaries
-.get()
-f-strings
-.format()
-List splitting
-List comprehensions
-Loops
-Exception handling
-Reusable email templates
-Basic application security

---

##🔮 Future Improvements

-Add HTML email support
-Add file attachments
-Add email logging
-Add scheduled emails
-Add a contact database
-Add more customizable templates
-Add email preview improvements
-Add AI-generated email content
-Add database integration
-Add a graphical user interface (GUI)
-Integrate with the future AI Business Assistant

---

##📅 August AI Automation Roadmap
-✅ Day 1 – Smart File Organizer
-✅ Day 2 – Bulk File Renamer
-✅ Day 3 – PDF Toolkit
-✅ Day 4 – Image Processing Toolkit
-✅ Day 5 – Excel Grade Automation
-✅ Day 6 – Email Automation Tool
-⏳ Day 7 – Coming Next

---

##👨‍💻 Author

**Etchie Glory Edonyabo**

Petroleum Engineering graduate transitioning into AI, Python, Automation, and Data Analytics.

Building one practical Python project every day throughout the **August AI Automation Roadmap**.