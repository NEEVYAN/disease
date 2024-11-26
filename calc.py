import streamlit as st
import requests  # To send data to Flask API

# Streamlit app code
st.title("My Streamlit App")

# Example: Accepting user input in Streamlit
user_input = st.text_input("Enter some data for ML calculation:")

if user_input:
    # Sending the data to the Flask API
    response = requests.post("http://localhost:5000/api/ml", json={"data": user_input})
    if response.status_code == 200:
        result = response.json()['result']
        st.write(f"ML Result: {result}")
    else:
        st.write("Error calling Flask API")
