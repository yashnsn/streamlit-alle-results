import streamlit as st
from PIL import Image
import os
import json

st.set_page_config(layout="wide")
root_path = "prog_content"
color_switching_res_path = os.path.join(root_path, "color_switching")
segmentation_res_path = os.path.join(root_path, "segmentation_masks")

all_categories = [None]
all_categories += [i for i in list(os.listdir(color_switching_res_path)) if not i.startswith(".")]

selected_category = st.selectbox("Select a category", all_categories)
# selected_category = 'dress'
if selected_category:
    all_files = [i for i in os.listdir(os.path.join(color_switching_res_path, selected_category)) if os.path.exists(os.path.join(segmentation_res_path, selected_category, i, "output.png"))]
    # print(os.path.join(segmentation_res_path, selected_category, os.listdir(os.path.join(color_switching_res_path, selected_category))[0], "output.png"))
    for ind_file in all_files:
        garment_image = Image.open(os.path.join(color_switching_res_path, selected_category, ind_file, "garment.jpg"))
        cropped_garment_image = Image.open(os.path.join(color_switching_res_path, selected_category, ind_file, "cropped_garment.jpg"))
        reference_image = Image.open(os.path.join(color_switching_res_path, selected_category, ind_file, "reference.jpg"))
        altered_reference_image = Image.open(os.path.join(color_switching_res_path, selected_category, ind_file, "reference_altered.jpg"))
        color_result = Image.open(os.path.join(color_switching_res_path, selected_category, ind_file, "output.png"))

        masked_reference_image = Image.open(os.path.join(segmentation_res_path, selected_category, ind_file, "reference_altered.jpg"))
        segmantation_result = Image.open(os.path.join(segmentation_res_path, selected_category, ind_file, "output.png"))
        cols = st.columns(7)

        cols[0].write("Garment")
        cols[0].image(garment_image)
        cols[1].write("Cropped Garment")
        cols[1].image(cropped_garment_image)
        cols[2].write("Reference")
        cols[2].image(reference_image)
        cols[3].write("Altered Reference")
        cols[3].image(altered_reference_image)
        cols[4].write("Masked Reference")
        cols[4].image(masked_reference_image)
        cols[5].write("Results(color change)")
        cols[5].image(color_result)
        cols[6].write("Results(segmentation mask)")
        cols[6].image(segmantation_result)

        metadata = json.load(open(os.path.join(color_switching_res_path, selected_category, ind_file, "metadata.json")))
        st.write("Metadata")
        st.json(metadata, expanded=True)
        

        st.divider()
        # break
