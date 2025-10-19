# 🕵️‍♂️ Privacy Policy Analyzer

An **AI-powered Privacy Policy Analyzer** built using **Flask** and **Groq’s Llama 3.3-70B model**.  
It reads privacy policies and summarizes them into a concise table highlighting:

- 🔍 **Key Points** — main findings & risk levels  
- 👤 **Your Rights** — what you can do  
- 📊 **Data Practices** — what’s collected, why, and who it’s shared with  
- ⚡ **Actions** — what steps you should take immediately  

---

## 🚀 Features
- 🧠 AI-driven summarization using **Groq Llama 3.3-70B**
- 🪶 Lightweight **Flask backend**
- 📋 Structured **Markdown table** output
- 🔐 Focused on privacy, no data stored
- 🔄 One-click chat reset

---

## 🏗️ Project Structure
projectanalyzer/
│
├── app.py # Flask backend
├── templates/
│ └── index.html # Frontend interface
├── .env # Your GROQ_API_KEY
├── requirements.txt # Dependencies
└── README.md # Project documentation

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yeulsanket/projectanalyzer.git
cd projectanalyzer
2️⃣ Create a Virtual Environment (optional)
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add Environment Variable

Create a .env file in the root folder:

GROQ_API_KEY=your_groq_api_key_here


Get your API key from https://console.groq.com

5️⃣ Run the App
python app.py


Then open:

http://localhost:5000