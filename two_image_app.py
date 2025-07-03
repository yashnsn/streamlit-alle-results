import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Custom Attention Flux", layout="wide")

base_images_path = 'synthetic_dataset/synthetic_base_images'
source_images_path = 'synthetic_dataset/synthetic_data_products'

for ind_file_name in os.listdir(source_images_path):
    if ind_file_name.startswith('.') or ind_file_name.endswith('.json'):
        continue
    st.write(f'File name: {ind_file_name}')
    cols = st.columns(2)
    
    with cols[0]:
        st.write('Source image')
        st.image(Image.open(f'{source_images_path}/{ind_file_name}'), use_container_width=True)
    with cols[1]:
        st.write('base image')
        st.image(Image.open(f'{base_images_path}/{ind_file_name}'), use_container_width=True)

    st.divider()