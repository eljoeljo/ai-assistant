import streamlit as st
from google import genai
import os
import requests
from pathlib import Path

st.title("Echo Bot")
client = genai.Client() #Instantiating client and reading key
API_KEY = os.getenv("GEMINI_API_KEY") #Loading API Key

if "history" not in st.session_state:
    st.session_state.history = [] #Array to keep track of history


prompt = st.chat_input("Say something")
if prompt:
    st.session_state.history.append(("You",prompt))
    response = client.models.generate_content( #Sending prompt to Gemini
    model="gemini-2.5-flash", contents=prompt
    )
    st.session_state.history.append(("Bot",response.text))
    
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SVG_DIR = ROOT / "svg_files"
    
 #Relative Path for AI SVG
robot_svg = SVG_DIR / "robot-svgrepo-com.svg"
svg_file_path = str(robot_svg)

    
 #Relative Path for User SVG
user_svg = SVG_DIR / "user-svgrepo-com.svg"
svg_file_path2 = str(user_svg)


for speaker,text in st.session_state.history:
        if speaker == "You":
            with st.chat_message("user",avatar=svg_file_path2):
                st.markdown(f"{text}")
        else:
            with st.chat_message("echobot",avatar=svg_file_path): #To differentiate between the user and bot output
                st.markdown(f"{text}")




    
    