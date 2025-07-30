import streamlit as st
from google import genai
import os
import requests
from pathlib import Path
from api import gemini_api_call
from svg import svg_paths

st.title("Chat Bot")


# SVG file paths
paths = svg_paths()

if "history" not in st.session_state:
    st.session_state.history = [] # Array to keep track of history

for speaker,text in st.session_state.history:
    avatar = paths[1] if speaker == "You" else paths[0]
    role = "user" if speaker == "You" else "echobot"
    with st.chat_message(role,avatar=str(avatar)):
        st.markdown(text)

prompt = st.chat_input("Say something")
  #Build the request body
if prompt:
    
    st.session_state.history.append(("You",prompt))
    with st.chat_message("user",avatar=str(paths[1])):
                st.markdown(f"{prompt}")
    with st.spinner(text="Thinking...",show_time=True): # To show user that the answer is processing
        candidates = gemini_api_call(api_key=os.getenv("GEMINI_API_KEY"),prompt=prompt)
        if not candidates:
            print("No response candidates returned.")
        else:
    # Each candidate has a .content.parts array of {text:"…"} objects
            first = candidates[0]["content"]
            text = "".join(part.get("text", "") for part in first.get("parts", []))  
    
        with st.chat_message("echobot",avatar=str(paths[0])): #To differentiate between the user and bot output
                st.markdown(f"{text}")
        st.session_state.history.append(("Bot",text))
    







    
    