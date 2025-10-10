import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

alphabake_results_path = "alphabake_results"
google_old_results_path = "fin_set_results"
google_new_results_path = "fin_set_results_V3"

base_images_path = "base_images_fin_optimized"
garments_path = "final_testset_garments"

all_cats = [None]+[i for i in os.listdir(f'{google_new_results_path}') if not i.startswith('.')]
selected_cat = st.selectbox('Category', all_cats)
# all_files = [i for i in os.listdir(f'{alphabake_results_path}') if not i.startswith('.')]

if selected_cat:
    for ind_file in os.listdir(f'{google_new_results_path}/{selected_cat}'):
        base_image_name = "_".join(ind_file.split('_',2)[:2])
        garment_image_name = ind_file.split('_',2)[-1]
        cols = st.columns(5)
        base_image = Image.open(f'{base_images_path}/{base_image_name}.png')
        cols[0].write('base image')
        cols[0].image(base_image)
        garment_image = Image.open(f'{garments_path}/{selected_cat.replace("_rmbg","")}/{garment_image_name}')
        cols[1].write('garment image')
        cols[1].image(garment_image)
        if os.path.exists(f'{alphabake_results_path}/{base_image_name}.png_base_image_{garment_image_name.replace(".webp",".jpg").replace(".png",".jpg")}'):
            alphabake_image = Image.open(f'{alphabake_results_path}/{base_image_name}.png_base_image_{garment_image_name.replace(".webp",".jpg").replace(".png",".jpg")}')
            cols[2].write('alphabake image')
            cols[2].image(alphabake_image)
        else:
            cols[2].write('alphabake image not found')

        if os.path.exists(f'{google_old_results_path}/{selected_cat.replace("_rmbg","").replace("dress","dresses")}/{ind_file}'):
            google_old_image = Image.open(f'{google_old_results_path}/{selected_cat.replace("_rmbg","").replace("dress","dresses")}/{ind_file}')
            cols[3].write('google old image')
            cols[3].image(google_old_image)
        else:
            cols[3].write('google old image not found')

        # if os.path.exists(f'{google_new_results_path}/{selected_cat}/{ind_file}'):
        # cols[3].write('google old image')
        # cols[3].image(google_old_image)
        google_new_image = Image.open(f'{google_new_results_path}/{selected_cat}/{ind_file}')
        cols[4].write('google new image')
        cols[4].image(google_new_image)
        
        st.divider()