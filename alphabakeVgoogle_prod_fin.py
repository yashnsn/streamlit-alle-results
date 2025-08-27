import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

# base_images_path = "base_images_fin"
cats = [None]
cats += [i for i in os.listdir("fin_set_results") if not i.startswith('.')]
google_results_path = "fin_set_results"
alphabake_res_path = "multi-threaded-test_V16"

selected_cat = st.selectbox('category',cats)
# all_files = [i for i in os.listdir(f'{}')]
if selected_cat:
    all_results = list(os.listdir(f'{google_results_path}/{selected_cat}'))
    all_results.sort()
    for ind_res in all_results:
        if ind_res.startswith('.'):
            continue

        image_name = ind_res.split("_",2)[-1]
        base_img_name = f'{ind_res.split("_",2)[0]}_{ind_res.split("_",2)[1]}'

        
        fin_name = f'{base_img_name}.png_base_image_{image_name}'.replace('.webp','.jpg').replace('.jpeg','.jpg')
        if not os.path.exists(f'{alphabake_res_path}/human/{fin_name}'):
            continue
        base_img = Image.open(f'{alphabake_res_path}/human/{fin_name}')
        garment_img = Image.open(f'{alphabake_res_path}/garment/{fin_name}')
        
        tryon_img = Image.open(f'{alphabake_res_path}/tryon/{fin_name}')
        # google_tryon = Image.open(f'{google_results_path}/{selected_cat}/{ind_res}')

        st.write(fin_name)
        cols = st.columns(3)
        cols[0].write('base image')
        cols[0].image(base_img)
        cols[1].write('garment image')
        cols[1].image(garment_img)
        cols[2].write('alphabake tryon image')
        cols[2].image(tryon_img)
        # cols[3].write('google tryon image')
        # cols[3].image(google_tryon)
        st.divider()
