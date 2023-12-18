import streamlit as st
import openai
import os


def homeui():
    st.title("This is Scenario")
    st.write(st.session_state['scenario'])

    st.subheader("Scenario Summary")
    st.text_area("Summary", "Enter the summary here...", height=200)
    

 
def main():
    homeui()

if __name__ == "__main__":
    main()