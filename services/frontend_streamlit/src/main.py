import streamlit as st
from google import genai
import os
import requests
from pathlib import Path
from api import gemini_api_call

st.title("Echo Bot")


#-Avatars- 
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SVG_DIR = ROOT / "svg_files"
robot_svg = SVG_DIR / "robot-svgrepo-com.svg"  #Relative Path for AI SVG
svg_file_path = str(robot_svg)
user_svg = SVG_DIR / "user-svgrepo-com.svg"  #Relative Path for User SVG
svg_file_path2 = str(user_svg)



if "history" not in st.session_state:
    st.session_state.history = [] #Array to keep track of history

for speaker,text in st.session_state.history:
    avatar = user_svg if speaker == "You" else robot_svg
    role = "user" if speaker == "You" else "echobot"
    with st.chat_message(role,avatar=str(avatar)):
        st.markdown(text)

prompt = st.chat_input("Say something")
#Build the request body
if prompt:
    
    st.session_state.history.append(("You",prompt))
    with st.chat_message("user",avatar=svg_file_path2):
                st.markdown(f"{prompt}")
    with st.spinner(text="Thinking...",show_time=True): #To show user that the answer is processing
        candidates = gemini_api_call(api_key=os.getenv("GEMINI_API_KEY"),prompt=prompt)
        if not candidates:
            print("No response candidates returned.")
        else:
    # Each candidate has a .content.parts array of {text:"…"} objects
            first = candidates[0]["content"]
            text = "".join(part.get("text", "") for part in first.get("parts", []))  
    
        with st.chat_message("echobot",avatar=svg_file_path): #To differentiate between the user and bot output
                st.markdown(f"{text}")
        st.session_state.history.append(("Bot",text))
    







    
    