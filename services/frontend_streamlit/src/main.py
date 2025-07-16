import streamlit as st
import os
st.title("Echo Bot")

if "history" not in st.session_state:
    st.session_state.history = [] #Array to keep track of history


prompt = st.chat_input("Say something")
if prompt:
    st.session_state.history.append(("You",prompt))
    st.session_state.history.append(("Bot",prompt))
    
svg_directory = "/Users/eljo/Desktop/projects/applications/ai-assistant/services/frontend_streamlit/svg_files" #Absolute Path for AI SVG
svg_filename = "robot-svgrepo-com.svg"
svg_file_path = os.path.join(svg_directory, svg_filename)

    
svg_directory2 = "/Users/eljo/Desktop/projects/applications/ai-assistant/services/frontend_streamlit/svg_files" #Absolute Path for User SVG
svg_filename2 = "user-svgrepo-com.svg"
svg_file_path2 = os.path.join(svg_directory2, svg_filename2)


for speaker,text in st.session_state.history:
        if speaker == "You":
            with st.chat_message("user",avatar=svg_file_path2):
                st.markdown(f"{text}")
        else:
            with st.chat_message("echobot",avatar=svg_file_path): #To differentiate between the user and bot output
                st.markdown(f"{text}")

    
    