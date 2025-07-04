import os
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("Alphabake Results")



root_dir = "./alphabake_final_test_results/tryons"
garment_dir = "./alphabake_final_test_results/garments"
human_dir = "./alphabake_final_test_results/base_images"

people = os.listdir(root_dir)
people.append(None)
all_rows = []
person = st.selectbox("Select a person", people, index=len(people)-1)
# for person in people:
if person is not None:
    for garment_name in os.listdir(os.path.join(root_dir, person, 'base_image_1')):
        ind_row = []
        for base_image_idx in range(1, 4):
            try:
                ind_row.append(Image.open(os.path.join(human_dir, f'{person}_base_image_base_image_{base_image_idx}.png')))
                ind_row.append(Image.open(os.path.join(root_dir, person, f'base_image_{base_image_idx}', garment_name)))
            except:
                print(f'{person} {garment_name} {base_image_idx} not found')
        ind_row.append(Image.open(os.path.join(garment_dir, garment_name)))
        all_rows.append(ind_row)

    for row in all_rows:
        for i in range(3):
            cols = st.columns(3)
            cols[0].image(row[2*i])
            cols[1].image(row[2*i+1])
            cols[2].image(row[-1])
            st.divider()

    # st.divider()