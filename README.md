# Youth Mental Wellness Chat (India)

> An AI-powered, confidential, and empathetic chat solution for supporting Indian youth in overcoming mental health stigma and accessing help.

## Features

- Confidential, non-judgmental chat powered by Google Gemini (Generative AI)
- Personalized responses in Hindi, English, Hinglish, or other Indian languages
- Culturally relevant, youth-friendly advice and coping strategies
- Multiple personalities: Friend, Girlfriend, Mentor
- Simple web interface (Flask + HTML/JS)

## Requirements

- Python 3.10+
- Google Gemini API key (set in `.env`)

## Setup (Local)

1. **Clone the repository**
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up your `.env` file:**
   - Create a file named `.env` in the project root:
     ```
     GEMINI_API_KEY=your_google_gemini_api_key
     ```
4. **Run the app:**
   ```sh
   python app.py
   ```
5. **Open in browser:**
   - Go to [http://localhost:5000](http://localhost:5000)

## Docker Usage

1. **Build the image:**
   ```sh
   docker build -t wellness-chat .
   ```
2. **Run the container:**
   ```sh
   docker run -p 8080:8080 --env-file .env wellness-chat
   ```
3. **Open in browser:**
   - Go to [http://localhost:8080](http://localhost:8080)

## Google Cloud Run Deployment

- See `.github/workflows/deploy.yml` for CI/CD setup.
- Set your `GCP_CREDENTIALS` and other secrets in GitHub Actions.

## Project Structure

```
mental-wellness-chat/
├── app.py              # Flask app (Gemini integration)
├── requirements.txt    # Python dependencies
├── Dockerfile          # For containerization
├── .env                # API key (not committed)
├── templates/
│   └── chat.html       # Frontend chat UI
└── .github/
	 └── workflows/
		  └── deploy.yml  # Cloud Run deployment workflow
```

## Notes & Issues

- **API Key Security:** Never commit your real API key. Use `.env` locally and GitHub secrets for deployment.
- **Language Personalization:** The AI is prompted to reply in the same language as the user's message (Hindi, English, Hinglish, etc.).
- **No persistent storage:** User context is in-memory. For production, use Firestore or Redis.
- **No professional crisis support:** If a user expresses severe distress, the AI gently suggests reaching out to a trusted adult or professional.

## Improvements & Suggestions

- Add language detection for more accurate replies.
- Integrate persistent storage for user context/history.
- Add more personalities or regional/cultural nuances.
- Improve frontend for mobile and accessibility.

## License

MIT
