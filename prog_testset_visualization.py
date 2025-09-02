import streamlit as st
import os
from PIL import Image
import json

st.set_page_config(layout='wide')

root_path = "prog_content_testset_diverse_set_output_fin"
all_cats = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.isdir(f'{root_path}/{i}')]
all_cats = [None] + all_cats
selected_cat = st.selectbox("Select category", all_cats)

if selected_cat:
    # st.write(os.listdir(f'{root_path}/{selected_cat}'))
    all_folders = [i for i in os.listdir(f'{root_path}/{selected_cat}') if not i.startswith('.') and os.path.exists(f'{root_path}/{selected_cat}/{i}/garment.jpg') and os.path.exists(f'{root_path}/{selected_cat}/{i}/reference.jpg') and os.path.exists(f'{root_path}/{selected_cat}/{i}/output_turbo.png')]
    st.markdown(f"**Found {len(all_folders)} examples in category {selected_cat}**")
    for ind_folder in all_folders:
        garment_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/garment.jpg')
        cropped_garment_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/cropped_garment.jpg')
        pin_ref_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/reference.jpg')
        masked_pin_ref_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/reference_altered.jpg')
        gen_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/output_turbo_grained.png')
        with open(f'{root_path}/{selected_cat}/{ind_folder}/metadata.json', 'r') as f:
            meta = json.load(f)

        # st.markdown(f"**{ind_folder} - {meta['category']}**")
        st.markdown(f'**{ind_folder}**')
        st.markdown(f"**Prompt: {meta['image_generation_prompt']}**")
        cols = st.columns(5)
        cols[0].write('garment image')
        cols[0].image(garment_img)
        cols[1].write('cropped garment image')
        cols[1].image(cropped_garment_img)
        cols[2].write('pin reference image')
        cols[2].image(pin_ref_img)
        cols[3].write('masked pin reference image')
        cols[3].image(masked_pin_ref_img)
        cols[4].write('generated image')
        cols[4].image(gen_img)

        st.divider()
# all_folders = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.exists(f'{root_path}/{i}/garment.jpg') and os.path.exists(f'{root_path}/{i}/reference.jpg') and os.path.exists(f'{root_path}/{i}/generated_image.jpg') and os.path.exists(f'{root_path}/{i}/meta.json')]