from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_reponse(question):
    response = chat.send_message(question,stream=True)
    return response