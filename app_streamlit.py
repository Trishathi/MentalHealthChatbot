import streamlit as st
import os
from google import genai

# --- Configure the AI models ---
# Note: Streamlit's deployment environment lets you set secrets for API keys
#genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# --- Part 1: Your Helper Functions ---
def contains_crisis_keywords(user_input):
    # Same function as before
    crisis_keywords = ["suicide", "kill myself", "end my life", "harm myself", "want to die"]
    for keyword in user_input.lower().split():
        if keyword in crisis_keywords:
            return True
    return False

# --- Part 2: The Streamlit App Interface ---
st.title("Mental Health Companion Chatbot")
st.caption("This is an AI companion, not a professional counselor. If you are in crisis, please seek immediate help.")

# Initialize chat history in Streamlit's session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# In your sidebar
with st.sidebar:
    st.title("Settings")
    mood = st.select_slider(
        "How is your energy today?",
        options=["Low/Burned out", "Feeling okay", "Highly Anxious", "Energetic/Productive"],
        value="Feeling okay"
    )
    st.write(f"The AI will now tailor its tone to: **{mood}**")

# Then, inject this into your Gemini prompt:
# "The user currently identifies their mood as {mood}. Adjust your empathy level accordingly."
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
if prompt := st.chat_input("Say something..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Check for crisis keywords first
    if contains_crisis_keywords(prompt):
        response = "Please, if you are in crisis, reach out to a professional immediately. You can contact a mental health crisis hotline like [Insert Hotline Number Here] for immediate, compassionate support."
        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        # Display bot response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
    else:
        # Craft the prompt for Gemini
        prompt_text = f"""
        You are a compassionate, empathetic, and non-judgmental mental health chatbot for students.
        Your purpose is to listen and provide support, not medical advice.
        A user has messaged you. The user is feeling {mood}. Please respond to their next message in a tone that fits this energy level.
        The user's message is: "{prompt}"
        """

        client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

        # --- Call the Gemini model ---
        response = client.models.generate_content(
            model="gemini-1.5-flash",  # you can switch to another Gemini model if needed
            contents=prompt_text
        )

        # Add bot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        # Display bot response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response.text)
