import streamlit as st
import os
from PIL import Image
import random

st.set_page_config(layout='wide')

all_possible_issues = ["blurry hands","artifacts","jawline distortion","edges issue","incorrect garment","incorrect body shape","unrealistic pose","pixelation","skin color mismatch","other"]
# base_images_path = "base_images_fin"
cats = [None]
cats += [i for i in os.listdir("old_data/fin_set_results") if not i.startswith('.')]
google_results_path = "old_data/fin_set_results_V3"
alphabake_res_path = "old_data/multi-threaded-test_V17"

selected_cat = st.selectbox('category',cats)
# all_files = [i for i in os.listdir(f'{}')]
import json



if selected_cat:
    issues_json_path = f"{alphabake_res_path}/fin_issues_{selected_cat}.json"

    # Load existing issues if present
    if os.path.exists(issues_json_path):
        with open(issues_json_path, "r") as f:
            try:
                all_issues = json.load(f)
            except Exception:
                all_issues = {}
    else:
        all_issues = {}
    all_results = list(os.listdir(f'{google_results_path}/{selected_cat}'))
    # random.shuffle(all_results)
    # all_results.sort()
    for ind_res in all_results:
        if ind_res.startswith('.'):
            continue

        image_name = ind_res.split("_",2)[-1]
        base_img_name = f'{ind_res.split("_",2)[0]}_{ind_res.split("_",2)[1]}'

        fin_name = f'{base_img_name}.png_base_image_{image_name}'.replace('.webp','.jpg').replace('.jpeg','.jpg')
        if 'stuti_0.png_base_image_2029275_1000.jpg' in fin_name or 'suhani_0.png_base_image_2029275_1000.jpg' in fin_name:
            continue
        if not os.path.exists(f'{alphabake_res_path}/human/{fin_name}'):
            continue
        base_img = Image.open(f'{alphabake_res_path}/human/{fin_name}')
        garment_img = Image.open(f'{alphabake_res_path}/garment/{fin_name}')
        
        tryon_img = Image.open(f'{alphabake_res_path}/tryon/{fin_name}')
        tryon_img_old = Image.open(f'{alphabake_res_path}/tryon_old/{fin_name}')
        # google_tryon = Image.open(f'{google_results_path}/{selected_cat}/{ind_res}')

        st.write(fin_name)
        cols = st.columns(4)
        cols[0].write('garment image')
        cols[0].image(garment_img)
        cols[1].write('base image')
        cols[1].image(base_img)
        # cols[2].write('alphabake tryon image(old)')
        # cols[2].image(tryon_img_old)
        cols[2].write('alphabake tryon image(new)')
        cols[2].image(tryon_img)
        cols[3].write('Issue')
        prev_issues = all_issues.get(fin_name, [])
        selected_issues = cols[3].multiselect("Select issue", all_possible_issues, default=prev_issues, key=fin_name)
        all_issues[fin_name] = selected_issues
        # cols[3].write('google tryon image')
        # cols[3].image(google_tryon)
        st.divider()

    # Save all issues to json after the loop
    with open(issues_json_path, "w") as f:
        json.dump(all_issues, f, indent=2)

        # INSERT_YOUR_CODE
        # Count the number of issues for each issue type
    from collections import Counter

    issue_counter = Counter()
    total_images_with_issues = 0
    total_issues = 0

    for issues in all_issues.values():
        if issues:
            total_images_with_issues += 1
            total_issues += len(issues)
        issue_counter.update(issues)

    st.header("Issues Summary")
    st.write(f"Total images: {len(all_issues)}")
    st.write(f"Images with at least one issue: {total_images_with_issues}")
    st.write(f"Total issues (all types, all images): {total_issues}")

    if issue_counter:
        st.write("Issue counts by type:")
        for issue, count in issue_counter.most_common():
            st.write(f"- {issue}: {count}")
    else:
        st.write("No issues selected yet.")
