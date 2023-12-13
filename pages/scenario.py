import os
import streamlit as st


def homeui():
    st.title("This is Scenario")
    if 'scenario' in st.session_state:
        st.write(st.session_state['scenario'])
    else:
        st.write("No scenario selected.")

    st.subheader("Scenario Summary")
    summary = st.text_area("Summary", "Enter the summary here...", height=200)
    if summary:
        st.session_state['summary'] = summary

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