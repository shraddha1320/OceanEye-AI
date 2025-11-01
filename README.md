#OceanEye-AI

Detecting Marine Plastic Pollution using Deep Learning

---
Overview

OceanEye-AI is an AI-driven sustainability project that detects and classifies marine plastic pollution from ocean images using Convolutional Neural Networks (CNNs).
The project aims to help researchers, NGOs, and authorities monitor ocean cleanliness automatically through satellite or drone imagery.

---
 Problem Statement

Plastic waste in oceans harms marine life and ecosystems. Manual inspection is slow and unreliable.
OceanEye-AI automates detection by using deep learning image classification, helping identify polluted regions efficiently and enabling data-driven cleanup actions.

---
Objectives

Build a CNN model to classify ocean images as:

green - Clean Water

yellow -  Floating Plastic

red - Severe Pollution

Promote sustainability through technology.
Provide a scalable model for integration with environmental monitoring systems.

---
 Methodology

1. Data Collection:
Gather open-source ocean datasets (e.g., Kaggle Ocean Plastic Dataset, NOAA images).

2. Preprocessing:
Resize and normalize images
Augment data for balance and diversity

3. Model Development (CNN):
Implement using TensorFlow/Keras
Layers: Conv2D → MaxPooling → Flatten → Dense → Softmax

4. Training & Evaluation:
Evaluate on accuracy, precision, recall, F1-score
Visualize using confusion matrix

5. (Future) Deploy using Streamlit as a web app

---
 Project Structure
OceanEye-AI/
│
├── data/                # Dataset and images
├── notebooks/           # Jupyter notebooks for experiments
├── src/                 # Model and training scripts
├── README.md            # Documentation
└── requirements.txt     # Dependencies

---
Tech Stack
Python 
TensorFlow / Keras
NumPy, Pandas, Matplotlib
OpenCV
Jupyter Notebook

---
 
 Sustainability Impact
OceanEye-AI supports UN SDG 14 – Life Below Water, contributing to cleaner oceans and healthier marine ecosystems.
By automating detection, it reduces human effort and accelerates environmental response.

---
Team
Project Lead: Shraddha Hebbar
Domain: Sustainability with AI-ML
Project Name: OceanEye-AI
