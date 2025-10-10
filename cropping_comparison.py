import streamlit as st
import os
from PIL import Image

root_path = "/Users/yaswanth/repositories/prog_content/prog_content_testset_sampled"

st.set_page_config(layout='wide')

all_cats = [i for i in os.listdir(root_path) if not i.startswith('.')]
selected_cat = st.selectbox("Select a category", all_cats)

if selected_cat:
    all_files = [i for i in os.listdir(f'{root_path}/{selected_cat}') if not i.startswith('.') and os.path.exists(f'{root_path}/{selected_cat}/{i}/garment_cropped_nonthinking.jpg')]
    all_files.sort()

    for ind_file in all_files:
        cols = st.columns(3)
        image1 = Image.open(f'{root_path}/{selected_cat}/{ind_file}/garment_cropped_nonthinking.jpg')
        image2 = Image.open(f'{root_path}/{selected_cat}/{ind_file}/cropped_garment.jpg' if os.path.exists(f'{root_path}/{selected_cat}/{ind_file}/cropped_garment.jpg') else f'{root_path}/{selected_cat}/{ind_file}/garment_cropped.jpg')
        image3 = Image.open(f'{root_path}/{selected_cat}/{ind_file}/garment.jpg')
        cols[0].write("Garment cropped nonthinking")
        cols[0].image(image3)
        cols[1].write("Garment cropped")
        cols[1].image(image2)
        cols[2].write("Garment cropped thinking")
        cols[2].image(image1)