import os
import streamlit as st
from PIL import Image
import json
from collections import defaultdict

alphabake_path = "alphabake_V5"
google_path = "google_results_V4"

st.set_page_config(layout="wide")

def load_scores(json_path="scores_prod.json"):
    if os.path.exists(json_path):
        with open(json_path, "r") as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    return {}

def save_scores(scores, json_path="scores_prod.json"):
    with open(json_path, "w") as f:
        json.dump(scores, f, indent=2)

scores_json_path = "scores_prod.json"
scores = load_scores(scores_json_path)

all_people = [None]
all_people += list(os.listdir(google_path))

selected_person = st.selectbox('Person', all_people)

if selected_person:
    all_files = [i for i in os.listdir(f'{google_path}/{selected_person}') if os.path.exists(f'{alphabake_path}/tryon/{selected_person}_base_image_{i}')]

    for ind_file in all_files:
        cols = st.columns(6)
        cols[0].write('base image')
        cols[0].image(Image.open(f'{alphabake_path}/human/{selected_person}_base_image_{ind_file}'))

        cols[1].write('Garment image')
        cols[1].image(Image.open(f'{alphabake_path}/garment/{selected_person}_base_image_{ind_file}'))
        
        cols[2].write('Alphabake tryon')
        cols[2].image(Image.open(f'{alphabake_path}/tryon/{selected_person}_base_image_{ind_file}'))

        cols[3].write('google tryon')
        cols[3].image(Image.open(f'{google_path}/{selected_person}/{ind_file}'))

        # Unique key for this tryon
        tryon_key = f"{selected_person}_{ind_file}"
        prev = scores.get(tryon_key, {})
        prev_alphabake = prev.get("alphabake", {})
        prev_google = prev.get("google", {})

        with cols[4]:
            st.write("Alphabake Scores")
            alphabake_bodyshape = st.selectbox(
                "Bodyshape", [None, 0, 1],
                key=f"alphabake_bodyshape_{selected_person}_{ind_file}",
                index=[None, 0, 1].index(prev_alphabake.get("bodyshape", None)) if prev_alphabake.get("bodyshape", None) in [None, 0, 1] else 0
            )
            alphabake_garment = st.selectbox(
                "Garment", [None, 0, 1],
                key=f"alphabake_garment_{selected_person}_{ind_file}",
                index=[None, 0, 1].index(prev_alphabake.get("garment", None)) if prev_alphabake.get("garment", None) in [None, 0, 1] else 0
            )
            alphabake_realism = st.selectbox(
                "Realism", [None, 0, 1],
                key=f"alphabake_realism_{selected_person}_{ind_file}",
                index=[None, 0, 1].index(prev_alphabake.get("realism", None)) if prev_alphabake.get("realism", None) in [None, 0, 1] else 0
            )

        with cols[5]:
            st.write("Google Scores")
            google_bodyshape = st.selectbox(
                "Bodyshape", [None, 0, 1],
                key=f"google_bodyshape_{selected_person}_{ind_file}",
                index=[None, 0, 1].index(prev_google.get("bodyshape", None)) if prev_google.get("bodyshape", None) in [None, 0, 1] else 0
            )
            google_garment = st.selectbox(
                "Garment", [None, 0, 1],
                key=f"google_garment_{selected_person}_{ind_file}",
                index=[None, 0, 1].index(prev_google.get("garment", None)) if prev_google.get("garment", None) in [None, 0, 1] else 0
            )
            google_realism = st.selectbox(
                "Realism", [None, 0, 1],
                key=f"google_realism_{selected_person}_{ind_file}",
                index=[None, 0, 1].index(prev_google.get("realism", None)) if prev_google.get("realism", None) in [None, 0, 1] else 0
            )

        # Store the responses in the dictionary
        scores[tryon_key] = {
            "person": selected_person,
            "ind_file": ind_file,
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
        save_scores(scores, scores_json_path)

    # --- Average score display logic ---
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