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
## Week2 Submission: DatasetPrep & CNN Training

### Dataset
- Polluted images: Roboflow
- Clean images: Collected manually
- Preprocessing: Resized to 128x128, normalized, train/test split

### Notebooks
- `DatasetPrep.ipynb` → Prepares dataset, previews images
- `CNN_Training.ipynb` → Trains CNN, evaluates, plots results

### Usage
1. Open `DatasetPrep.ipynb` → Run all cells to generate `X_train, X_test, y_train, y_test`
2. Open `CNN_Training.ipynb` → Run all cells to train the model and see evaluation

### Results
- CNN test accuracy: 83%

---
Team
Project Lead: Shraddha Hebbar
Domain: Sustainability with AI-ML
Project Name: OceanEye-AI
