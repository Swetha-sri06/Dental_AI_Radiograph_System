# streamlit dashboard
import streamlit as st
import cv2
from inference import run_inference

st.title("AI Dental Radiograph Analysis")

uploaded = st.file_uploader("Upload OPG")

if uploaded:

    file_bytes = uploaded.read()

    with open("temp.png","wb") as f:
        f.write(file_bytes)

    teeth,numbers = run_inference("temp.png")

    st.image("temp.png")

    st.write("Detected Teeth:",len(teeth))
