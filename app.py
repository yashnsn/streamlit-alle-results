import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Custom Attention Flux", layout="wide")
character_path_mapper = {'isha':('base_images/isha.jpeg','results/results_isha_prod_run_V0','results/isha'), 'stuti':('base_images/stuti_3.jpeg','results/results_stuti_prod_run_V0','results/stuti'),'rhea':('base_images/rhea.png','results/results_rhea_prod_run_V0','results/rhea')}
garment_images_path = 'garments/final_test_images'
all_people = [None]
all_people += list(character_path_mapper.keys())
person = st.selectbox('Person',all_people)

if person is not None:
    base_image_path, try_on_results_path, prod_results_path = character_path_mapper[person]
    base_image = Image.open(base_image_path)

    all_tryon_images = []
    all_garment_images = []
    all_prod_results = []
    all_image_names = [i for i in os.listdir(try_on_results_path) if not i.startswith('.')]
    all_image_names.sort()
    for ind_result in all_image_names:
        all_tryon_images.append(Image.open(f'{try_on_results_path}/{ind_result}'))
        all_garment_images.append(Image.open(f'{garment_images_path}/{ind_result}'))
        all_prod_results.append(Image.open(f'{prod_results_path}/{ind_result}'))

    for image_name, tryon_image, garment_image, prod_result in zip(all_image_names, all_tryon_images, all_garment_images, all_prod_results):
        st.write(f'File name: {image_name}')
        cols = st.columns(4)
        
        
        with cols[0]:
            st.write('base image')
            st.image(base_image, use_container_width=True)
        with cols[1]:
            st.write('try on result')
            st.image(tryon_image, use_container_width=True)
        with cols[2]:
            st.write('prod result')
            st.image(prod_result, use_container_width=True)
        with cols[3]:
            st.write('garment image')
            st.image(garment_image, use_container_width=True)
        
        st.divider()