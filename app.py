from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing in the environment variables.")

# -----------------------------
# Initialize Chat Model
# -----------------------------
chat = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key
)

# -----------------------------
# Flask app
# -----------------------------
app = Flask(__name__)
chat_history = [
    {"role": "system", "content":
     "You are a professional Privacy Policy Analyzer. "
     "You read privacy policy text in sections and extract key facts clearly and concisely. "
     "Always provide: Key Points, User Rights, Data Collection & Usage, and Next Steps if relevant. "
     "If the user provides a short snippet or a section title, respond based on that section."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please provide some text to analyze."})
    
    chat_history.append({"role": "user", "content": user_input})
    
    try:
        response = chat.invoke(chat_history)
        bot_message = response.content
        chat_history.append({"role": "assistant", "content": bot_message})
        return jsonify({"response": bot_message})
    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
