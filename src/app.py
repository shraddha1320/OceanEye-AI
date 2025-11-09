import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# 🫧 Page setup
st.set_page_config(
    page_title="OceanEye-AI",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

#  Custom CSS (modern pastel style)
st.markdown("""
    <style>
    /* Background gradient for entire app */
    body {
        background-color: #fffaf6;
    }
    .stApp {
        background: linear-gradient(150deg, #a8dadc, #fffaf6);
        color: #333333;
        font-family: 'Helvetica Neue', 'Poppins', sans-serif;
    }

    /* Main content boxes */
    .css-1d391kg {
        background-color: #ffffffdd;
        border-radius: 25px;
        padding: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    /* Header */
    h1 {
        text-align: center;
        color: #457b9d;
        font-weight: 800;
        font-size: 2.5rem;
    }

    /* Uploaded image styling */
    .uploadedImage {
        border-radius: 20px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        margin-top: 20px;
    }

    /* Prediction box */
    .predictionBox {
        background-color: #ffffffee;
        border-left: 6px solid #f94144;
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    .predictionBox:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #999999;
        margin-top: 50px;
        font-size: 14px;
        font-style: italic;
    }

    /* Buttons (file uploader) */
    .stButton>button {
        background: linear-gradient(135deg, #fbc4ab, #ffb4a2);
        color: #fff;
        border-radius: 12px;
        padding: 8px 18px;
        font-weight: 600;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #ffb4a2, #f28482);
        transform: scale(1.05);
    }

    </style>
""", unsafe_allow_html=True)

#  Header
st.markdown("<h1>OceanEye-AI🐋</h1>", unsafe_allow_html=True)
st.write("Upload a photo and let this lil CNN tell if it’s **Clean** or **Polluted** ")

# Load your model
model = load_model("water_quality_cnn.h5")

#  File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image ", use_column_width=True, output_format="PNG")

    #  Preprocess
    img_resized = img.resize((128, 128))
    img_array = np.array(img_resized) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    #  Predict
    prediction = model.predict(img_array)
    prob = float(prediction[0][0])
    label = "Polluted " if prob > 0.5 else "Clean "
    confidence = round(prob * 100 if prob > 0.5 else (1 - prob) * 100, 2)

    # Output box
    # Dynamically change border color based on prediction
    border_color = "#f63f43" if prob > 0.5 else "#3ecca6"
    st.markdown(f"""
    <div class="predictionBox" style="border-left: 6px solid {border_color};">
        <h3>{label}</h3>
        <p>Confidence: <b>{confidence}%</b></p>
    </div>
    """, unsafe_allow_html=True)

#  Footer
st.markdown('<div class="footer">Made by Shraddha using CNN + Streamlit</div>', unsafe_allow_html=True)
