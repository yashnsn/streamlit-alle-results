import streamlit as st
import os
from PIL import Image
import json

st.set_page_config(layout='wide')

root_path = "/Users/yaswanth/repositories/prog_content/prog_content_testset_diverse_set_output_fin_upscaled"
all_cats = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.isdir(f'{root_path}/{i}')]
all_cats = [None] + all_cats
selected_cat = st.selectbox("Select category", all_cats)

if selected_cat:
    # st.write(os.listdir(f'{root_path}/{selected_cat}'))
    all_folders = [i for i in os.listdir(f'{root_path}/{selected_cat}') if not i.startswith('.') and os.path.exists(f'{root_path}/{selected_cat}/{i}/garment_upscaled.jpg') and os.path.exists(f'{root_path}/{selected_cat}/{i}/reference.jpg') and os.path.exists(f'{root_path}/{selected_cat}/{i}/output_turbo.png')]
    st.markdown(f"**Found {len(all_folders)} examples in category {selected_cat}**")
    for ind_folder in all_folders:
        garment_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/garment.jpg')
        upscaled_garment_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/garment_upscaled.jpg')
        cropped_garment_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/cropped_garment.jpg')
        pin_ref_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/reference.jpg')
        masked_pin_ref_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/reference_altered.jpg')
        gen_img = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/output_turbo.png')
        gen_img_rerun = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/output_turbo_rerun_1.png')
        gen_img_upscaled = Image.open(f'{root_path}/{selected_cat}/{ind_folder}/output_turbo_V2.png')
        with open(f'{root_path}/{selected_cat}/{ind_folder}/metadata.json', 'r') as f:
            meta = json.load(f)

        # st.markdown(f"**{ind_folder} - {meta['category']}**")
        st.markdown(f'**{ind_folder}**')
        st.markdown(f"**Prompt: {meta['image_generation_prompt']}**")
        cols = st.columns(8)
        cols[0].write('garment image')
        cols[0].image(garment_img)
        cols[1].write('garment image(upscaled)')
        cols[1].image(upscaled_garment_img)
        cols[2].write('cropped garment image')
        cols[2].image(cropped_garment_img)
        cols[3].write('pin reference image')
        cols[3].image(pin_ref_img)
        cols[4].write('masked pin reference image')
        cols[4].image(masked_pin_ref_img)
        cols[5].write('generated image')
        cols[5].image(gen_img)
        cols[6].write('generated image')
        cols[6].image(gen_img_rerun)
        cols[7].write('generated image(with garment upscaling)')
        cols[7].image(gen_img_upscaled)

        st.divider()
# all_folders = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.exists(f'{root_path}/{i}/garment.jpg') and os.path.exists(f'{root_path}/{i}/reference.jpg') and os.path.exists(f'{root_path}/{i}/generated_image.jpg') and os.path.exists(f'{root_path}/{i}/meta.json')]