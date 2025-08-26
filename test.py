import streamlit as st
from PIL import Image
import os

st.set_page_config(layout='wide')
root_path = '/Users/yaswanth/Downloads/combined_images_output_fill_V5'

# selected_cat = st.selectbox('category',[None, 'fullbody', 'upperbody'])

# if selected_cat:
for i in os.listdir(f"{root_path}/"):
    if i.startswith('.'):
        continue
    img1 = Image.open(f'{root_path}//{i}/cropped_garment.jpg')
    img2 = Image.open(f'{root_path}//{i}/reference_compiler_upscaled.jpg')
    img3 = Image.open(f'{root_path}//{i}/output.jpg')

    cols = st.columns(3)
    cols[0].write('garment')
    cols[0].image(img1)
    cols[1].write('reference')
    cols[1].image(img2)
    cols[2].write('output')
    cols[2].image(img3)
    st.divider()