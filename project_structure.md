# Project Structure: OceanEye-AI �

This document explains the folder and file structure of the project.

OceanEye-AI/ │
├── data/ │ 
├── raw/ → Unprocessed satellite or ocean dataset files │   
├── processed/ → Cleaned and labeled data ready for training │
└── README.md → Info about data sources and preprocessing │
├── notebooks/ │ 
├── EDA.ipynb → Data exploration, visualization, and cleaning │
├── Model_Training.ipynb → Model training and evaluation notebook │
└── Prediction_Test.ipynb → Testing the trained model │
├── src/ │   
├── data_loader.py → Functions for loading and preprocessing datasets │
├── model.py → CNN or ML model architecture │
├── train.py → Script to train and save the model │
├── predict.py → Runs predictions on new inputs │
└── utils.py → Helper functions (metrics, plotting, etc.) │
├── problem_statement.md → Project background and objectives 
├── README.md → Main project overview and usage 
└── project_structure.md → Explanation of folder structure
