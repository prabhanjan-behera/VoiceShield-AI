# VoiceShield AI - Round 2 Prototype (MVP)

An intelligent call-monitoring prototype designed to protect senior citizens from financial fraud by detecting high-risk keywords in real-time across multiple regional languages.

## 🚀 Current Implementation (Phase 1 MVP)
In this round, we have built a functional frontend and a rule-based backend text/keyword interaction model:
- **Frontend Architecture:** Flutter mobile interface optimized for elderly users (large font targets, high contrast warning triggers).
- **Backend Core:** A real-time keyword-matching engine written in Python (`app.py`) supporting **10 regional languages**.
- **Fraud Trigger:** Continuously scans live conversation inputs for high-risk red-flag phrases (e.g., *"Paisa do"*, *"OTP batao"*, *"Account Block"*) and instantly triggers localized security warnings.

## 🛠️ Project Structure & Tech Stack
- **Frontend:** Flutter / Dart
- **Backend:** Python (`app.py` utilizing core pattern matching)

## 🔮 Future Roadmap (Phase 2 Update)
1. **AI Voice Biomarkers:** Integrating deep learning speech models (like Wav2Vec2 and OpenAI Whisper) to differentiate between genuine human speech and AI-cloned or synthetic voices.
2. **Telecom Level Gateway Integration:** Deploying the analysis engine directly at the carrier infrastructure level (partnering with telecom departments like Jio, Airtel, or BSNL) for network-wide safety without requiring separate app installations.
