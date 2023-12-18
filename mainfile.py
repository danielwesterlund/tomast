import streamlit as st
import openai
import os


# ------- Constants and Configuration --------

os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
openai.api_key = os.environ['OPENAI_API_KEY']

st.set_page_config(page_title="Tomast", page_icon="🪖", layout='wide')

st.session_state['model'] = "gpt-3.5-turbo"
st.session_state['language'] = "German"


# ------- General UI -------

def homeui():
    st.title("This is Tomast")

    st.markdown("""
    Welcome to Tomast! This is TOMAST, an AI-powered operating system to facilitate the creation of scripts and materials for military exercises and training. 
    Let's get started!
    """)
    st.markdown("")
    st.subheader('Please define the Scenario 👇')



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



# ------- OpenAI Call -------

def call_openai_api(prompt, max_tokens=1000, temperature=0.4):
    model = st.session_state['model']
    language = st.session_state['language']
    system = f"""You always generate in {language}."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response['choices'][0]['message']['content'].strip()
    except (KeyError, Exception) as e:
        return f"An error occurred: {e}"
    


def main():
    homeui()

if __name__ == "__main__":
    main()