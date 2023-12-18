import streamlit as st
import openai
import os


# ------- Constants and Configuration --------

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
openai.api_key = os.environ['OPENAI_API_KEY']

st.set_page_config(page_title="Tomast", page_icon="🪖", layout='wide')


# ------- General UI -------

def homeui():
    st.title("This is Tomast")

    st.markdown("""
    Welcome to Tomast! This is TOMAST, an AI-powered operating system to facilitate the creation of scripts and materials for military exercises and training. 
    Let's get started!
    """)
    st.markdown("")
    st.subheader('Please define the Scenario 👇')

    prompt = "Please generate a blog outline on how a beginner can break into the field of data science."

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant with extensive experience in data science and technical writing."},
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)


    # Check if 'Scenario' already exists in session_state
    # If not, then initialize it
    if 'scenario' not in st.session_state:
        st.session_state['scenario'] = "The war in Kosovo"

    # If it is, update it
    scenario_input = st.text_area("Scenario", value=st.session_state.get('scenario', ''), placeholder="Enter your scenario here and continue by clicking on ...")
    
    if st.button('Submit'):
        if scenario_input:
            st.session_state['scenario'] = scenario_input
            st.success("Understood! The Scenario has been updated")

def main():
    homeui()

if __name__ == "__main__":
    main()