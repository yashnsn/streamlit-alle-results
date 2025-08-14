import streamlit as st
import os
from PIL import Image

st.set_page_config(page_title="Pinterest Base Image Gen Comparor", page_icon=":chart_with_upwards_trend:", layout="wide")

root_path = "pinterest_base_images_testset_output"

cats = [None]
cats += list(os.listdir(root_path))
selected_cat = st.selectbox("Select Category", cats)
# for cat in cats:
if selected_cat:
    # if not selected_cat.startswith('.'):
    #     continue
    
    all_prefixes = {i.split('_')[0] for i in os.listdir(f'{root_path}/{selected_cat}')}
    for ind_prefix in all_prefixes:
        if not os.path.exists(f'{root_path}/{selected_cat}/{ind_prefix}_original'):
            continue

        original_image = Image.open(f'{root_path}/{selected_cat}/{ind_prefix}_original/reference.jpg')
        garment_image = Image.open(f'{root_path}/{selected_cat}/{ind_prefix}_original/garment.jpg')
        gen_image = Image.open(f'{root_path}/{selected_cat}/{ind_prefix}_original/output.png')
        gen_image_upscaled = Image.open(f'{root_path}/{selected_cat}/{ind_prefix}_upscaled/output.png')
        gen_image_upscaled_refined = Image.open(f'{root_path}/{selected_cat}/{ind_prefix}_upscaled_refined/output.png')

        cols = st.columns(5)

        with cols[0]:
            st.write("Original Image")
            st.image(original_image)
        with cols[1]:
            st.write("Garment Image")
            st.image(garment_image)
        with cols[2]:
            st.write("Output using Original referenence")
            st.image(gen_image)
        with cols[3]:
            st.write("Output using upscaled image")
            st.image(gen_image_upscaled)
        with cols[4]:
            st.write("Output using refined + upscaled image")
            st.image(gen_image_upscaled_refined)

        st.divider()