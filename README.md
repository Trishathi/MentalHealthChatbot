# 🧠 Student Mental Health Companion Chatbot

An empathetic, accessible, and privacy-focused AI chatbot built to support students dealing with stress, anxiety, and academic burnout. Powered by Python, Streamlit, and the Google Gemini API.

---

## 📌 Project Overview

Planning academic schedules, managing exams, and balancing life can be overwhelming. Many students hesitate to seek initial support due to stigma or lack of immediate resources. 

This project provides an AI-driven, non-judgmental conversational agent designed to:
- Offer compassionate, real-time responses using tuned prompt engineering.
- Provide quick, actionable coping mechanisms (grounding techniques, breathing exercises).
- Offer instant access to emergency resources and crisis hotlines when needed.

> **Disclaimer:** This chatbot is an educational project designed for peer support and self-help resources. It is **not** a substitute for professional medical advice, diagnosis, or treatment.

---

## ✨ Key Features

* **Empathetic AI Interface:** Built with Google's Gemini LLM, guided by custom prompt templates to ensure supportive and safe responses.
* **Safety First & Crisis Intervention:** Dedicated crisis detection logic that provides immediate hotline contacts when distressed keywords are recognized.
* **Interactive Web App:** Clean, intuitive UI built using Streamlit's native chat components (`st.chat_message` and `st.chat_input`).
* **Mood-Adaptive Responses:** Includes an interactive mood selector so users can share their current emotional state (e.g., anxious, overwhelmed, low energy), allowing the AI to customize its tone, empathy, and recommendations accordingly.

---

## 🛠️ Tech Stack

* **Frontend & Web Framework:** [Streamlit](https://streamlit.io/)
* **AI Model & API:** [Google Gemini API](https://ai.google.dev/) (`google-genai`)
* **Language:** Python 3.10+

---

## 🚀 Getting Started

Follow these steps to run the project locally on your machine.

### Prerequisites

- Python 3.10 or higher installed.
- A Google Gemini API Key (obtainable from [Google AI Studio](https://aistudio.google.com/)).

### Installation & Setup

1. **Clone the Repository**
```bash
git clone [https://github.com/YOUR_USERNAME/mental-health-chatbot-streamlit.git](https://github.com/YOUR_USERNAME/mental-health-chatbot-streamlit.git)
cd mental-health-chatbot-streamlit

```

2. **Set Up a Virtual Environment (Recommended)**
* **Windows:**
```bash
python -m venv venv
venv\Scripts\activate

```


* **macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate

```




3. **Install Dependencies**
```bash
pip install -r requirements.txt

```


4. **Set Your API Key**
* **Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"

```


* **Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"

```


* **macOS / Linux:**
```bash
export GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"

```




5. **Run the Application**
```bash
python -m streamlit run app_streamlit.py

```



---

## 📁 Repository Structure

```text
├── app_streamlit.py    # Main Streamlit application file
├── requirements.txt    # Python package dependencies
├── README.md           # Project documentation
└── .gitignore          # Excluded files (e.g., venv, API keys)

```

---

## 💡 How It Works (Prompt Strategy)

The application uses dynamic prompt engineering to enforce safety boundaries before passing input to the Gemini model:

1. **Persona Definition:** Instructs the model to act as a supportive peer/companion rather than a medical doctor.
2. **Context Enclosure:** Safely structures user input within f-strings (`f"User input: {user_input}"`) to maintain conversation context.
3. **Guardrails:** Explicitly instructs the AI to avoid giving clinical diagnoses or medical prescriptions.

---

```

```
