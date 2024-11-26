import streamlit as st
import base64
import os

def image_to_base64(image_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))

    image_path_full = os.path.join(script_dir, image_path)
    

    if not os.path.exists(image_path_full):
        st.error(f"Image file not found: {image_path_full}")
        return ''
    
    with open(image_path_full, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def app():
    st.markdown("<h1 style='text-align: center; color: red;'>About Multiple Disease Prediction Project</h1>", unsafe_allow_html=True)
    st.write("This project aims to predict the likelihood of three major diseases: Diabetes, Heart Disease, and Chronic Kidney Disease.")
    st.write("The project was developed by a team of three final year students under the supervision of Assistant Professor [Manish Kumar Srivastava](mailto:mkscs@mmmut.ac.in) from the Department of Computer Science and Engineering at Madan Mohan Malaviya University of Technology (MMMUT), Gorakhpur.")
    st.write("The goal of this project was to utilize machine learning techniques to create predictive models that can assist in the early detection and prevention of these diseases, thereby improving healthcare outcomes.")
    st.write("The project utilizes datasets containing relevant medical information such as patient demographics, medical history, and diagnostic test results.")
    st.write("Using this data, the project implements machine learning algorithms to predict the likelihood of each disease based on the input parameters provided by the user.")
    st.write("The predictions provided by the models are intended to serve as a tool for healthcare professionals to prioritize and personalize patient care, as well as for individuals to assess their own health risks.")
    st.write("We hope that this project contributes to the advancement of healthcare technology and facilitates better health management for individuals.")
    st.write("For any inquiries or feedback, please contact:")
    st.write("- [Kushagra Shukla](mailto:2020021073@mmmut.ac.in)")
    st.write("- [Harsh Vardhan Gaur](mailto:2020021062@mmmut.ac.in)")
    st.write("- [Hiralal Kumar Yadav](mailto:2020021066@mmmut.ac.in)")
    
    img_data = image_to_base64("images/MMMUT.jpg")
    if img_data:
        st.markdown(f"<img src='data:image/jpeg;base64,{img_data}' alt='MMMUT Logo' style='width:100%; height:300px'>", unsafe_allow_html=True)
