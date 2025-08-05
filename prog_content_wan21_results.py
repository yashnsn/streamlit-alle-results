import os
import streamlit as st
from PIL import Image
st.set_page_config(page_title="WAN21 Results", page_icon=":chart_with_upwards_trend:", layout="wide")

root_path_V1 = "wan2.1 results"
root_path_V2 = "prog_content/wan21_results"
runwayML_results = "test_dataset_V2_output_V8/dress"

for ind_folder in os.listdir(root_path_V2):
    if ind_folder.startswith('.'):
        continue
    
    cropped_garment = Image.open(os.path.join(root_path_V2, ind_folder, "cropped_garment.png"))
    reference_altered = Image.open(os.path.join(root_path_V2, ind_folder, "reference_altered.png"))
    wan21_result = Image.open(os.path.join(root_path_V2, ind_folder, "output.png"))
    runwayML_result = Image.open(os.path.join(runwayML_results, ind_folder, "output.png"))

    cols = st.columns(4)
    with cols[0]:
        st.write("Cropped Garment")
        st.image(cropped_garment)
    with cols[1]:
        st.write("Reference Altered")
        st.image(reference_altered)
    with cols[2]:
        st.write("WAN21 Result")
        st.image(wan21_result)
    with cols[3]:
        st.write("RunwayML Result")
        st.image(runwayML_result)
    st.write("---")