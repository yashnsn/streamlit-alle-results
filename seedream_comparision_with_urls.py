import streamlit as st
import os
from PIL import Image
import pandas as pd
import asyncio
import aiohttp
from io import BytesIO
import hashlib

# Make sure there's a folder to store downloaded images
DOWNLOAD_DIR = "downloaded_images"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Utility: Create a filename for each URL (safe for filesystem)
def url_to_filename(url: str) -> str:
    # Hash URL so filenames are unique and safe
    return hashlib.md5(url.encode()).hexdigest() + ".jpg"

# Async function to fetch and save a single image
async def fetch_and_save_image(session, url: str) -> str:
    filepath = os.path.join(DOWNLOAD_DIR, url_to_filename(url))
    if os.path.exists(filepath):
        return filepath  # Already downloaded

    try:
        async with session.get(url, timeout=45) as response:
            if response.status == 200:
                img_bytes = await response.read()
                with open(filepath, "wb") as f:
                    f.write(img_bytes)
                return filepath
            else:
                return None
    except Exception as e:
        st.error(f"Error downloading {url}: {e}")
        return None

# Fetch multiple images in parallel
def fetch_images_to_local(urls):
    async def runner():
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_and_save_image(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    return asyncio.run(runner())

# Load image from local path
def load_image(path: str):
    if path and os.path.exists(path):
        return Image.open(path)
    return None


# ---------------- Streamlit UI -------------------
df = pd.read_csv('seedream_comparision.csv')

st.set_page_config(layout='wide')
all_cats = [None] + df['category'].unique().tolist()

selected_cat = st.selectbox("Select category", all_cats)
if selected_cat:
    filtered_df = df[df['category'] == selected_cat]

    for ind_row in filtered_df.to_dict(orient='records'):
        urls = [
            ind_row['cropped_garment_url'],
            ind_row['reference_url'],
            ind_row['seedream_og'],
            ind_row['seedream_upscaled'],
            ind_row['tryon_url']
        ]

        # Download images to local
        local_paths = fetch_images_to_local(urls)
        images = [load_image(path) for path in local_paths]

        garment_img, pin_ref_img, gen_img, gen_img_using_upscaled, gen_img_V2 = images

        st.write(ind_row['generation_id'])
        st.write(ind_row['image_generation_prompt'])
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
        st.divider()
