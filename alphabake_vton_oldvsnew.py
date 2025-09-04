import streamlit as st
import os

st.set_page_config(layout='wide')
from PIL import Image

root_path = "multi-threaded-test_V17"

all_files = os.listdir(root_path)
