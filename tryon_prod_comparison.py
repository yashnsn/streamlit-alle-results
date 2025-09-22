import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

root_path = "old_data/multi-threaded-test_V17"
prod_results = "/Users/yaswanth/repositories/tryon_production/alphabake_prod_results"

all_files = [i for i in os.listdir(f"{prod_results}") if not i.startswith('.')]

for ind_file in all_files:
    garment_img = Image.open(f'{root_path}/garment/{ind_file}')
    human_img = Image.open(f'{root_path}/human/{ind_file}')
    tryon_res = Image.open(f'{root_path}/tryon/{ind_file}')
    tryon_prod_res = Image.open(f'{prod_results}/{ind_file}')

    cols = st.columns(4)

    cols[0].write('Garment image')
    cols[0].image(garment_img)
    cols[1].write('Base Image')
    cols[1].image(human_img)
    cols[2].write('Tryon(old)')
    cols[2].image(tryon_res)
    cols[3].write('Tryon(prod)')
    cols[3].image(tryon_prod_res)

    st.divider()