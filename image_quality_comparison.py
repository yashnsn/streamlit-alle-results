import streamlit as st
from PIL import Image
import os

st.set_page_config(layout='wide')
root_path = "prog_content_image_quality"

all_files = [i for i in os.listdir(f"{root_path}/selected_images") if not i.startswith('.')]

for ind_file in all_files:
    cols = st.columns(3)

    img1 = Image.open(f'{root_path}/selected_images/{ind_file}')
    img2 = Image.open(f'{root_path}/selected_images_grained/{ind_file}')
    img3 = Image.open(f'{root_path}/selected_images_refined/{ind_file}')

    cols[0].write('Raw Image')
    cols[0].image(img1)

    cols[1].write('Grained image')
    cols[1].image(img2)

    cols[2].write('Refined image')
    cols[2].image(img3)

    st.divider()