import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

root_path = "testset_1010"
all_cats = [None]+[i for i in os.listdir(root_path) if not i.startswith('.')]

selected_cat = st.selectbox('Select the category', all_cats)

if selected_cat:
    for ind_file in os.listdir(f'{root_path}/{selected_cat}'):
        if selected_cat.startswith('.'):
            continue
        
        img = Image.open(f'{root_path}/{selected_cat}/{ind_file}')
        st.image(img)
        st.divider()