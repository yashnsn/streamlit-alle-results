import streamlit as st
from PIL import Image
import os
import json

st.set_page_config(layout="wide")

root_path = "test_dataset_V2_output_V8/pant"

for ind_folder in os.listdir(root_path):
    if not os.path.exists(os.path.join(root_path, ind_folder, "output.png")):
        continue
    cols = st.columns(5)
    garment_image = Image.open(os.path.join(root_path, ind_folder, "garment.jpg"))
    cropped_garment_image = Image.open(os.path.join(root_path, ind_folder, "cropped_garment.jpg"))
    reference_image = Image.open(os.path.join(root_path, ind_folder, "reference_altered.jpg"))
    metadata = json.load(open(os.path.join(root_path, ind_folder, "metadata.json")))
    output = Image.open(os.path.join(root_path, ind_folder, "output.png"))
    cols[0].write("Garment")
    cols[0].image(garment_image)
    cols[1].write("Cropped Garment")
    cols[1].image(cropped_garment_image)
    cols[2].write("Reference")
    cols[2].image(reference_image)
    with cols[3]:
        st.write('Metadata')
        st.json(metadata, expanded=True)
    cols[4].write("Output")
    cols[4].image(output)
    st.divider()