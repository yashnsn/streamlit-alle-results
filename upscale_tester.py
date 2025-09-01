import streamlit as st
import os
from PIL import Image

root_path = '/Users/yaswanth/Downloads/combined images_upscaled_test_res_wh_V0'
supp_path = '/Users/yaswanth/Downloads/combined images_upscaled_test_res_wh_V1'
st.set_page_config(layout='wide')
all_folders = [i for i in os.listdir(f"{root_path}/") if not i.startswith('.')]
all_folders.sort()

for ind_folder in all_folders:
    if not os.path.exists(f'{supp_path}/{ind_folder}/reference_upscaled.jpg') or not os.path.exists(f'{root_path}/{ind_folder}/reference_upscaled.jpg'):
        continue
    ref_img = Image.open(f'{root_path}/{ind_folder}/reference.jpg')
    img1 = Image.open(f'{root_path}/{ind_folder}/reference_upscaled.jpg')
    img2 = Image.open(f'{supp_path}/{ind_folder}/reference_upscaled.jpg')

    cols = st.columns(3)
    cols[0].write('reference')
    cols[0].image(ref_img)
    cols[1].write('upscaled - 1024x1024')
    cols[1].image(img1)
    cols[2].write('upscaled_supp - 768x1344')
    cols[2].image(img2)
    st.divider()