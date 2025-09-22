from PIL import Image
import streamlit as st
import os

st.set_page_config(layout='wide')

root_path = "synthetic_dataset_V7"

for ind_folder in os.listdir(root_path):
    if ind_folder.startswith('.'):
        continue
    
    base_image_file_name = [i for i in os.listdir(f'{root_path}/{ind_folder}') if 'primary' in i][0]
    cols = st.columns(4)
    orig_garment_image = Image.open(f'{root_path}/{ind_folder}/original_garment.jpg')
    base_image = Image.open(f'{root_path}/{ind_folder}/{base_image_file_name}')
    tryon_image = Image.open(f'{root_path}/{ind_folder}/tryon.jpg')
    garment_image = Image.open(f'{root_path}/{ind_folder}/garment.jpg')

    cols[0].write('Outfit image used for reference')
    cols[0].image(orig_garment_image)
    cols[1].write('Base Image(from prod)')
    cols[1].image(base_image)
    cols[2].write('Tryon Image(target)')
    cols[2].image(tryon_image)
    cols[3].write('Outfit Image')
    cols[3].image(garment_image)

    st.divider()