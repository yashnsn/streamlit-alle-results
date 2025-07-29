import os
from PIL import Image
import streamlit as st

st.set_page_config(layout="wide")
root_path = "/Users/yaswanth/repositories/pinterest_scrapper/final_mixed_dataset_hashed"

garments_path = f"{root_path}/garment_image"
outfit_path = f"{root_path}/outfit_images_resized"
human_path = f"{root_path}/human_images_cropped"

all_files = os.listdir(garments_path)

for ind_file in all_files:
    garment_image = Image.open(os.path.join(garments_path, ind_file))
    outfit_image = Image.open(os.path.join(outfit_path, ind_file))
    human_image = Image.open(os.path.join(human_path, ind_file.split('_')[0] + '.jpg'))
    st.write(ind_file)
    cols = st.columns(3)
    cols[0].write('Garment image')
    cols[1].write('Outfit image')
    cols[2].write('Human image')
    cols[0].image(garment_image, use_container_width=True)
    cols[1].image(outfit_image, use_container_width=True)
    cols[2].image(human_image, use_container_width=True)
    st.divider()