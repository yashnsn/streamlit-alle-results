import streamlit as st
import os
from PIL import Image
import json
import pandas as pd
import asyncio
import aiohttp
from io import BytesIO

df = pd.read_csv('seedream_comparision.csv')

st.set_page_config(layout='wide')
all_cats = [None] + df['category'].unique().tolist()

# Async function to fetch a single image
async def fetch_image(session, url: str):
    try:
        async with session.get(url, timeout=45) as response:
            if response.status == 200:
                img_bytes = await response.read()
                return Image.open(BytesIO(img_bytes))
            else:
                return None
    except Exception as e:
        st.error(f"Error loading {url}: {e}")
        return None

# Fetch multiple images in parallel
@st.cache_data(show_spinner=False)
def fetch_images_async(urls):
    async def runner():
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_image(session, url) for url in urls]
            return await asyncio.gather(*tasks)

    return asyncio.run(runner())

# Streamlit UI
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

        # Download images in parallel
        garment_img, pin_ref_img, gen_img, gen_img_using_upscaled, gen_img_V2 = fetch_images_async(urls)

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
