import os
import openai
import streamlit as st


def homeui():
    st.title("This is Matrix")
    st.write(st.session_state['scenario'])


 
def main():
    homeui()

if __name__ == "__main__":
    main()