import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

old_alphabake_results_path = "alphabake_old_tryon"
new_alphabake_path = "multi-threaded-test_V15"

google_results_path = "tryon_results"

all_files = [i for i in os.listdir(f'{new_alphabake_path}/tryon') if not i.startswith('.')]
all_files.sort()
for ind_file in all_files:
    base_img = Image.open(f"{new_alphabake_path}/human/{ind_file}")
    garment_img = Image.open(f"{new_alphabake_path}/garment/{ind_file}")

    old_alphabake_tryon = Image.open(f'{old_alphabake_results_path}/{ind_file.replace(".png","")}')
    new_alphabake_tryon = Image.open(f'{new_alphabake_path}/tryon/{ind_file}')

    google_tryon = Image.open(f'{google_results_path}/{ind_file.replace(".png_base_image","").replace(".jpg","_rmbg.jpg")}')

    cols = st.columns(5)

    cols[0].write('Base image')
    cols[0].image(base_img)
    cols[1].write('Garment image')
    cols[1].image(garment_img)
    cols[2].write('Old alphabake tryon result')
    cols[2].image(old_alphabake_tryon)
    cols[3].write('New alphabake tryon result')
    cols[3].image(new_alphabake_tryon)
    cols[4].write('Google tryon result')
    cols[4].image(google_tryon)

    st.divider()