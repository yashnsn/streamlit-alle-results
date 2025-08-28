import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

root_path = "multi-threaded-test_V16_selected_comparison"

for ind_file in os.listdir(f'{root_path}/tryon'):
    if ind_file.startswith('.'):
        continue

    garment_img = Image.open(f'{root_path}/garment/{ind_file}')
    base_img = Image.open(f'{root_path}/human/{ind_file}')
    tryon_old = Image.open(f'{root_path}/tryon_old/{ind_file.replace(".jpg.jpg",".jpg").replace(".png.png",".png")}')
    tryon = Image.open(f'{root_path}/tryon/{ind_file}')

    cols = st.columns(4)

    cols[0].write('garment image')
    cols[0].image(garment_img)
    cols[1].write('base image')
    cols[1].image(base_img)
    cols[2].write('tryon old result')
    cols[2].image(tryon_old)
    cols[3].write('tryon result')
    cols[3].image(tryon)

    st.divider()