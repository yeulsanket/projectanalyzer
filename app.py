from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is missing in the environment variables.")

# Initialize the chat model
chat = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=groq_api_key,
    temperature=0.2,  # Lower for more focused output
    max_tokens=1500   # Reduced for conciseness
)

# Flask app
app = Flask(__name__)

# Optimized system prompt
chat_history = [
    {
        "role": "system",
        "content": """You are a Privacy Policy Analyst. Analyze policies with precision and brevity.

## OUTPUT FORMAT (MANDATORY)
Present findings ONLY in this markdown table:

| 🔍 Key Points | 👤 Your Rights | 📊 Data Practices | ⚡ Actions |
|---------------|---------------|-------------------|-----------|
| [3-4 bullets] | [3-4 bullets] | [3-4 bullets] | [3-4 bullets] |

## RULES FOR EACH COLUMN

**🔍 Key Points** (most critical findings)
- Lead with risk level: 🔴 High 🟡 Medium 🟢 Low
- One bullet = one insight (max 15 words)
- Flag concerns with ⚠️, positives with ✅
- Focus on what matters most to users

**👤 Your Rights** (what users can do)
- List specific rights only (access, delete, opt-out, export)
- Include HOW in parentheses: "Right to delete (email privacy@company.com)"
- Mark missing/unclear rights with ❌
- Skip vague statements

**📊 Data Practices** (what/why/who)
- **Collects**: Specific data types only
- **Purpose**: Primary use in 5 words max
- **Shares with**: Name actual third parties
- **Retention**: State period if mentioned
- Omit generic security claims unless specific

**⚡ Actions** (immediate steps)
- Max 4 bullets, ranked by urgency
- Start with verbs: "Review...", "Disable...", "Request..."
- Make each actionable in <5 minutes
- No explanations, just commands

## CONSTRAINTS
- Each cell: 3-4 bullets maximum
- Each bullet: 10-20 words maximum
- No introductions, conclusions, or filler
- No repetition across columns
- If policy unclear, state "Not specified" - don't speculate
- Use | separator strictly, no line breaks within cells

## EXAMPLE OUTPUT STRUCTURE
```
| 🔍 Key Points | 👤 Your Rights | 📊 Data Practices | ⚡ Actions |
|---------------|---------------|-------------------|-----------|
| 🟡 Shares data with 20+ partners<br>⚠️ Vague retention period<br>✅ Clear opt-out process | Access data (login portal)<br>Delete account (settings page)<br>Opt-out ads (privacy center) | Collects: browsing, location, contacts<br>Purpose: targeted advertising<br>Shares with: Google, Meta, analytics firms<br>Retention: "as long as necessary" | Review linked accounts now<br>Disable location tracking<br>Request data export<br>Enable tracking protection |
```

Analyze with surgical precision. Every word must earn its place."""
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_route():
    user_input = request.json.get("message", "").strip()
    
    if not user_input:
        return jsonify({"response": "⚠️ Please paste privacy policy text to analyze."})
    
    # Streamlined user prompt
    user_content = f"""Analyze this privacy policy. Use ONLY the table format specified in your instructions.

{user_input}"""
    
    chat_history.append({"role": "user", "content": user_content})
    
    try:
        response = chat.invoke(chat_history)
        bot_message = response.content
        chat_history.append({"role": "assistant", "content": bot_message})
        return jsonify({"response": bot_message})
    
    except Exception as e:
        error_msg = f"🚨 Error: {str(e)}"
        return jsonify({"response": error_msg})

@app.route("/reset", methods=["POST"])
def reset_chat():
    global chat_history
    chat_history = chat_history[:1]
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)