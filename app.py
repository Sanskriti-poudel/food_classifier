import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image

# Load model
model = tf.keras.models.load_model("food_classifier_model.h5")

# Load class names
with open("class_names.json", "r") as f:
    class_names = json.load(f)

st.set_page_config(page_title="Food Classifier", layout="centered")

st.title("🍔 Food Image Classification")
st.write("Upload a food image to classify")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction)

    st.success(f"🍽 Predicted Food: {predicted_class}")
    st.info(f"📊 Confidence: {confidence * 100:.2f}%")
