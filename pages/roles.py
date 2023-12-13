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
    
    # Display details for selected person in a table
    if selected_person:
        st.subheader(f"Details for {selected_person}")
        details = {
            "Name": "",  # Replace with actual data
            "Age": "",  # Replace with actual data
            "Date of Birth": "",  # Replace with actual data
            "Educational History": "",  # Replace with actual data
            "Biography": "",  # Replace with actual data
            "Character Traits": "",  # Replace with actual data
            "Ethnicity": "",  # Replace with actual data
            "Personality": "",  # Replace with actual data
            "Motivations": "",  # Replace with actual data
        }
        st.table(details)
def main():
    homeui()

if __name__ == "__main__":
    main()