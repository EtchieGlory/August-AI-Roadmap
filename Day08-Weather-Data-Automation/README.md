# 🌤️ Day 8 - Weather API Tool

A command-line Weather API Tool built with Python and **requests** as part of my **August AI Automation Roadmap**.

This application uses the Open-Meteo API to find a city's location and retrieve its current weather information.

---

## 🚀 Features

- 🌍 Search for a city by name
- 📍 Retrieve latitude and longitude using a geocoding API
- 🌡️ Get current temperature
- 🌤️ Get current weather condition
- 🔌 Work with external APIs
- 📦 Process JSON responses
- ⚠️ Handle API and connection errors
- 🧩 Use reusable Python functions

---

## 🛠️ Technologies Used

- Python 3
- requests
- Open-Meteo API

---

## 📂 Project Structure

```text
Day08-Weather-API/
│
├── main.py
├── requirements.txt
└── README.md
```

## 📦 Installation
Clone the repository:
```bash
git clone <https://github.com/EtchieGlory/August-AI-Roadmap>
```

Navigate into the project:
```bash
cd Day08-Weather-API
```

Install the required package:
```bash
pip install -r requirements.txt
```

---


## ▶️ Usage
Run the application:
python main.py
You'll see:

```text
==============================
       WEATHER TOOL
==============================
Enter city:
```

Enter a city name, for example:
Lagos
The application will retrieve the city's coordinates and current weather information.

---

## 📌 Example
Input
Enter city: Lagos
Output
```text
📍 City: Lagos
🌡️ Temperature: 27.4°C
🌤️ Condition: Partly cloudy
```

---

## 🔄 How It Works

**The application uses two API requests**:
```text
User enters city
       ↓
Geocoding API
       ↓
Latitude + Longitude
       ↓
Weather API
       ↓
JSON response
       ↓
Extract temperature + weather code
       ↓
Display weather information
```

---

## 📚 What I Learned

**This project helped me learn**:

- What APIs are
- Making HTTP requests with requests
- GET requests
- Query parameters
- HTTP status codes
- raise_for_status()
- JSON data
- response.json()
- Nested dictionaries
- Lists and indexing
- Tuple unpacking
- Dictionary .get()
- API error handling
- Working with multiple APIs
- Creating reusable functions

---

## 🔮 Future Improvements

- 🌍 Add more detailed weather information
- 📅 Add weather forecasts
- 🌧️ Display precipitation probability
- 💨 Display wind speed
- 📊 Save weather data to CSV
- 📈 Track weather history
- 🔔 Add weather alerts
- 🖥️ Build a graphical user interface (GUI)
- 🤖 Add AI-powered weather summaries
- 📱 Turn it into a mobile or web application

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
- ⏳ Day 9 – Coming Next

---

## 👨‍💻 Author
**Etchie Glory Edonyabo**
Petroleum Engineering graduate transitioning into AI, Python, Automation, and Data Analytics.
Building one practical Python project every day throughout the **August AI Automation Roadmap**.