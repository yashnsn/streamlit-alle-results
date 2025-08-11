import streamlit as st
from PIL import Image
import os
import json

st.set_page_config(page_title="Prog Content Debugging", page_icon=":chart_with_upwards_trend:", layout="wide")
st.title("Prog Content Debugging")

root_path = "/Users/yaswanth/repositories/prog_content/prog_content_debugging_2"

for ind_folders in os.listdir(root_path):
    if ind_folders.startswith('.'):
        continue
    
    data = json.load(open(os.path.join(root_path, ind_folders, "metadata.json")))
    garment_image = Image.open(os.path.join(root_path, ind_folders, "cropped_garment.jpg"))
    reference_image = Image.open(os.path.join(root_path, ind_folders, "reference.jpg"))
    gen_image = Image.open(os.path.join(root_path, ind_folders, "output_rerun.png"))
    old_gen_image = Image.open(os.path.join(root_path, ind_folders, "old_output.jpg"))


    cols = st.columns(5)
    with cols[0]:
        st.write(data["image_generation_prompt"])
    with cols[1]:
        st.image(garment_image)
    with cols[2]:
        st.image(reference_image)
    with cols[3]:
        st.image(gen_image)
    with cols[4]:
        st.image(old_gen_image)
    st.write("---")