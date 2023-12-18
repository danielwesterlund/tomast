import streamlit as st
import openai
import os

from openai import OpenAI


# ------- Constants and Configuration --------

st.set_page_config(page_title="Tomast", page_icon="🪖", layout='wide')

st.session_state['model'] = "gpt-3.5-turbo"
st.session_state['language'] = "German"


# Create an instance of the OpenAI API client
client = openai.ApiClient(
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']
openai.api_key = os.environ['OPENAI_API_KEY']
)


# ------- OpenAI Call -------

def call_openai_api(prompt, max_tokens=1000, temperature=0.4):
    model = st.session_state['model']
    language = st.session_state['language']
    system = f"""You always generate in {language}."""
    try:
        response = client.chat.completions.create(
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
    

    # ------- Scenario Summary  -------#

def scenario_summary():
    prompt = f"""The first input you always need is the Scenario which serves as the fundamental context in which the scenario takes place. This could either be a functional scenario which will include places, organisations and history. It will usually have a military context and include conflict and potential for conflict.

You will analyse this Scenario in detail:  {st.session_state['scenario']}

and will extract:
key people, 
alliances, 
important events, 
conflicting parties, 
potential betrayals 
and potentials for peace.

You will then summarise the scenario in 2-3 paragraphs.
    """
    scenario_summary = call_openai_api(prompt, max_tokens=1000)
    st.session_state['scenario'] = scenario_summary
    st.success("Summary generated...")
    return scenario_summary



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
            summary = scenario_summary()
            st.write(summary)
    


    


def main():
    homeui()

if __name__ == "__main__":
    main()
