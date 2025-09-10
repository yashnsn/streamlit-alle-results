import streamlit as st
import pandas as pd
import asyncio
import aiohttp
from PIL import Image
from io import BytesIO

# Load CSV
df = pd.read_csv('seedream_comparision.csv')

st.set_page_config(layout='wide')
all_cats = [None] + df['category'].unique().tolist()

# ---------- Async Helpers ----------
async def fetch_image(session, url, sem):
    """Fetch a single image with concurrency control."""
    async with sem:  # Limit concurrency
        # try:
        async with session.get(url, timeout=40) as response:
            if response.status == 200:
                data = await response.read()
                return Image.open(BytesIO(data))
            return None
        # except:
        #     return None

async def fetch_all_images(urls, limit=10):
    """Fetch all images asynchronously with a concurrency limit."""
    sem = asyncio.Semaphore(limit)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_image(session, url, sem) for url in urls]
        return await asyncio.gather(*tasks)

@st.cache_data(show_spinner=False)
def load_all_images(urls):
    return asyncio.run(fetch_all_images(urls, limit=10))

# ---------- UI ----------
selected_cat = st.selectbox("Select category", all_cats)

if selected_cat:
    filtered_df = df[df['category'] == selected_cat]

    # Collect all URLs
    all_urls = []
    for row in filtered_df.to_dict(orient='records'):
        all_urls.extend([
            row['cropped_garment_url'],
            row['reference_url'],
            row['seedream_og'],
            row['seedream_upscaled'],
            row['tryon_url']
        ])

    # Download all images with concurrency control
    all_images = load_all_images(all_urls)

    # Map back to rows
    img_index = 0
    for row in filtered_df.to_dict(orient='records'):
        garment_img = all_images[img_index]; img_index += 1
        pin_ref_img = all_images[img_index]; img_index += 1
        gen_img = all_images[img_index]; img_index += 1
        gen_img_using_upscaled = all_images[img_index]; img_index += 1
        gen_img_V2 = all_images[img_index]; img_index += 1

        st.write(row['generation_id'])
        st.write(row['image_generation_prompt'])
        cols = st.columns(5)
        cols[0].write('garment image(upscaled)'); cols[0].image(garment_img)
        cols[1].write('pin reference image(upscaled)'); cols[1].image(pin_ref_img)
        cols[2].write('generated image(prog)'); cols[2].image(gen_img_V2)
        cols[3].write('generated image(seedream)'); cols[3].image(gen_img)
        cols[4].write('generated image(seedream, using upscaled garment)'); cols[4].image(gen_img_using_upscaled)
        st.divider()
