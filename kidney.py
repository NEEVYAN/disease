import streamlit as st
import pickle
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


model_path = os.path.join(script_dir, 'models', 'kidney.sav')


try:
    with open(model_path, 'rb') as f:
        kidney_model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}")
    kidney_model = None
except Exception as e:
    st.error(f"An error occurred while loading the model: {e}")
    kidney_model = None

def app():
    st.markdown("<h1 style='text-align: center; color: red;'>Chronic Kidney Disease Prediction</h1>", unsafe_allow_html=True)

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input("Age (in years)", min_value=0, max_value=120, value=50, step=1)
            blood_pressure = st.number_input("Blood Pressure (in mm/Hg)", min_value=0, max_value=200, value=80)
            specific_gravity = st.selectbox("Specific Gravity", options=[1.005, 1.010, 1.015, 1.020, 1.025])
        with col2:
            albumin = st.selectbox("Albumin Level", options=[0, 1, 2, 3, 4, 5])
            sugar = st.selectbox("Sugar Level", options=[0, 1, 2, 3, 4, 5])
            red_blood_cells = st.selectbox("Red Blood Cells", options={"Abnormal": 0, "Normal": 1})
        with col3:
            pus_cell = st.selectbox("Pus Cell", options={"Abnormal": 0, "Normal": 1})
            pus_cell_clumps = st.selectbox("Pus Cell Clumps", options={"Not Present": 0, "Present": 1})
            bacteria = st.selectbox("Bacteria", options={"Not Present": 0, "Present": 1})

        col4, col5, col6 = st.columns(3)
        with col4:
            blood_glucose_random = st.number_input("Blood Glucose Random (in mgs/dl)", min_value=0.0, max_value=500.0, value=100.0)
            blood_urea = st.number_input("Blood Urea (in mgs/dl)", min_value=0.0, max_value=300.0, value=50.0)
            serum_creatinine = st.number_input("Serum Creatinine (in mgs/dl)", min_value=0.0, max_value=15.0, value=1.0)
        with col5:
            sodium = st.number_input("Sodium (in mEq/L)", min_value=100.0, max_value=150.0, value=135.0)
            potassium = st.number_input("Potassium (in mEq/L)", min_value=0.0, max_value=10.0, value=4.5)
            haemoglobin = st.number_input("Haemoglobin (in gms)", min_value=0.0, max_value=20.0, value=15.0)
        with col6:
            packed_cell_volume = st.number_input("Packed Cell Volume", min_value=0, max_value=60, value=40)
            white_blood_cell_count = st.number_input("White Blood Cell Count (in cells/cumm)", min_value=0, max_value=20000, value=8000)
            red_blood_cell_count = st.number_input("Red Blood Cell Count (in millions/cmm)", min_value=0.0, max_value=10.0, value=5.0)

        col7, col8, col9 = st.columns(3)
        with col7:
            hypertension = st.selectbox("Hypertension", options={"No": 0, "Yes": 1})
            diabetes_mellitus = st.selectbox("Diabetes Mellitus", options={"No": 0, "Yes": 1})
        with col8:
            coronary_artery_disease = st.selectbox("Coronary Artery Disease", options={"No": 0, "Yes": 1})
            appetite = st.selectbox("Appetite", options={"Good": 0, "Poor": 1})
        with col9:
            pedal_edema = st.selectbox("Pedal Edema", options={"No": 0, "Yes": 1})
            aanemia = st.selectbox("Anemia", options={"No": 0, "Yes": 1})

    # Code for prediction
    kidney_diagnosis = ''

    # Button to predict result
    if st.button("Chronic Kidney Disease Prediction"):
        if kidney_model is None:
            st.error("Model is not loaded. Cannot perform prediction.")
        else:
            try:

                user_input = [
                    age,
                    blood_pressure,
                    specific_gravity,
                    albumin,
                    sugar,
                    red_blood_cells,
                    pus_cell,
                    pus_cell_clumps,
                    bacteria,
                    blood_glucose_random,
                    blood_urea,
                    serum_creatinine,
                    sodium,
                    potassium,
                    haemoglobin,
                    packed_cell_volume,
                    white_blood_cell_count,
                    red_blood_cell_count,
                    hypertension,
                    diabetes_mellitus,
                    coronary_artery_disease,
                    appetite,
                    pedal_edema,
                    aanemia
                ]

                user_input = [float(value) if isinstance(value, (int, float)) else float(value) for value in user_input]


                input_array = np.array(user_input).reshape(1, -1)

   
                kidney_prediction = kidney_model.predict(input_array)


                if kidney_prediction[0] == 1:
                    kidney_diagnosis = 'The person does not have chronic kidney disease.'
                else:
                    kidney_diagnosis = 'The person is likely to have chronic kidney disease.'

                st.success(kidney_diagnosis)
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")
