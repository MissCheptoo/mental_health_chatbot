# -*- coding: utf-8 -*-
import nltk
import streamlit as st
from nltk.chat.util import Chat, reflections

# Define chatbot conversation pairs
pairs = [
    (r"(.*)sad(.*)", ["I'm sorry you're feeling sad. Want to talk about what's causing it?"]),
    (r"(.*)anxious(.*)|(.*)anxiety(.*)", ["Anxiety can be overwhelming. Would you like some calming tips?"]),
    (r"(.*)stress(.*)", ["Stress is tough. Deep breathing or a short break might help. Want more ideas?"]),
    (r"(.*)depressed(.*)", ["It’s okay to feel this way. You're not alone. Would it help to explore some support resources?"]),
    (r"(.*)help(.*)", ["I'm here to listen. Can you tell me more about how you're feeling?"]),
    (r"(.*)thank(.*)", ["You're welcome! I'm here whenever you need to talk."]),
    (r"quit", ["Take care. Remember, you're not alone."]),
    (r"(.*)", ["That sounds tough. I'm here to listen. Would you like to share more?"])
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Streamlit app
def main():
    st.title("Mental Health Support Chatbot 🤖💬")
    st.write("This chatbot offers general emotional support. It’s **not a substitute for professional help**.")

    # Input box for user message
    user_input = st.text_input("How are you feeling today?")

    # Display chatbot response
    if user_input:
        response = chatbot.respond(user_input)
        st.write(f"**Chatbot:** {response}")

        # Disclaimer
        st.markdown("---")
        st.warning("⚠️ This chatbot provides general support only. If you're in crisis or need help, please contact a mental health professional.")

if __name__ == "__main__":
    main()
