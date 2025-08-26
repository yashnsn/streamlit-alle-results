import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')
all_cats = [None, 'tops', 'dresses']
selected_cat = st.selectbox('category',all_cats)

if selected_cat:
    if selected_cat in 'dresses':
        root_path = "/Users/yaswanth/repositories/alphabake_experimentation/outputs/multi-threaded-test_V12"
    else:
        root_path = "/Users/yaswanth/repositories/alphabake_experimentation/outputs/multi-threaded-test_V13"

    all_files = list(os.listdir(f"{root_path}/tryon"))
    all_files.sort()
    for ind_file_name in all_files:
        if ind_file_name.startswith('.'):
            continue

        cols = st.columns(3)
        cols[0].image(Image.open(f'{root_path}/human/{ind_file_name}'))
        cols[1].image(Image.open(f'{root_path}/garment/{ind_file_name}'))
        cols[2].image(Image.open(f'{root_path}/tryon/{ind_file_name}'))