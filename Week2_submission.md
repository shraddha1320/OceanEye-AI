Week2 Submission: Dataset Preparation & CNN Training
Problem Statement

Marine plastic pollution is a growing environmental crisis.
The goal of OceanEye-AI is to detect and classify plastic waste floating on ocean surfaces using aerial or satellite images.
This week’s focus: preparing a usable dataset and training the CNN model for accurate classification of clean vs polluted water.

Dataset
Feature              	Details
Polluted Images	        Collected from Roboflow
Clean Images	        Collected manually
Preprocessing	        Resized to 128×128, normalized, train/test split applied
Train/Test Split	    80/20
Number of Images	    69 polluted, 20 clean

Folder Structure
data/
└── processed/
    ├── clean/
    │   ├── train/      # Clean training images
    │   └── test/       # Clean test images
    └── polluted/
        ├── train/      # Polluted training images
        └── test/       # Polluted test images


Sample images from each class were visualized in DatasetPrep.ipynb.

Tools and Technologies
Tool	                 Purpose
Python	                 Core programming language
TensorFlow/Keras	     Deep Learning framework
OpenCV	                 Image preprocessing
NumPy / Pandas	         Data handling
Matplotlib	             Data visualization
Jupyter Notebook	     Experimentation and workflow

Notebooks
Notebook	               Purpose
DatasetPrep.ipynb	       Prepares and visualizes the dataset
CNN_Training.ipynb	       Defines, trains, and evaluates the CNN model

CNN Model Training & Results
Parameter	                     Value / Description
Architecture	                 3 Conv2D layers + MaxPooling + Flatten + Dense layers + Dropout
Data Augmentation	             rotation_range=20, width/height_shift=0.1, horizontal_flip=True
Batch Size	                     8
Epochs	                         15
Loss Function	                 Binary Crossentropy
Optimizer	                     Adam (lr=0.001)
Test Accuracy	                 ~83%


Model File	water_quality_cnn.h5 (too large for GitHub; use Drive link)

Training curves, evaluation metrics, and sample predictions are included in the notebooks.

Usage

Open DatasetPrep.ipynb → run all cells to generate X_train, X_test, y_train, y_test.

Open CNN_Training.ipynb → run all cells to train the CNN model and view evaluation.

 Note: water_quality_cnn.h5 is large (>100MB). Download separately from [Google Drive link] before running the GUI.

Project Lead
Name	                Domain	                          GitHub
Shraddha Hebbar     	Sustainability with AI / ML	      https://github.com/shraddha1320/OceanEye-AI
