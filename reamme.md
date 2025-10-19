🔍 Privacy Policy Analyzer
An AI-powered Privacy Policy Analyzer built using Flask and Groq's Llama 3.3-70B model. It reads privacy policies and summarizes them into a concise table highlighting:

📊 What You'll Get

🔍 Key Points — main findings & risk levels
👤 Your Rights — what you can do
📊 Data Practices — what's collected, why, and who it's shared with
⚡ Actions — what steps you should take immediately


🚀 Features

🧠 AI-driven summarization using Groq Llama 3.3-70B
🪶 Lightweight Flask backend
📋 Structured Markdown table output
🔒 Focused on privacy — no data stored
🔄 One-click chat reset


📁 Project Structure
projectanalyzer/
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend interface
├── .env                   # Your GROQ_API_KEY
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

🛠️ Setup Guide
1️⃣ Clone the Repository
bashgit clone https://github.com/yeulsanket/projectanalyzer.git
cd projectanalyzer
2️⃣ Create a Virtual Environment (Optional but Recommended)
macOS / Linux:
bashpython -m venv venv
source venv/bin/activate
Windows:
bashpython -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bashpip install -r requirements.txt
4️⃣ Set Up Environment Variable
Create a .env file in the root folder:
envGROQ_API_KEY=your_groq_api_key_here
🔑 Get your API key from: https://console.groq.com
5️⃣ Run the Application
bashpython app.py

📝 Usage

Open your browser and navigate to http://localhost:5000
Paste a privacy policy URL or text
Click "Analyze" to get your results
Review the structured breakdown of privacy practices


🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

📄 License
This project is open source and available under the MIT License.

⚠️ Disclaimer
This tool provides AI-generated summaries and should not be considered legal advice. Always read the full privacy policy for critical decisions.