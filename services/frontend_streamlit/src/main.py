import streamlit as st

st.title("Echo Bot")

if "history" not in st.session_state:
    st.session_state.history = [] #Array to keep track of history


prompt = st.chat_input("Say something")
if prompt:
    st.session_state.history.append(("You",prompt))
    st.session_state.history.append(("Bot",prompt))
    
for speaker,text in st.session_state.history:
        if speaker == "You":
            with st.chat_message("user"): 
                st.markdown(f"**You:** {text}")
        else:
            with st.chat_message("bot"): #To differentiate between the user and bot output
                st.markdown(f"**Bot:** {text}")

    
    