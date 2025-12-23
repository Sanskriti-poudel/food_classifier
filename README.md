# food_classifier
A food image classification project using convolutional neural networks and transfer learning, with a Streamlit interface and Docker-based deployment.
Project Overview

The Food Classification Project is a deep learning–based system designed to automatically classify images of food into different categories. It leverages transfer learning with MobileNetV2 to efficiently train a robust model on a custom dataset. The system is packaged as a Streamlit web application and deployed using Docker for consistent, reproducible execution across different machines.

Key Features
Deep Learning Model: Uses MobileNetV2 pretrained on ImageNet as the base.
Transfer Learning: Fine-tunes the top layers for custom food categories.
Data Augmentation: Includes rotation, zoom, horizontal flip to improve generalization.
Categorical Classification: Supports multi-class classification.
Streamlit Frontend: Allows users to interact with the model through a simple web interface.
Dockerized Deployment: Ensures that the app runs consistently on any machine.

To run on your device:
# Clone your GitHub repository
git clone https://github.com/YOUR_USERNAME/food_classifier.git
cd food_classifier

# Build the Docker image 
docker build -t food_classifier .

# Run the Streamlit app with port mapping
docker run -p 8501:8501 food_classifier
On your browser:http://localhost:8501


