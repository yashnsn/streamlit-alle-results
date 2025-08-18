import os
import json
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

root_path = "combined_images_output_2"

cats = [None]
cats += list(os.listdir(root_path))

selected_cats = st.selectbox("Select Category", cats)

if selected_cats:
    all_files = list(os.listdir(f'{root_path}/{selected_cats}'))
    all_files.sort()
    for ind_prefix in all_files:
        if not os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output.png'):
            continue
        
        with open(f'{root_path}/{selected_cats}/{ind_prefix}/metadata.json', 'r') as f:
            metadata = json.load(f)

        original_image = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/cropped_garment.jpg')
        ref_image = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/reference_upscaled.jpg')
        gen_image_gen4 = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output.png')
        gen_image_turbo = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo.png')
        gen_image_turbo_refined = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo_refined.jpg')
        gen_image_turbo_upscaled = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo_upscaled.jpg')

        st.write(ind_prefix)
        st.write(metadata)

        cols = st.columns(6)
        cols[0].write("Original")
        cols[1].write("Reference(upscaled)")
        cols[2].write("Output - Gen 4(regular)")
        cols[3].write("Output - Gen 4 turbo")
        cols[4].write("Output - Gen 4 turbo(refined)")
        cols[5].write("Output - Gen 4 turbo(upscaled)")
        
        cols[0].image(original_image)
        cols[1].image(ref_image)
        cols[2].image(gen_image_gen4)
        cols[3].image(gen_image_turbo)
        cols[4].image(gen_image_turbo_refined)
        cols[5].image(gen_image_turbo_upscaled)

        st.divider()

        
        