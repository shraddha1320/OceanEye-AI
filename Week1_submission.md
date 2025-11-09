Week2 Submission: Dataset Preparation & CNN Training
Problem Statement

Marine plastic pollution continues to threaten marine life and ecosystems.
OceanEye-AI automates detection and classification of plastic waste floating on ocean surfaces using Deep Learning (CNN).
This week’s focus: preparing a usable dataset and training the CNN model for accurate classification.

Dataset

Polluted images: Collected from Roboflow

Clean images: Collected manually

Preprocessing:

Resized to 128×128 pixels

Normalized pixel values

Train/test split applied

Folder Structure:

data/
└── processed/
    ├── clean/
    │   ├── train/
    │   └── test/
    └── polluted/
        ├── train/
        └── test/


Preview: Sample images from each class were visualized in the DatasetPrep notebook.

Tools and Technologies
Tool	Purpose
Python	Core programming language
TensorFlow / Keras	Deep Learning framework
OpenCV	Image preprocessing
NumPy / Pandas	Data handling
Matplotlib	Visualization
Jupyter Notebook	Experimentation and workflow
Notebooks

DatasetPrep.ipynb → Prepares and visualizes the dataset

CNN_Training.ipynb → Defines, trains, and evaluates the CNN model

Model Training & Results

Architecture: 3 convolutional layers + 2 dense layers + dropout

Data Augmentation: rotation, width/height shift, horizontal flip

Train/Test split: 80/20

Test Accuracy: ~83%

Outputs: Training curves, evaluation metrics, and model saved as water_quality_cnn.h5

⚠️ Note: water_quality_cnn.h5 is too large for GitHub; download separately from linked Drive folder.

Usage

Open DatasetPrep.ipynb → run all cells to generate X_train, X_test, y_train, y_test

Open CNN_Training.ipynb → run all cells to train the model and view evaluation

Project Lead
Name: Shraddha Hebbar  
Domain: Sustainability with AI / ML    
GitHub Repo: [https://github.com/shraddha1320/OceanEye-AI](https://github.com/shraddha1320/OceanEye-AI)
