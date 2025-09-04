import streamlit as st
import os
from PIL import Image
import json

src_root_path = "combined_images_output_V6_prod"
src_dev_path = "combined_images_output_V3"

st.set_page_config(layout='wide')
st.title("Development vs Production")

cats = [None,'fullbody','upperbody']

selected_cat = st.selectbox("Select category", cats)
if selected_cat:
    root_path = os.path.join(src_root_path, selected_cat)
    dev_path = os.path.join(src_dev_path, selected_cat)
    all_folders = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.exists(os.path.join(root_path, i, 'generated_image.jpg'))]
    
    for ind_folder in all_folders:
        flag = os.path.exists(os.path.join(dev_path, ind_folder, 'reference_compiler_upscaled.jpg')) and os.path.exists(os.path.join(root_path, ind_folder, 'upscaled_reference.jpg')) and os.path.exists(os.path.join(dev_path, ind_folder, 'cropped_garment.jpg')) and os.path.exists(os.path.join(root_path, ind_folder, 'cropped_garment.jpg')) and os.path.exists(os.path.join(dev_path, ind_folder, 'reference_altered.jpg')) and os.path.exists(os.path.join(root_path, ind_folder, 'upscaled_reference_masked.jpg')) and os.path.exists(os.path.join(dev_path, ind_folder, 'metadata.json')) and os.path.exists(os.path.join(root_path, ind_folder, 'metadata.json')) and os.path.exists(os.path.join(dev_path, ind_folder, 'garment.jpg')) and os.path.exists(os.path.join(dev_path, ind_folder, 'reference.jpg')) and os.path.exists(os.path.join(dev_path, ind_folder, 'output_turbo.png'))
        if not flag:
            continue
        dev_ref_upscaled = Image.open(os.path.join(dev_path, ind_folder, 'reference_compiler_upscaled.jpg'))
        prod_ref_upscaled = Image.open(os.path.join(root_path, ind_folder, 'upscaled_reference.jpg'))

        dev_cropped_garment = Image.open(os.path.join(dev_path, ind_folder, 'cropped_garment.jpg'))
        prod_cropped_garment = Image.open(os.path.join(root_path, ind_folder, 'cropped_garment.jpg'))

        dev_ref_masked = Image.open(os.path.join(dev_path, ind_folder, 'reference_altered.jpg'))
        prod_ref_masked = Image.open(os.path.join(root_path, ind_folder, 'upscaled_reference_masked.jpg'))

        dev_metadata = json.load(open(os.path.join(dev_path, ind_folder, 'metadata.json')))
        prod_metadata = json.load(open(os.path.join(root_path, ind_folder, 'metadata.json')))

        garment_image = Image.open(os.path.join(dev_path, ind_folder, 'garment.jpg'))
        reference_image = Image.open(os.path.join(dev_path, ind_folder, 'reference.jpg'))

        dev_output = Image.open(os.path.join(dev_path, ind_folder, 'output_turbo.png'))
        prod_output = Image.open(os.path.join(root_path, ind_folder, 'generated_image.jpg'))

        st.markdown(f'**{ind_folder}**')
        st.write('dev prompt')
        st.write(dev_metadata['image_generation_prompt'])
        st.write('prod prompt')
        st.write(prod_metadata['image_generation_prompt'])
        cols = st.columns(6)

        cols[0].write('Garment Image')
        cols[0].image(garment_image)
        cols[0].write('Reference Image')
        cols[0].image(reference_image)
        cols[1].write('Dev cropped garment')
        cols[1].image(dev_cropped_garment)
        cols[1].write('Prod cropped garment')
        cols[1].image(prod_cropped_garment)
        cols[2].write('Dev upscaled reference')
        cols[2].image(dev_ref_upscaled)
        cols[2].write('Prod upscaled reference')
        cols[2].image(prod_ref_upscaled)
        cols[3].write('Dev masked reference')
        cols[3].image(dev_ref_masked)
        cols[3].write('Prod masked reference')
        cols[3].image(prod_ref_masked)
        cols[4].write('Dev generated image')
        cols[4].image(dev_output)
        cols[5].write('Prod generated image')
        cols[5].image(prod_output)

        st.divider()