import os
import streamlit as st

# ------- Constants and Configuration --------

st.set_page_config(page_title="Tomast", page_icon="🪖", layout='wide')

# ------- General UI -------

def homeui():
    st.title("This is Tomast")
    
    # Sidebar for navigation
    st.sidebar.title("People with roles")
    people = ["Person 1", "Person 2", "Person 3"]  # Replace with actual names
    selected_person = st.sidebar.selectbox("Select a person", people)
    
    # Display details for selected person
    if selected_person:
        st.subheader(f"Details for {selected_person}")
        st.text("Name: ")  # Replace with actual data
        st.text("Age: ")  # Replace with actual data
        st.text("Date of Birth: ")  # Replace with actual data
        st.text("Educational History: ")  # Replace with actual data
        st.text("Biography: ")  # Replace with actual data
        st.text("Character Traits: ")  # Replace with actual data
        st.text("Ethnicity: ")  # Replace with actual data
        st.text("Personality: ")  # Replace with actual data
        st.text("Motivations: ")  # Replace with actual data
