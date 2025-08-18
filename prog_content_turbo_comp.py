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
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/reference.jpg'):
            ref_image = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/reference.jpg')
        else:
            ref_image = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/reference_upscaled.jpg'):
            ref_image_upscaled = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/reference_upscaled.jpg')
        else:
            ref_image_upscaled = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output.png'):
            gen_image_gen4 = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output.png')
        else:
            gen_image_gen4 = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo.png'):
            gen_image_turbo = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo.png')
        else:
            gen_image_turbo = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo_refined.jpg'):
            gen_image_turbo_refined = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo_refined.jpg')
        else:
            gen_image_turbo_refined = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo_upscaled.jpg'):
            gen_image_turbo_upscaled = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo_upscaled.jpg')
        else:
            gen_image_turbo_upscaled = None
        st.write(ind_prefix)
        st.write(metadata)

        cols = st.columns(7)
        cols[0].write("Original")
        cols[1].write("Reference")
        cols[2].write("Reference(upscaled)")
        cols[3].write("Output - Gen 4(regular)")
        cols[4].write("Output - Gen 4 turbo")
        cols[5].write("Output - Gen 4 turbo(refined)")
        cols[6].write("Output - Gen 4 turbo(upscaled)")
        
        cols[0].image(original_image)
        if ref_image:
            cols[1].image(ref_image)
        if ref_image_upscaled:
            cols[2].image(ref_image_upscaled)
        if gen_image_gen4:
            cols[3].image(gen_image_gen4)
        if gen_image_turbo:
            cols[4].image(gen_image_turbo)
        if gen_image_turbo_refined:
            cols[5].image(gen_image_turbo_refined)
        if gen_image_turbo_upscaled:
            cols[6].image(gen_image_turbo_upscaled)

        st.divider()

        
        