import os
import json
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

root_path = "combined_images_output_3"
supp_path = "combined_images_output_2"
cats = [None]
cats += list(os.listdir(root_path))
cats.remove('lowerbody')

selected_cats = st.selectbox("Select Category", cats)

if selected_cats:
    all_files = list(os.listdir(f'{root_path}/{selected_cats}'))
    all_files.sort()
    for ind_prefix in all_files:
        if not os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output.png'):
            continue
        
        with open(f'{root_path}/{selected_cats}/{ind_prefix}/metadata.json', 'r') as f:
            metadata1 = json.load(f)
        with open(f'{supp_path}/{selected_cats}/{ind_prefix}/metadata.json', 'r') as f:
            metadata2 = json.load(f)

        original_image = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/cropped_garment.jpg')

        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/reference_upscaled.jpg'):
            ref_image_upscaled = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/reference_upscaled.jpg')
        else:
            ref_image_upscaled = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output.png'):
            gen_image_gen4 = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output.png')
            gen_image_gen4_supp = Image.open(f'{supp_path}/{selected_cats}/{ind_prefix}/output.png')
        else:
            gen_image_gen4 = None
            gen_image_gen4_supp = None
        if os.path.exists(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo.png'):
            gen_image_turbo = Image.open(f'{root_path}/{selected_cats}/{ind_prefix}/output_turbo.png')
            gen_image_turbo_supp = Image.open(f'{supp_path}/{selected_cats}/{ind_prefix}/output_turbo.png')
        else:
            gen_image_turbo = None
            gen_image_turbo_supp = None
        
        st.write(ind_prefix)
        st.write("Old prompt")
        st.write(metadata2)
        st.write("New prompt")
        st.write(metadata1)

        cols = st.columns(6)
        cols[0].write("Original")
        cols[1].write("Reference(upscaled)")
        cols[2].write("Output - Gen 4(regular - old)")
        cols[3].write("Output - Gen 4(regular)")
        cols[4].write("Output - Gen 4(turbo) - old")
        cols[5].write("Output - Gen 4(turbo)")
        
        cols[0].image(original_image)
        if ref_image_upscaled:
            cols[1].image(ref_image_upscaled)
        if gen_image_gen4_supp:
            cols[2].image(gen_image_gen4_supp)
        if gen_image_gen4:
            cols[3].image(gen_image_gen4)
        if gen_image_turbo_supp:
            cols[4].image(gen_image_turbo_supp)
        if gen_image_turbo:
            cols[5].image(gen_image_turbo)
        

        st.divider()

        
        