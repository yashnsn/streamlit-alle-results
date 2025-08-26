import streamlit as st
from PIL import Image
import os

st.set_page_config(layout='wide')

from PIL import Image, ImageFilter
import numpy as np

def add_noise_and_sharpen_pil(img: Image.Image,
                              noise_std: float = 5.0,
                              sharpen_amount: float = 1.0,
                              blur_radius: float = 2.0) -> Image.Image:
    """
    Add Gaussian noise and then apply unsharp‐mask sharpening to a PIL Image.
    
    Parameters
    ----------
    img : PIL.Image.Image
        Input image (mode “RGB” or “RGBA”).
    noise_std : float
        Standard deviation of Gaussian noise (0–255 intensity scale).
    sharpen_amount : float
        Unsharp‐mask strength. 1.0 = default, higher = stronger sharpening.
    blur_radius : float
        Radius of the Gaussian blur used in the unsharp mask.
        
    Returns
    -------
    PIL.Image.Image
        The processed image.
    """
    # 1) Add Gaussian noise
    arr = np.array(img).astype(np.float32)
    noise = np.random.randn(*arr.shape) * noise_std
    noisy = np.clip(arr + noise, 0, 255).astype(np.uint8)
    noisy_img = Image.fromarray(noisy)
    
    # 2) Unsharp mask sharpening
    #    PIL’s UnsharpMask: radius, percent, threshold
    #    We map sharpen_amount → percent linearly (100% per unit)
    percent = 100 * sharpen_amount
    # threshold=0 ensures all pixels are considered
    sharpened = noisy_img.filter(
        ImageFilter.UnsharpMask(radius=blur_radius, percent=int(percent), threshold=3)
    )
    
    return sharpened

opt_path = "combined_images_output_V3"
non_opt_path = "combined_images_output_2_updated_prompt"

selected_cat = st.selectbox('categories',[None, 'fullbody', 'upperbody'])

if selected_cat:
    all_folders = {i for i in os.listdir(f'{opt_path}/{selected_cat}') if not i.startswith('.') and os.path.exists(f'{opt_path}/{selected_cat}/{i}/output_turbo.png')}
    all_folders = [i for i in os.listdir(f'{non_opt_path}/{selected_cat}') if i in all_folders and os.path.exists(f'{non_opt_path}/{selected_cat}/{i}/output_turbo.png')]

    for ind_folder in all_folders:
        garment_img = Image.open(f'{opt_path}/{selected_cat}/{ind_folder}/cropped_garment.jpg')
        ref_upscaled = Image.open(f'{non_opt_path}/{selected_cat}/{ind_folder}/reference_upscaled.jpg')
        ref_upscaled_opt = Image.open(f'{opt_path}/{selected_cat}/{ind_folder}/reference_compiler_upscaled.jpg')
        res = add_noise_and_sharpen_pil(Image.open(f'{non_opt_path}/{selected_cat}/{ind_folder}/output_turbo.png'),noise_std=4, sharpen_amount=0.5, blur_radius=2)
        res_opt = add_noise_and_sharpen_pil(Image.open(f'{opt_path}/{selected_cat}/{ind_folder}/output_turbo.png'),noise_std=4, sharpen_amount=0.5, blur_radius=2)

        cols = st.columns(5)

        cols[0].write('Garment Image')
        cols[0].image(garment_img)
        cols[1].write('Reference image upscaled')
        cols[1].image(ref_upscaled)
        cols[2].write('Reference image upscaled(optimized)')
        cols[2].image(ref_upscaled_opt)
        cols[3].write('Generated image')
        cols[3].image(res)
        cols[4].write('Generated image(optimized)')
        cols[4].image(res_opt)