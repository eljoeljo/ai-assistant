import streamlit as st

st.title("Echo Bot")

if "history" not in st.session_state:
    st.session_state.history = []

user_text = st.text_area("You:", "")

if st.button("Send") and user_text:
    st.session_state.history.append(("You",user_text))
    st.session_state.history.append(("Bot",user_text))
    
for speaker,text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**Bot:** {text}")

    
    