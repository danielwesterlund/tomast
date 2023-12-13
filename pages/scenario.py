import os
import openai
import streamlit as st


def homeui():
    st.title("This is Scenario")
    st.write(st.session_state['scenario'])

    st.subheader("Scenario Summary")
    st.text_area("Summary", "Enter the summary here...", height=200)
    st.subheader("Scenario Images")
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        st.image(uploaded_file)
    st.subheader("Scenario Maps")
    uploaded_map = st.file_uploader("Choose a map...", type="jpg")
    if uploaded_map is not None:
        st.image(uploaded_map)

 
def main():
    homeui()

if __name__ == "__main__":
    main()