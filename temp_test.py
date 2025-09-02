import streamlit as st
import os

st.set_page_config(layout='wide')
from PIL import Image

root_path = "/Users/yaswanth/repositories/prog_content/prog_content_testset/Shirt"
all_files = [i for i in os.listdir(root_path) if not i.startswith('.') and i.endswith('.jpg')]

for ind_file in all_files:
    img = Image.open(f'{root_path}/{ind_file}')
    st.markdown(f"**{ind_file}**")
    st.image(img)
    st.divider()

["vto_image_20250828_122320","vto_image_20250829_082844","vto_image_20250829_082927"]
["vto_image_20250829_023330","vto_image_20250829_024701"]