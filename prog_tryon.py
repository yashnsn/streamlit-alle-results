import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')

src_root_path = "prog_content_testset_sampled_fin"
all_cats = [i for i in os.listdir(src_root_path) if not i.startswith('.') and os.path.isdir(f'{src_root_path}/{i}')]
all_cats = [None] + all_cats
selected_cat = st.selectbox("Select category", all_cats)
if selected_cat:
    root_path = f"{src_root_path}/{selected_cat}"
    all_files = [i for i in os.listdir(root_path) if not i.startswith('.') and os.path.exists(f'{root_path}/{i}/output_text_desc_redux_switch_5_mask_V2.jpg')]

    for ind_file in all_files:
        garment_img = Image.open(f'{root_path}/{ind_file}/garment_cropped_upscaled.jpg')
        # garment_img_cropped = Image.open(f'{root_path}/{ind_file}/garment_upscaled_segmented.jpg')
        pin_ref_img = Image.open(f'{root_path}/{ind_file}/reference_upscaled.jpg')
        pin_ref_mask = Image.open(f'{root_path}/{ind_file}/reference_upscaled_mask_expanded_V2.png')
        gen_img = Image.open(f'{root_path}/{ind_file}/output_text_desc_redux_switch_5_mask_V2.jpg')

        pin_ref_mask_V2 = Image.open(f'{root_path}/{ind_file}/reference_upscaled_mask_V3.jpg')
        gen_img_V2 = Image.open(f'{root_path}/{ind_file}/output_text_desc_redux_switch_5_mask_V5.jpg')
        # gen_img_2 = Image.open(f'{root_path}/{ind_file}/output_cropped_V2_segmented_tryon.png')
        # gen_img_3 = Image.open(f'{root_path}/{ind_file}/output_text_desc_redux.jpg')
        # if os.path.exists(f'{root_path}/{ind_file}/output_prog_wf.png'):
        #     gen_img_4 = Image.open(f'{root_path}/{ind_file}/output_prog_wf.png')
        # else:
        #     gen_img_4 = None
        st.markdown(f'**{ind_file}**')
        cols = st.columns(6)
        cols[0].write('garment image(upscaled)')
        cols[0].image(garment_img)
        # cols[1].write('garment image(upscaled) - cropped for redux model')
        # cols[1].image(garment_img_cropped)
        cols[1].write('pin reference image(upscaled)')
        cols[1].image(pin_ref_img)
        cols[2].write('mask for inpainting')
        cols[2].image(pin_ref_mask)
        cols[3].write('mask for inpainting(updated)')
        cols[3].image(pin_ref_mask_V2)
        # cols[3].write('generated image')
        # cols[3].image(gen_img)
        # cols[4].write('generated image(segmented garment)')
        # cols[4].image(gen_img_2)
        cols[4].write('generated image(text+redux)')
        cols[4].image(gen_img)
        cols[5].write('generated image(updated mask)')
        cols[5].image(gen_img_V2)
        # if gen_img_4:
        #     cols[4].write('generated image(prog workflow)')
        #     cols[4].image(gen_img_4)
        st.divider()