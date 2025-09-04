import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

edges_files = ["stuti_0.png_base_image_917885_1001.jpg","isha_1.png_base_image_57486_1004.jpg","isha_1.png_base_image_177369_1001.jpg","isha_0.png_base_image_178888_1000.jpg","isha_1.png_base_image_176672_1000.jpg"]
jaw_distorition = ["stuti_0.png_base_image_170574_1001.jpg","isha_1.png_base_image_66778_1003.jpg","stuti_0.png_base_image_57486_1004.jpg"]
artifacts = ["stuti_1.png_base_image_57486_1004.jpg","suhani_1.png_base_image_93083_1000.jpg","stuti_1.png_base_image_2029702_1000.jpg","suhani_1.png_base_image_2029702_1000.jpg","isha_0.png_base_image_1344335_1001.jpg","suhani_1.png_base_image_1344335_1001.jpg","isha_0.png_base_image_176672_1000.jpg"]
garment_accuracy = ["isha_0.png_base_image_115898_1000.jpg","isha_1.png_base_image_74998_1008.jpg","isha_1.png_base_image_1158065_1002.jpg","stuti_0.png_base_image_1344564_1000.jpg"]
blurring_hands = ["isha_0.png_base_image_1290761_1004.jpg","isha_0.png_base_image_802897_1001.jpg","isha_0.png_base_image_66778_1003.jpg","isha_0.png_base_image_1356755_1000.jpg"]
# files = ["isha_0.png_base_image_1290761_1004.jpg","isha_0.png_base_image_802897_1001.jpg","isha_0.png_base_image_66778_1003.jpg","isha_0.png_base_image_1356755_1000.jpg","stuti_1.png_base_image_57486_1004.jpg","suhani_1.png_base_image_93083_1000.jpg","stuti_1.png_base_image_2029702_1000.jpg","suhani_1.png_base_image_2029702_1000.jpg","isha_0.png_base_image_1344335_1001.jpg","suhani_1.png_base_image_1344335_1001.jpg","isha_0.png_base_image_176672_1000.jpg"]

# src_fir = "outputs/multi-threaded-test_V16"
src_fir = "multi-threaded-test_V17_alphabake_fix"
# os.makedirs(dest_path, exist_ok=True)
mapper = {
    "edges_files": edges_files,
    "jaw_distorition": jaw_distorition,
    "artifacts": artifacts,
    "garment_accuracy": garment_accuracy,
    "blurring_hands": blurring_hands
}

selected_issue = st.selectbox("Select issue", list(mapper.keys()))

for ind_file in mapper[selected_issue]:
    src_folder = f'{src_fir}_{selected_issue}'
    base_img = Image.open(f'{src_folder}/human/{ind_file}')
    garment_img = Image.open(f'{src_folder}/garment/{ind_file}')
    tryon_img = Image.open(f'{src_folder}/tryon/{ind_file}.jpg')
    tryon_img_old = Image.open(f'{src_folder}/tryon_old/{ind_file}.jpg')
    tryon_retain_skin_false = Image.open(f'{src_folder}/tryon_retain_skin_false_lat/{ind_file}.jpg')

    st.markdown(f"**{ind_file}**")
    cols = st.columns(5)
    cols[0].write('base image')
    cols[0].image(base_img)
    cols[1].write('garment image')
    cols[1].image(garment_img)
    cols[2].write('tryon image (old)')
    cols[2].image(tryon_img_old)
    cols[3].write('tryon image (retain skin false)')
    cols[3].image(tryon_retain_skin_false)
    cols[4].write('tryon image (retain skin true)')
    cols[4].image(tryon_img)

    st.divider()