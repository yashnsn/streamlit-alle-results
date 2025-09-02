import streamlit as st
import os
from PIL import Image
import pandas as pd

st.set_page_config(layout='wide')

root_path = "prog_content_prod_run_V2"
df = pd.read_csv("/Users/yaswanth/Downloads/Syn_con_rejection%_RCA - Raw data.csv")
supp_df = pd.read_csv('/Users/yaswanth/Downloads/All urls - generated - joined (1).csv')

mapper = {i['id']:i['attr_generation_prompt'] for i in supp_df.iloc(0)}
# print(mapper.keys())
# print(df.columns)
all_rejection_reasons = df["rejection_reason"].unique()
selected_rejection_reason = st.selectbox("Select rejection_reason", all_rejection_reasons)

filtered_df = df[df["rejection_reason"] == selected_rejection_reason]
filtered_df_sampled = filtered_df.sample(n=30)
for ind_row in filtered_df_sampled.iloc(0):
    if not(os.path.exists(f'{root_path}/{ind_row["generation_id"]}') and os.path.exists(f'{root_path}/{ind_row["generation_id"]}/garment.jpg') and os.path.exists(f'{root_path}/{ind_row["generation_id"]}/reference.jpg') and os.path.exists(f'{root_path}/{ind_row["generation_id"]}/generated_image.jpg')):
        continue

    gen_id = ind_row["generation_id"]

    garment_image = f'{root_path}/{gen_id}/garment.jpg'
    garment_cropped_image = f'{root_path}/{gen_id}/garment_cropped.jpg'
    pin_ref_image = f'{root_path}/{gen_id}/reference.jpg'
    pin_ref_masked_image = f'{root_path}/{gen_id}/reference_masked.jpg'
    gen_image = f'{root_path}/{gen_id}/generated_image.jpg'
    gen_prompt = mapper[str(gen_id)]
    st.markdown(f"**{gen_id} - {ind_row["category"]}**")
    st.markdown(f"**{gen_prompt}**")
    cols = st.columns(5)
    cols[0].write('garment image')
    cols[0].image(garment_image)
    cols[1].write('garment cropped image')
    cols[1].image(garment_cropped_image)
    cols[2].write('pin reference image')
    cols[2].image(pin_ref_image)
    cols[3].write('pin reference masked image')
    cols[3].image(pin_ref_masked_image)
    cols[4].write('generated image')
    cols[4].image(gen_image)