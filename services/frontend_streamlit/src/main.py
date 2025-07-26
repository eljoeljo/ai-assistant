import streamlit as st
from google import genai
import os
import requests
from pathlib import Path

st.title("Echo Bot")
client = genai.Client() #Instantiating client and reading key

#-Avatars- 
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SVG_DIR = ROOT / "svg_files"
robot_svg = SVG_DIR / "robot-svgrepo-com.svg"  #Relative Path for AI SVG
svg_file_path = str(robot_svg)
user_svg = SVG_DIR / "user-svgrepo-com.svg"  #Relative Path for User SVG
svg_file_path2 = str(user_svg)



API_KEY = os.getenv("GEMINI_API_KEY") #Loading API Key

if "history" not in st.session_state:
    st.session_state.history = [] #Array to keep track of history

for speaker,text in st.session_state.history:
    avatar = user_svg if speaker == "You" else robot_svg
    role = "user" if speaker == "You" else "echobot"
    with st.chat_message(role,avatar=str(avatar)):
        st.markdown(text)

prompt = st.chat_input("Say something")
if prompt:
    st.session_state.history.append(("You",prompt))
    with st.chat_message("user",avatar=svg_file_path2):
                st.markdown(f"{prompt}")
    with st.spinner(text="Thinking...",show_time=True): #To show user that the answer is processing
        response = client.models.generate_content( #Sending prompt to Gemini
        model="gemini-2.5-flash", contents=prompt
        )   
    
        bot_text = response.text
    
    
        with st.chat_message("echobot",avatar=svg_file_path): #To differentiate between the user and bot output
                st.markdown(f"{bot_text}")
        st.session_state.history.append(("Bot",bot_text))
    







    
    