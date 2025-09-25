from PIL import Image
import streamlit as st
import os

st.set_page_config(layout='wide')

base_image_path = "base_images_fin_optimized"
garments = "final_testset_garments"
results = "final_testset_garments_results"

base_images = [i for i in os.listdir(results) if not i.startswith('.')]
base_images.sort()
base_images = [None]+base_images
selected_base_image = st.selectbox('Base image', base_images)

category = [None, 'dress','skirts','shirts','t_shirts']
selected_cat = st.selectbox('Category', category)

if selected_base_image and selected_cat:
    base_image = Image.open(f'{base_image_path}/{selected_base_image}.png')
    for ind_garment_img in os.listdir(f'{results}/{selected_base_image}/{selected_cat}'):
        if ind_garment_img.startswith('.'):
            continue
        garment_img = Image.open(f'{garments}/{selected_cat}/{ind_garment_img}')
        result_img = Image.open(f'{results}/{selected_base_image}/{selected_cat}/{ind_garment_img}')

        cols = st.columns(3)

        cols[0].write('base image')
        cols[0].image(base_image)
        cols[1].write('garment image')
        cols[1].image(garment_img)
        cols[2].write('Result image')
        cols[2].image(result_img)