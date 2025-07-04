import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Custom Attention Flux", layout="wide")

condition_image_path = 'synthetic_training_dataset/control_image'
target_image_path = "synthetic_training_dataset/target_image"


for ind_file_name in {i.replace('super_res_','').replace('altered_','') for i in os.listdir(condition_image_path)}:
    st.write(f'File name: {ind_file_name}')
    cols = st.columns(4)
    
    with cols[0]:
        st.write('Condition image')
        st.image(Image.open(f'{condition_image_path}/super_res_{ind_file_name}'), use_container_width=True)
    with cols[1]:
        st.write('Base image')
        st.image(Image.open(f'{target_image_path}/super_res_{ind_file_name}'), use_container_width=True)
    with cols[2]:
        st.write('Condition image')
        st.image(Image.open(f'{condition_image_path}/altered_{ind_file_name}'), use_container_width=True)
    with cols[3]:
        st.write('Base image')
        st.image(Image.open(f'{target_image_path}/altered_{ind_file_name}'), use_container_width=True)

    st.divider()