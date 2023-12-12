import os
import openai
import streamlit as st


# ------- Constants and Configuration --------

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
openai.api_key = os.environ['OPENAI_API_KEY']
st.set_page_config(page_title="NexaChat", page_icon="🧙‍♂️", layout='wide')


# ------- General UI -------

def home_ui():
    st.title('Conduct a synthetic Interview 🧙‍♂️')
    st.markdown("""
    Welcome to NexaChat! This application allows you to create a tailored AI-generated persona and conduct a manual or automatic interview with it. \n
    Gain first insights and prepare for a real interview. Let's get started!
    """)
    st.markdown("")
    st.subheader('How to conduct your synthetic interview')
    "1. Enter an interview topic."
    "2. Generate your persona."
    "3. Start the conversation."
    "Use the sidebar to navigate."
    st.markdown("")
    st.subheader('Enter your interview topic 👇')
    if 'project_problem' not in st.session_state:
        st.session_state['project_problem'] = "How to conduct synthetic interviews"
    st.session_state['project_problem'] = st.text_area("Interview Topic", value=st.session_state.get('project_problem', ''), placeholder="Enter your interview topic here and continue by clicking on '1️⃣ Generate Persona' in the sidebar.")
    if st.session_state['project_problem'] != "How to conduct synthetic interviews":
        st.success("Interview topic saved! Continue through the sidebar.")

# ------- Main App -------

def main():
    home_ui()

if __name__ == "__main__":
    main()