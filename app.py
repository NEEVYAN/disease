import streamlit as st
from streamlit_option_menu import option_menu
import diabetes
import heart
import home
import about
import parkinson


# Set up page configuration for full-width layout
st.set_page_config(
    page_title="Health Kwik Plus",
    page_icon="🏥",  
    layout="wide",  # Ensures full-width layout
    initial_sidebar_state="collapsed"  # Hides sidebar initially
)

# Load CSS for custom styling
def load_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: white; /* Light background color */
                
        }
        .container-fluid {
            padding-left: 0;
            padding-right: 0;
        }
        .navbar {
            margin-bottom: 20px;
            border-radius: 0;
        }
        .option-menu {
            margin: 0 auto;
            width: 100%;
            text-align: center;
        }
        .stApp {
            padding-top: 0;
        }
        </style>
    """, unsafe_allow_html=True)

# Render Navigation Bar
selected = option_menu(
    menu_title="Health Kwik Plus - Multiple Disease Prediction System",
    options=[
        'Home',
        'Diabetes Prediction',
        'Heart Disease Prediction',
        'Parkinson\'s Disease Prediction',
        'About'
    ],
    icons=['house', 'droplet-half', 'heart-pulse', 'lungs', 'info-circle'],
    default_index=0,
    menu_icon="🏥",  
    orientation="horizontal",  # Horizontal navigation
    styles={
        "nav-link-selected": {"background-color": "#2A9D8F", "color": "white"},
        "container": {"width": "100%"},
        "icon": {"font-size": "20px"},
    },
)

# Load CSS
load_custom_css()

# Define page routing logic
if selected == 'Home':
    home.app()
elif selected == 'About':
    about.app()
elif selected == 'Diabetes Prediction':
    diabetes.app()
elif selected == 'Heart Disease Prediction':
    heart.app()
elif selected == 'Parkinson\'s Disease Prediction':
    parkinson.app()
