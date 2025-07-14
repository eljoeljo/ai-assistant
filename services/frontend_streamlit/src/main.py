import streamlit as st

st.title("Echo Bot")

if "history" not in st.session_state:
    st.session_state.history = [] #Array to keep track of history


with st.form(key="chat_form", clear_on_submit=True): #Input from user cleared from text area after being entered
    user_text = st.text_input("You:")
    submit = st.form_submit_button("Send")
    if submit and user_text:
        st.session_state.history.append(("You",user_text)) 
        st.session_state.history.append(("Bot",user_text))
    
for speaker,text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")

    
    