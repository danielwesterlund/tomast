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

    # Create a HTML table with custom CSS
    table_html = """
    <table style="width:100%">
        <thead style="background-color: lightgray; font-weight: bold;">
            <tr>
                <th>Name</th>
                <th></th>
            </tr>
        </thead>
        <tbody>
    """
    for key, value in details.items():
        table_html += f"<tr><td>{key}</td><td>{value}</td></tr>"
    table_html += "</tbody></table>"

    st.markdown(table_html, unsafe_allow_html=True)

    
def main():
    homeui()

if __name__ == "__main__":
    main()