import streamlit as st
from Pages import cv2


def app():
    st.title('VEHICLE DETECTION')
    menu = ['From Image', 'From Video', 'Real Time']
    sidebar = st.sidebar
    sidebar.markdown('<a href="https://final-year-project-6a454.web.app" style="font-size:2em;text-decoration:none;font-style:bold">Dashboard</a>', unsafe_allow_html=True)
    choice = sidebar.selectbox("Menu", menu)
    if choice == 'From Image':
        plate_detection.detect_from_image()

if __name__ == '__main__':
    app()