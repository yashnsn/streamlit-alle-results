import streamlit as st
from PIL import Image
import os

st.set_page_config(layout='wide')

root_path = "multi-threaded-test_V13"
root_path_resized = "multi-threaded-test_V14"

all_files = [i for i in os.listdir(f'{root_path}/tryon') if not i.startswith('.')]
all_files.sort()

for ind_file in all_files:
    garment_img = Image.open(f'{root_path}/garment/{ind_file}')
    base_img = Image.open(f'{root_path}/human/{ind_file}')
    base_img_resized = Image.open(f'{root_path_resized}/human/{ind_file}')

    tryon = Image.open(f'{root_path}/tryon/{ind_file}')
    tryon_resized = Image.open(f'{root_path_resized}/tryon/{ind_file}')

    cols = st.columns(5)

    cols[0].write('garment image')
    cols[0].image(garment_img)
    cols[1].write('base image(orig)')
    cols[1].image(base_img)
    cols[2].write('base image(downsampled)')
    cols[2].image(base_img_resized)
    cols[3].write('tryon result(orig)')
    cols[3].image(tryon)
    cols[4].write('tryon result(downsampled base image)')
    cols[4].image(tryon_resized)

    st.divider()


