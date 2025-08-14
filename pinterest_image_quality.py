import streamlit as st
import os
import json
from PIL import Image
import pandas as pd

st.set_page_config(page_title="Pinterest Image Quality", page_icon=":chart_with_upwards_trend:", layout="wide")

res_path = "./pinterest_base_image_gen_V7"
src_path = "pinterest_images_V2"
all_files = os.listdir(src_path)
all_files.sort()

all_images = [i for i in all_files if i.endswith(".jpg") or i.endswith(".png")]
# df = pd.read_csv("image_quality_scores (1).csv")
# mapper = {}
# for ind_row in df.iloc(0):
#     mapper[ind_row["image"].split('/')[-1]] = ind_row["brisque_score"]

for ind_image in all_images:
    if not os.path.exists(os.path.join(res_path, f"{ind_image[:-4]}.json")):
        continue
    
    metadata = json.load(open(os.path.join(res_path, f"{ind_image[:-4]}.json")))
    st.markdown(f'file name: {ind_image}\n\n score: {metadata["brisque_score"]:.02f}\n\n width: {metadata["width"]}, height: {metadata["height"]}\n\n time taken: {metadata["refining_time"]+metadata["upscaling_time"]:.02f} seconds')
    image = Image.open(os.path.join(src_path, ind_image))
    # res_image1 = Image.open(os.path.join(res_path, f"{ind_image[:-4]}_refined.jpg"))
    res_image2 = Image.open(os.path.join(res_path, f"{ind_image[:-4]}_upscaled.jpg"))
    res_image3 = Image.open(os.path.join(res_path, f"{ind_image[:-4]}_upscaled_refined.jpg"))

    cols = st.columns(4)

    with cols[0]:
        st.write("Original Image")
        st.image(image)
    with cols[1]:
        st.write("Upscaled Image")
        st.image(res_image2)
    with cols[2]:
        st.write("Upscaled Refined Image")
        st.image(res_image3)

    st.divider()