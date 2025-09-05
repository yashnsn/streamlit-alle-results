import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

root_path = "Top"

all_files = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.exists(f'{root_path}/{i}/output_tryon.png')]

for ind_file in all_files:
    garment_img = Image.open(f'{root_path}/{ind_file}/garment_upscaled.jpg')
    garment_img_cropped = Image.open(f'{root_path}/{ind_file}/garment_upscaled_cropped.jpg')
    pin_ref_img = Image.open(f'{root_path}/{ind_file}/reference_upscaled.jpg')
    pin_ref_mask = Image.open(f'{root_path}/{ind_file}/reference_upscaled_mask_expanded.jpg')
    gen_img = Image.open(f'{root_path}/{ind_file}/output_cropped_tryon.png')

    st.markdown(f'**{ind_file}**')
    cols = st.columns(5)
    cols[0].write('garment image(upscaled)')
    cols[0].image(garment_img)
    cols[1].write('garment image(upscaled)')
    cols[1].image(garment_img)
    cols[2].write('pin reference image(upscaled)')
    cols[2].image(pin_ref_img)
    cols[3].write('masked pin reference image(upscaled)')
    cols[3].image(pin_ref_mask)
    cols[4].write('generated image')
    cols[4].image(gen_img)
    st.divider()