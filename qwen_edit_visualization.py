from PIL import Image
import streamlit as st
import os

st.set_page_config(layout='wide')

base_image_path = "base_images_fin_optimized"
garments = "final_testset_garments"
# old_results = "final_testset_garments_results_V7"
new_results = "final_testset_garments_results_V15_lora"
alphabake_results_path = "alphabake_results"

base_images = [i for i in os.listdir(new_results) if not i.startswith('.')]
base_images.sort()
base_images = [None]+base_images
selected_base_image = st.selectbox('Base image', base_images)

category = [None, 'dress','skirts','shirts','t_shirts']
selected_cat = st.selectbox('Category', category)

if selected_base_image and selected_cat:
    base_image = Image.open(f'{base_image_path}/{selected_base_image}.png')
    for ind_garment_img in os.listdir(f'{new_results}/{selected_base_image}/{selected_cat}'):
        if ind_garment_img.startswith('.') or ind_garment_img.endswith('.json') or 'processed' in ind_garment_img:
            continue
        if not os.path.exists(f'{alphabake_results_path}/{selected_base_image}.png_base_image_{ind_garment_img.replace(".webp",".jpg").replace(".png",".jpg")}'):
            continue
        garment_img = Image.open(f'{garments}/{selected_cat}/{ind_garment_img}')
        # old_result_img = Image.open(f'{old_results}/{selected_base_image}/{selected_cat}/{ind_garment_img}')
        alphabake_result_img = Image.open(f'{alphabake_results_path}/{selected_base_image}.png_base_image_{ind_garment_img.replace(".webp",".jpg").replace(".png",".jpg")}')
        new_result_img = Image.open(f'{new_results}/{selected_base_image}/{selected_cat}/{ind_garment_img}')

        cols = st.columns(4)

        cols[0].write('base image')
        cols[0].image(base_image)
        cols[1].write('garment image')
        cols[1].image(garment_img)
        cols[2].write('Alphabake result')
        cols[2].image(alphabake_result_img)
        cols[3].write('Result image(w lora)')
        cols[3].image(new_result_img)