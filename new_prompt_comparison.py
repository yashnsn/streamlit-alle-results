import streamlit as st
import os
from PIL import Image
import json

st.set_page_config(layout="wide")

root_path = "combined_images_output_2_updated_prompt"
supp_path = "combined_images_output_2"
# supp_path_2 = "combined_images_output_3"

cats = [None]
cats += [i for i in os.listdir(root_path) if not i.startswith('.')]
selected_cat = st.selectbox("Select a category", cats)

if selected_cat:
    all_files = os.listdir(f'{root_path}/{selected_cat}')
    all_files.sort()

    for ind_prefix in all_files:
        if not os.path.exists(f'{root_path}/{selected_cat}/{ind_prefix}/output_turbo.png') or not os.path.exists(f'{supp_path}/{selected_cat}/{ind_prefix}/output_turbo.png'):
            continue

        # old_metadata_2 = json.load(open(f'{supp_path_2}/{selected_cat}/{ind_prefix}/metadata.json'))
        old_metadata = json.load(open(f'{supp_path}/{selected_cat}/{ind_prefix}/metadata.json'))
        new_metadata = json.load(open(f'{root_path}/{selected_cat}/{ind_prefix}/metadata.json'))

        st.write(ind_prefix)
        st.write("Old prompt")
        st.write(old_metadata["image_generation_prompt"])
        # st.write("Intermediate prompt")
        # st.write(old_metadata_2["image_generation_prompt"])
        st.write("New prompt")
        st.write(new_metadata["image_generation_prompt"])
        # st.divider()
        cols = st.columns(4)
        cols[0].write("Cropped garment")
        cols[0].image(Image.open(f'{root_path}/{selected_cat}/{ind_prefix}/cropped_garment.jpg'))
        cols[1].write("Reference(upscaled)")
        cols[1].image(Image.open(f"{root_path}/{selected_cat}/{ind_prefix}/reference_upscaled.jpg"))
        cols[2].write("Output - Gen 4(turbo) - old")
        cols[2].image(Image.open(f'{supp_path}/{selected_cat}/{ind_prefix}/output_turbo.png'))
        # cols[3].write("Output - Gen 4(turbo) - intermediate")
        # cols[3].image(Image.open(f'{supp_path_2}/{selected_cat}/{ind_prefix}/output_turbo.png'))
        cols[3].write("Output - Gen 4(turbo)")
        cols[3].image(Image.open(f'{root_path}/{selected_cat}/{ind_prefix}/output_turbo.png'))
        
        st.divider()