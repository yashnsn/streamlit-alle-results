import os
from PIL import Image
import streamlit as st

st.set_page_config(page_title="AlphaBakeVGoogle", layout="wide")

root_path = "alphabake_final_test_results_V2"
google_path = os.path.join(root_path, "google_tryons")
alphabake_path = os.path.join(root_path, "tryons")

people = [None,'isha', 'prateek', 'stuti']

all_male_garment_images = [i for i in os.listdir(os.path.join(root_path, 'garments')) if 'outfit' in i]
all_female_garment_images = [i for i in os.listdir(os.path.join(root_path, 'garments')) if 'outfit' not in i]
person = st.selectbox("Select a person", people, index=0)
# for person in people:
import json

# Define a function to load and save scores
def load_scores(json_path="scores.json"):
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    return {}

def save_scores(scores, json_path="scores.json"):
    with open(json_path, "w") as f:
        json.dump(scores, f, indent=2)

scores_json_path = "scores.json"
scores = load_scores(scores_json_path)

if person is not None:
    if person == 'prateek':
        garments_list = all_male_garment_images
    else:
        garments_list = all_female_garment_images

    for garment_name in garments_list:
        for base_image_idx in range(1, 3):
            alphabake_tryon_path = os.path.join(alphabake_path, person, f'base_image_{base_image_idx}', garment_name)
            alphabake_image = Image.open(alphabake_tryon_path)
            
            base_image_path = os.path.join(root_path, 'base_images', f'{person}_base_image_{base_image_idx}.png')
            base_image = Image.open(base_image_path)

            garment_image_path = os.path.join(root_path, 'garments', garment_name)
            garment_image = Image.open(garment_image_path)

            google_tryon_path = os.path.join(google_path, person, f'base_image_{base_image_idx}', garment_name)
            if os.path.exists(google_tryon_path):
                google_tryon_image = Image.open(google_tryon_path)
            else:
                google_tryon_image = None

            cols = st.columns([4,4,6,5,2,2])
            cols[0].write('base image')
            cols[0].image(base_image)
            cols[1].write('garment image')
            cols[1].image(garment_image)
            cols[2].write('alphabake image')
            cols[2].image(alphabake_image)
            if google_tryon_image is not None:
                cols[3].write('google tryon image')
                cols[3].image(google_tryon_image)
            else:
                cols[3].write('No google tryon image')

            # Scoring for alphabake (0 or 1)
            

            # Unique key for this tryon
            tryon_key = f"{person}_{base_image_idx}_{garment_name}"

            # Get previous values if they exist, else default to 0
            prev = scores.get(tryon_key, {})
            prev_alphabake = prev.get("alphabake", {})
            prev_google = prev.get("google", {})

            with cols[4]:
                st.write("Alphabake Scores")
                alphabake_bodyshape = st.selectbox(
                    "Bodyshape", [None, 0, 1],
                    key=f"alphabake_bodyshape_{person}_{base_image_idx}_{garment_name}",
                    index=[None, 0, 1].index(prev_alphabake.get("bodyshape", None)) if prev_alphabake.get("bodyshape", None) in [None, 0, 1] else 0
                )
                alphabake_garment = st.selectbox(
                    "Garment", [None, 0, 1],
                    key=f"alphabake_garment_{person}_{base_image_idx}_{garment_name}",
                    index=[None, 0, 1].index(prev_alphabake.get("garment", None)) if prev_alphabake.get("garment", None) in [None, 0, 1] else 0
                )
                alphabake_realism = st.selectbox(
                    "Realism", [None, 0, 1],
                    key=f"alphabake_realism_{person}_{base_image_idx}_{garment_name}",
                    index=[None, 0, 1].index(prev_alphabake.get("realism", None)) if prev_alphabake.get("realism", None) in [None, 0, 1] else 0
                )

            with cols[5]:
                st.write("Google Scores")
                google_bodyshape = st.selectbox(
                    "Bodyshape", [None, 0, 1],
                    key=f"google_bodyshape_{person}_{base_image_idx}_{garment_name}",
                    index=[None, 0, 1].index(prev_google.get("bodyshape", None)) if prev_google.get("bodyshape", None) in [None, 0, 1] else 0
                )
                google_garment = st.selectbox(
                    "Garment", [None, 0, 1],
                    key=f"google_garment_{person}_{base_image_idx}_{garment_name}",
                    index=[None, 0, 1].index(prev_google.get("garment", None)) if prev_google.get("garment", None) in [None, 0, 1] else 0
                )
                google_realism = st.selectbox(
                    "Realism", [None, 0, 1],
                    key=f"google_realism_{person}_{base_image_idx}_{garment_name}",
                    index=[None, 0, 1].index(prev_google.get("realism", None)) if prev_google.get("realism", None) in [None, 0, 1] else 0
                )

            # Store results in the scores dict
            scores[tryon_key] = {
                "person": person,
                "base_image_idx": base_image_idx,
                "garment_name": garment_name,
                "alphabake": {
                    "bodyshape": alphabake_bodyshape,
                    "garment": alphabake_garment,
                    "realism": alphabake_realism
                },
                "google": {
                    "bodyshape": google_bodyshape,
                    "garment": google_garment,
                    "realism": google_realism
                }
            }

            # Save to JSON file
            save_scores(scores, scores_json_path)

            st.divider()

    from collections import defaultdict

    def average_score_per_person(scores, model, score_type):
        person_scores = defaultdict(list)
        for tryon in scores.values():
            person = tryon.get("person")
            if model in tryon and score_type in tryon[model]:
                val = tryon[model][score_type]
                if val is not None:
                    person_scores[person].append(val)
        # Compute average per person
        return {person: (sum(vals) / len(vals) if vals else None) for person, vals in person_scores.items()}

    # Ask user to select a person
    all_persons = sorted({tryon.get("person") for tryon in scores.values() if tryon.get("person") is not None})
    selected_person = person
    # selected_person = st.selectbox("Select a person to view their average scores", all_persons)

    # Compute averages for the selected person only
    def average_score_for_selected_person(scores, model, score_type, person):
        vals = [
            tryon[model][score_type]
            for tryon in scores.values()
            if tryon.get("person") == person and model in tryon and score_type in tryon[model] and tryon[model][score_type] is not None
        ]
        return sum(vals) / len(vals) if vals else None

    alphabake_bodyshape_avg = average_score_for_selected_person(scores, "alphabake", "bodyshape", selected_person)
    alphabake_garment_avg = average_score_for_selected_person(scores, "alphabake", "garment", selected_person)
    alphabake_realism_avg = average_score_for_selected_person(scores, "alphabake", "realism", selected_person)
    google_bodyshape_avg = average_score_for_selected_person(scores, "google", "bodyshape", selected_person)
    google_garment_avg = average_score_for_selected_person(scores, "google", "garment", selected_person)
    google_realism_avg = average_score_for_selected_person(scores, "google", "realism", selected_person)

    st.markdown(f"### Average Scores for {selected_person} (excluding None values)")
    st.write({
        "Alphabake": {
            "bodyshape": alphabake_bodyshape_avg,
            "garment": alphabake_garment_avg,
            "realism": alphabake_realism_avg
        },
        "Google": {
            "bodyshape": google_bodyshape_avg,
            "garment": google_garment_avg,
            "realism": google_realism_avg
        }
    })
            
            