import streamlit as st
import os
from PIL import Image
import json

st.set_page_config(layout='wide')

src_root_path = "prog_content_testset_sampled"
# supp_path = "/Users/yaswanth/repositories/prog_content/prog_content_testset_sampled/Jeans"
seleceted_cat = st.selectbox("Select category", [None] + [i for i in os.listdir(src_root_path) if not i.startswith('.') and os.path.isdir(f'{src_root_path}/{i}')])
if seleceted_cat:
    root_path = f"{src_root_path}/{seleceted_cat}"

    for ind_folder in os.listdir(root_path):
        
        if ind_folder.startswith('.'):
            continue
        st.write(ind_folder)
        garment_img = Image.open(f'{root_path}/{ind_folder}/garment_cropped_upscaled.jpg')
        pin_ref_img = Image.open(f'{root_path}/{ind_folder}/reference.jpg')
        gen_img = Image.open(f'{root_path}/{ind_folder}/output_seedream.png')
        gen_img_using_upscaled = Image.open(f'{root_path}/{ind_folder}/output_seedream_upscaled_garment.png')
        gen_img_V2 = Image.open(f'{root_path}/{ind_folder}/output_text_desc_redux_switch_5_mask_V5.jpg')
        prompt = json.load(open(f'{root_path}/{ind_folder}/generation_prompt_seedream.json'))
        st.write(prompt)
        cols = st.columns(5)
        cols[0].write('garment image(upscaled)')
        cols[0].image(garment_img)
        cols[1].write('pin reference image(upscaled)')
        cols[1].image(pin_ref_img)
        cols[2].write('generated image(prog)')
        cols[2].image(gen_img_V2)
        cols[3].write('generated image(seedream)')
        cols[3].image(gen_img)
        cols[4].write('generated image(seedream, using upscaled garment)')
        cols[4].image(gen_img_using_upscaled)
        
        # cols[4].write('prompt')
        # cols[4].write(prompt['image_generation_prompt'])
        st.divider()