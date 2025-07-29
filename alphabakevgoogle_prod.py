import os
import streamlit as st
from PIL import Image

alphabake_path = "alphabake_V5"
google_path = "google_results_V4"

st.set_page_config(layout="wide")

all_people = [None]
all_people += list(os.listdir(google_path))

selected_person = st.selectbox('Person',all_people)

if selected_person:
    # Use session state to store scores and reset if person changes
    if 'scores' not in st.session_state:
        st.session_state['scores'] = {}
    if 'last_person' not in st.session_state:
        st.session_state['last_person'] = None

    # Reset scores if person changes
    if st.session_state['last_person'] != selected_person:
        st.session_state['scores'] = {}
        st.session_state['last_person'] = selected_person

    all_files = [i for i in os.listdir(f'{google_path}/{selected_person}') if os.path.exists(f'{alphabake_path}/tryon/{selected_person}_base_image_{i}')]

    for ind_file in all_files:
        cols = st.columns(5)
        cols[0].write('base image')
        cols[0].image(Image.open(f'{alphabake_path}/human/{selected_person}_base_image_{ind_file}'))

        cols[1].write('Garment image')
        cols[1].image(Image.open(f'{alphabake_path}/garment/{selected_person}_base_image_{ind_file}'))
        
        cols[2].write('Alphabake tryon')
        cols[2].image(Image.open(f'{alphabake_path}/tryon/{selected_person}_base_image_{ind_file}'))

        cols[3].write('google tryon')
        cols[3].image(Image.open(f'{google_path}/{selected_person}/{ind_file}'))

        with cols[4]:
            model_choice = st.selectbox(
                "Select Model",
                ["alphabake", "google"],
                key=f"model_select_{selected_person}_{ind_file}"
            )
            # Store the choice in session state
            st.session_state['scores'][ind_file] = model_choice

    # After all files, summarize preferences
    if st.session_state['scores']:
        alphabake_files = [f for f, v in st.session_state['scores'].items() if v == "alphabake"]
        google_files = [f for f, v in st.session_state['scores'].items() if v == "google"]

        st.markdown("### Summary of Preferences")
        st.write(f"**Alphabake preferred:** {len(alphabake_files)}")
        if alphabake_files:
            st.write(alphabake_files)
        st.write(f"**Google preferred:** {len(google_files)}")
        if google_files:
            st.write(google_files)