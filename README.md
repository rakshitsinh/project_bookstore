# 📚 Bookstore Inventory Management System with WhatsApp Bot

A hybrid application that combines a **desktop GUI (PyQt5)** with a **WhatsApp chatbot (Flask + Twilio API)** to manage and search bookstore inventory in real-time.

---

## 🚀 Features

- 📖 GUI-based bookstore management using PyQt5  
- 🔍 Fast book search (price, availability, details)  
- 📦 Inventory management using SQLite database  
- 🤖 WhatsApp chatbot integration for real-time book queries  
- 🌐 REST API built using Flask  
- 🔗 Webhook integration using Twilio API  
- 🚀 ngrok used for exposing local server  

---

## 🧠 How It Works

1. User sends a message on WhatsApp (book name)  
2. Message is received via Twilio webhook  
3. Flask backend processes the request  
4. SQLite database is queried  
5. Bot responds with:
   - Title  
   - Author  
   - Price  
   - Available Quantity  

---

## 🛠️ Tech Stack

- **Python**
- **PyQt5** (Desktop GUI)
- **Flask** (Backend API)
- **SQLite** (Database)
- **Twilio API** (WhatsApp integration)
- **ngrok** (Public URL tunneling)

---

## 📂 Project Structure
project_bookstore/
│── wp_bot.py # WhatsApp chatbot backend
│── assingment.py # PyQt5 GUI application
│── 
│── bookstore.db # SQLite database (ignored in Git)
│── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
bash
git clone https://github.com/your-username/project_bookstore.git
cd project_bookstore
### 2️⃣ Install dependencies
pip install flask twilio pyqt5
### 3️⃣ Run PyQt Application
python main.py
### 4️⃣ Run WhatsApp Bot
python wp_bot.py
### 5️⃣ Start ngrok
ngrok http 5000
### 6️⃣ Configure Twilio Webhook

Paste:

https://your-ngrok-url/whatsapp

in:

Twilio Sandbox → WHEN A MESSAGE COMES IN
💬 Example Usage

User (WhatsApp):

think python

Bot Response:

📚 Book Found!

Title: think python
Author: a dowrry
Price: ₹450
Stock: 20
⚠️ Notes
Ensure Flask server and ngrok are running simultaneously
Do not upload bookstore.db (add to .gitignore)
This project uses Twilio Sandbox for testing
🚀 Future Enhancements
🛒 Order books via WhatsApp
🔔 Stock notifications
🤖 AI-based recommendations
📊 Admin analytics dashboard
👨‍💻 Author

Rakshit Sinh
📧 Connect with me on GitHub

⭐ If you like this project

Give it a ⭐ on GitHub!
