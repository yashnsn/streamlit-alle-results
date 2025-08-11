import streamlit as st
import os
from PIL import Image

cats = {"dress":"prog_content/wan21_dress_nopinterest","shirt":"prog_content/shirt_V4_uncropped_garment_unreferenced"}
runway_res_path = "prog_content/segmentation_masks"
all_cats = [None] + list(cats.keys())

st.set_page_config(page_title="No Pin Reference", page_icon=":chart_with_upwards_trend:", layout="wide")

st.title("No Pin Reference")

cat = st.selectbox("Select Category", all_cats)

if cat is not None:
    all_files = os.listdir(cats[cat])
    for file in all_files:
        if file.endswith("."):
            continue

        garment_path = os.path.join(cats[cat], file, "cropped_garment.png")
        pinterst_path = os.path.join(f"{runway_res_path}/{cat}", file, "reference.jpg")
        garment_img = Image.open(garment_path)
        reference_img = Image.open(pinterst_path)

        gen1_image = Image.open(os.path.join(cats[cat], file, "output_saturation_contrast_corrected.jpg"))
        gen2_image = Image.open(os.path.join(f"{runway_res_path}/{cat}", file, "output.png"))

        cols = st.columns(4)
        with cols[0]:
            st.write("Garment")
            st.image(garment_img)
        with cols[1]:
            st.write("Reference")
            st.image(reference_img)
        with cols[2]:
            st.write("Wan generated")
            st.image(gen1_image)
        with cols[3]:
            st.write("Runway generated")
            st.image(gen2_image)
        st.write("---")