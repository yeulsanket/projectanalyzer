🕵️‍♂️ Privacy Policy Analyzer
An AI-powered Privacy Policy Analyzer built using Flask and Groq's Llama 3.3-70B model. It reads privacy policies and summarizes them into a concise table highlighting:

🔍 Key Points — main findings & risk levels
👤 Your Rights — what you can do
📊 Data Practices — what's collected, why, and who it's shared with
⚡ Actions — what steps you should take immediately


🚀 Features

🧠 AI-driven summarization using Groq Llama 3.3-70B
🪶 Lightweight Flask backend
📋 Structured Markdown table output
🔐 Focused on privacy — no data stored
🔄 One-click chat reset


🏗️ Project Structure
projectanalyzer/
│
├── app.py                 # Flask backend
├── templates/
│   └── index.html         # Frontend interface
├── .env                   # Your GROQ_API_KEY
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

⚙️ Setup Guide
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

🔑 Get your API key from https://console.groq.com

5️⃣ Run the Application
bashpython app.py
```

Then open your browser and navigate to:
```
http://localhost:5000

📖 Usage

Paste or upload a privacy policy into the text area
Click "Analyze" to process the document
Review the structured summary with key insights
Take action based on the recommendations provided


🛠️ Technologies Used

Flask — lightweight Python web framework
Groq API — Llama 3.3-70B model for AI analysis
HTML/CSS/JavaScript — frontend interface
python-dotenv — environment variable management


📦 Dependencies
Key packages (see requirements.txt for complete list):

flask — web framework
groq — API client for Groq
python-dotenv — environment configuration


🔒 Privacy & Security

No data storage — policies are analyzed in real-time
API calls are made securely to Groq's servers
Local processing — your API key stays in your environment


🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request


📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Sanket Yeul

GitHub: @yeulsanket


🙏 Acknowledgments

Groq for providing the powerful Llama 3.3-70B model
Flask community for the excellent web framework
All contributors who help improve this project


📧 Support
If you encounter any issues or have questions, please:

Open an issue on GitHub Issues
Check existing issues for solutions


⭐ Star This Repository
If you find this project useful, please give it a star! It helps others discover the project and motivates continued development.

Made with ❤️ by Sanket Yeul