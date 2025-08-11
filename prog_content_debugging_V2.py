import streamlit as st
import os
from PIL import Image
import json

st.set_page_config(page_title="Prog Content Debugging", page_icon=":chart_with_upwards_trend:", layout="wide")
root_path = "./prog_content_debugging_4"
all_files = os.listdir(root_path)
all_files.sort()

metadata = json.load(open("prog_content_debugging_4/metadata.json"))

all_errors = [i['Issues'] for i in metadata.values()]
all_errors = list(set(all_errors))

error_col = st.selectbox("Select Error", all_errors)

all_selected_rows = [i for i in metadata.keys() if metadata[i]['Issues'] == error_col]

for idx in all_selected_rows:
    if not os.path.exists(os.path.join(root_path, f"{int(idx):03d}", "reference_altered.jpg")):
        continue
    
    garment_image = Image.open(os.path.join(root_path, f"{int(idx):03d}", "garment.jpg"))
    cropped_garment_image = Image.open(os.path.join(root_path, f"{int(idx):03d}", "cropped_garment.jpg"))
    reference_image = Image.open(os.path.join(root_path, f"{int(idx):03d}", "reference_altered.jpg"))
    gen_image = Image.open(os.path.join(root_path, f"{int(idx):03d}", "output.png"))
    old_gen_image = Image.open(os.path.join(root_path, f"{int(idx):03d}", "output_original.jpg"))
    gen_prompted = json.load(open(os.path.join(root_path, f"{int(idx):03d}", "metadata.json")))

    metadata[idx]['image_generation_prompt'] = gen_prompted['image_generation_prompt']
    cols = st.columns(6)

    with cols[0]:
        st.write("Garment Image")
        st.image(garment_image)
    with cols[1]:
        st.write("Cropped Garment Image")
        st.image(cropped_garment_image)
    with cols[2]:
        st.write("Reference Image")
        st.image(reference_image)
    with cols[3]:
        st.write("Old Gen Image")
        st.image(old_gen_image)
    with cols[4]:
        st.write("New Gen Image")
        st.image(gen_image)
    with cols[5]:
        st.write("Metadata")
        st.write(metadata[idx])
        
        # st.write(metadata[idx])
    st.write("---")