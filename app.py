import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# Initialize app + Gemini
app = Flask(__name__)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# In-memory user context (can use Firestore/Redis in production)
user_context = {}

def build_prompt(user_id, user_message, personality="friend"):
    context = user_context.get(user_id, {"history": [], "status": {"stress": 5, "mood": "neutral"}})
    # Personality settings
    personalities = {
        "friend": "Talk like a caring best friend.",
        "girlfriend": "Talk like a supportive, loving girlfriend.",
        "mentor": "Talk like a wise mentor, supportive but professional."
    }
    persona = personalities.get(personality, "Talk like a supportive friend.")
    prompt = f"""
You are an empathetic, confidential AI companion for youth mental wellness in India.

Persona: {persona}

User's current mental status:
{context['status']}

Previous chat history (last 5 messages):
{context['history'][-5:]}

New message from user:
{user_message}

Your task:
1. Respond in a warm, friendly, and non-judgmental way. Never shame or blame the user.
2. Acknowledge their feelings and validate their experiences if it is positive so our ultimate goal achieve that is mental wellness.
3. Normalize mental health conversations—gently mention that it's okay to talk about feelings and that seeking help is a sign of strength.
4. Consider the user’s mental state & previous context in your reply.
5. If stress or sadness seems high, gently suggest practical, culturally familiar coping strategies (e.g., talking to a trusted friend or family member, taking a walk, listening to music, practicing yoga, journaling, etc.).
6. If the user expresses severe distress or mentions self-harm, gently encourage them to reach out to a trusted adult or mental health professional, while remaining supportive and non-alarming.
7. Share simple, evidence-based self-care tips and information about mental health in a youth-friendly, culturally relevant way.
8. Use Indian English, local idioms, and culturally relevant examples when appropriate.
9. Reply in the same language as the user's latest message (Hindi, English, Hinglish, or other Indian language).
10. Keep responses short, supportive, and like a real chat message.
"""
    return prompt

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data["user_id"]
    message = data["message"]
    personality = data.get("personality", "friend")

    # Build prompt
    prompt = build_prompt(user_id, message, personality)

    try:
        response = model.generate_content(prompt)
        reply = response.text
    except Exception as e:
        reply = f"Sorry, there was an error: {str(e)}"

    # Update context
    if user_id not in user_context:
        user_context[user_id] = {"history": [], "status": {"stress": 5, "mood": "neutral"}}
    user_context[user_id]["history"].append({"user": message, "bot": reply})
    return jsonify({"reply": reply, "status": user_context[user_id]["status"]})

if __name__ == "__main__":
    app.run(debug=True)
