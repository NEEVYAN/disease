import streamlit as st

def app():
    # Full-width header section
    st.markdown("""
    <div style="background-color: #007bff; color: white; padding: 30px; text-align: center;">
        <h1>Welcome to Health Kwik Plus</h1>
        <p>Your one-stop solution for multiple disease prediction</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction Section
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 30px; text-align: center; color: black">
        <h2 style="color: black">Why Choose Health Kwik Plus?</h2>
        <p >Health Kwik Plus is designed to provide accurate predictions for various diseases, helping you stay informed and take preventive measures. With state-of-the-art algorithms and a user-friendly interface, we ensure reliability and ease of use.</p>
    </div>
    """, unsafe_allow_html=True)

    # Features Section
    st.markdown("""
    <div style="padding: 30px;">
        <h2 style="text-align: center;">Features</h2>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 200px;">
                <h4 style="color: black">Accurate Predictions</h4>
                <p style="color: black">Our AI models achieve over 90% accuracy in disease prediction.</p>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 200px;">
                <h4 style="color: black">Secure Platform</h4>
                <p style="color: black">Your data is encrypted and protected with industry-standard security measures.</p>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 200px;">
                <h4 style="color: black">Expert Insights</h4>
                <p style="color: black">Backed by medical professionals to ensure clinical relevance.</p>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 200px;">
                <h4 style="color: black">24/7 Access</h4>
                <p style="color: black">Access the platform anytime, anywhere, on any device.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Services Section
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 30px;">
        <h2 style="text-align: center;">Our Services</h2>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 300px;">
                <h3 style="color: black">Diabetes Prediction</h3>
                <p style="color: black">Use advanced algorithms to predict your risk of diabetes.</p>
                <button style="background-color: #007bff; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;">Learn More</button>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 300px;">
                <h3 style="color: black">Heart Disease Prediction</h3>
                <p style="color: black">Identify potential heart disease risks with precision.</p>
                <button style="background-color: #007bff; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;">Learn More</button>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 300px;">
                <h3 style="color: black">Parkinson's Disease Prediction</h3>
                <p style="color: black">Detect early signs of Parkinson's disease effectively.</p>
                <button style="background-color: #007bff; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer;">Learn More</button>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Testimonials Section
    st.markdown("""
    <div style="padding: 30px;">
        <h2 style="text-align: center;">What Our Users Say</h2>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 300px;">
                <p style="color: black">"Health Kwik Plus helped me take proactive steps to manage my health. The predictions are accurate and easy to understand!"</p>
                <h5 style="color: black">- Jane Doe</h5>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 300px;">
                <p style="color: black">"The heart disease prediction module was a game-changer for me. I recommend it to everyone!"</p>
                <h5>- John Smith</h5>
            </div>
            <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); text-align: center; width: 300px;">
                <p style="color: black">"The platform is intuitive and provides valuable insights. Kudos to the team for making healthcare accessible!"</p>
                <h5 style="color: black">- Emily Johnson</h5>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("""
    <div style="background-color: #007bff; color: white; padding: 30px; text-align: center;">
        <h2 style="color: black">Contact Us</h2>
        <p style="color: black">If you have any questions or need assistance, feel free to reach out to us.</p>
        <p style="color: black">Email: support@healthkwikplus.com | Phone: +123 456 7890</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()
