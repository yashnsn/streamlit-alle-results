import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Custom Attention Flux", layout="wide")
# character_path_mapper = {
    # 'isha':('base_images/isha.jpeg','results/results_isha_prod_run_V0','results/isha_prod','results/isha_alphabake_tryon','garments/final_test_images'), 
    # 'stuti':('base_images/stuti_3.jpeg','results/results_stuti_prod_run_V0','base_images/stuti_LoKR2.png','results/results_stuti_LoKR2_prod_run_V0_updated_prompt','results/stuti'),
    # 'rhea':('base_images/rhea.png','results/results_rhea_prod_run_V0','base_images/rhea_LoKR2.png','results/results_rhea_LoKR2_prod_run_V0_updated_prompt','results/rhea')
# }
# garment_images_path = 'garments/final_test_images'
root_path = 'Testing_set_tops_alle'
results_path = 'results/prog_content_tops'
# all_people = [None]
# all_people += list(character_path_mapper.keys())
# person = st.selectbox('Person',all_people)

# if person is not None:
if True:
    # base_image_path, try_on_results_path, base_image_path_2, try_on_results_path_2, prod_results_path = character_path_mapper[person]
    # base_image_path, try_on_results_path, google_try_on_results_path, alphabake_tryon_path, garment_image_path = character_path_mapper[person]
    # base_image = Image.open(base_image_path)
    # base_image2 = Image.open(base_image_path_2)

    all_tryon_images = []
    all_google_tryon_images = []
    # all_alphabake_tryon_images = []
    all_garment_images = []
    all_base_images = []
    all_image_names = [i for i in os.listdir(root_path) if not i.startswith('.')]
    all_image_names.sort()
    for ind_result in all_image_names:
        try:
            all_tryon_images.append(Image.open(f'{root_path}/{ind_result}/tryon_fixed.png'))
        except:
            all_tryon_images.append(Image.open(f'{root_path}/{ind_result}/tryon.png'))
        all_google_tryon_images.append(Image.open(f'{results_path}/{ind_result}.png'))
        all_garment_images.append(Image.open(f'{root_path}/{ind_result}/product.png'))
        all_base_images.append(Image.open(f'{root_path}/{ind_result}/base.png'))
        # all_prod_results.append(Image.open(f'{prod_results_path}/{ind_result}'))

    for image_name, base_image, tryon_image,google_tryon_image, garment_image in zip(all_image_names, all_base_images, all_tryon_images, all_google_tryon_images,all_garment_images):
        st.write(f'File name: {image_name}')
        cols = st.columns(4)
        
        
        with cols[0]:
            st.write('base image')
            st.image(base_image, use_container_width=True)
        with cols[1]:
            st.write('try on result(ours)')
            st.image(tryon_image, use_container_width=True)
        with cols[2]:
            st.write('try on result(google)')
            st.image(google_tryon_image, use_container_width=True)
        with cols[3]:
            st.write('garment image')
            st.image(garment_image, use_container_width=True)
        
        st.divider()