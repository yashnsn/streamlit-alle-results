import streamlit as st
import os
from PIL import Image

st.set_page_config(layout='wide')
root_path = "/Users/yaswanth/repositories/tryon_production/testset_for_prod"

all_folders = [i for i in os.listdir(f"{root_path}/tryon_results_fin") if not i.startswith('.')]
all_garment_file_paths = {i:f"{root_path}/garment_images_fin/{cat}/{i}" for cat in os.listdir(f'{root_path}/garment_images_fin/') if not cat.startswith('.') for i in os.listdir(f'{root_path}/garment_images_fin/{cat}') if not i.startswith('.')}
# print(all_garment_file_paths)

base_imgs_testset = []
vton_imgs_testset = []
for base_image_name in all_folders:
    for garment_image_name in os.listdir(f'{root_path}/tryon_results_fin/{base_image_name}'):
        # face_img = Image.open(f'{root_path}/face_images/{base_image_name[:-2]}.jpg')
        # full_body_img = Image.open(f'{root_path}/full_body_images/{base_image_name[:-2]}.jpg')
        # base_image_generated = Image.open(f'{root_path}/base_images_fin/{base_image_name}.png')
        # garment_img = Image.open(all_garment_file_paths[garment_image_name])
        # final_tryon = Image.open(f'{root_path}/tryon_results_fin/{base_image_name}/{garment_image_name}')

        base_imgs_testset.append((f'{root_path}/face_images/{base_image_name[:-2]}.jpg', f'{root_path}/full_body_images/{base_image_name[:-2]}.jpg', f'{root_path}/base_images_fin/{base_image_name}.png'))
        vton_imgs_testset.append((all_garment_file_paths[garment_image_name], f'{root_path}/base_images_fin/{base_image_name}.png', f'{root_path}/tryon_results_fin/{base_image_name}/{garment_image_name}'))
base_imgs_testset = set(base_imgs_testset)

cats = [None, 'base image test set', 'vton testset']
selected_cat = st.selectbox('testset',cats)
if selected_cat:
    if cats[1] in selected_cat:
        for ind_img in base_imgs_testset:
            face_img = Image.open(ind_img[0])
            full_body_img = Image.open(ind_img[1])
            base_image_generated = Image.open(ind_img[2])
            cols = st.columns(3)
            cols[0].write('face image')
            cols[0].image(face_img)
            cols[1].write('full body image')
            cols[1].image(full_body_img)
            cols[2].write('generated base image')
            cols[2].image(base_image_generated)
        # cols[3].write('garment image')
        # cols[3].image(garment_img)
        # cols[4].write('final tryon image')
        # cols[4].image(final_tryon)

        st.divider()
    else:
        for ind_img in vton_imgs_testset:
            cols = st.columns(3)
            base_image_generated = Image.open(ind_img[1])
            garment_img = Image.open(ind_img[0])
            final_tryon = Image.open(ind_img[2]).resize(base_image_generated.size)
            cols[0].write('generated base image')
            cols[0].image(base_image_generated)
            cols[1].write('garment image')
            cols[1].image(garment_img)
            cols[2].write('final tryon image')
            cols[2].image(final_tryon)
            st.divider()