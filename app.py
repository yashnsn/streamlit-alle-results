import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Custom Attention Flux", layout="wide")
character_path_mapper = {'isha':('base_images/isha.jpeg','results/results_isha_test_run_V19_value_attn_weights'), 'stuti':('base_images/stuti_3.jpeg','results/results_stuti_test_run_V19_value_attn_weights'),'rhea':('base_images/rhea.png','results/results_rhea_test_run_V19_value_attn_weights')}
garment_images_path = 'garments/outfits_final_test'
all_people = [None]
all_people += list(character_path_mapper.keys())
person = st.selectbox('Person',all_people)

if person is not None:
    base_image_path, try_on_results_path = character_path_mapper[person]
    base_image = Image.open(base_image_path)

    all_tryon_images = []
    all_garment_images = []
    all_image_names = list(os.listdir(try_on_results_path))
    all_image_names.sort()
    for ind_result in all_image_names:
        all_tryon_images.append(Image.open(f'{try_on_results_path}/{ind_result}'))
        all_garment_images.append(Image.open(f'{garment_images_path}/{ind_result}'))

    for image_name, tryon_image, garment_image in zip(all_image_names, all_tryon_images, all_garment_images):
        st.write(f'File name: {image_name}')
        cols = st.columns(3)
        
        
        with cols[0]:
            st.write('base image')
            st.image(base_image, use_container_width=True)
        with cols[1]:
            st.write('try on result')
            st.image(tryon_image, use_container_width=True)
        with cols[2]:
            st.write('garment image')
            st.image(garment_image, use_container_width=True)
        st.divider()