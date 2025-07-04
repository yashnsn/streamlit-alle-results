import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Custom Attention Flux", layout="wide")

base_images_path = 'synthetic_dataset/synthetic_base_images'
source_images_path = 'synthetic_dataset/synthetic_data_products'
altered_base_images_path = 'synthetic_dataset/synthetic_base_images_altered'
altered_source_images_path = 'synthetic_dataset/synthetic_data_products_altered'
superres_source_images_path = 'synthetic_dataset/synthetic_data_products_super_res'
superres_base_images_path = 'synthetic_dataset/synthetic_base_images_super_res'

for ind_file_name in os.listdir(source_images_path):
    if ind_file_name.startswith('.') or ind_file_name.endswith('.json') or ind_file_name in ['outfit_40.png','outfit_21.png','1118817_1000.jpg','1089201_1000.jpg','175763_1004.jpg','725879_1001.jpg','898604_1000.jpg']:
        continue
    st.write(f'File name: {ind_file_name}')
    cols = st.columns(6)
    
    with cols[0]:
        st.write('Source image')
        st.image(Image.open(f'{source_images_path}/{ind_file_name}'), use_container_width=True)
    with cols[1]:
        st.write('Base image')
        st.image(Image.open(f'{base_images_path}/{ind_file_name}'), use_container_width=True)
    with cols[2]:
        st.write('Altered source image')
        st.image(Image.open(f'{altered_source_images_path}/{ind_file_name}'), use_container_width=True)
    with cols[3]:
        st.write('Altered base image')
        st.image(Image.open(f'{altered_base_images_path}/{ind_file_name}'), use_container_width=True)
    with cols[4]:
        st.write('Altered source image')
        st.image(Image.open(f'{superres_source_images_path}/{ind_file_name}'), use_container_width=True)
    with cols[5]:
        st.write('Altered base image')
        st.image(Image.open(f'{superres_base_images_path}/{ind_file_name}'), use_container_width=True)

    st.divider()