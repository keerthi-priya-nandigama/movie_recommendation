# 🎬 Movie Recommendation System

## Overview

This project is a Content-Based Movie Recommendation System developed using Python and Machine Learning. It recommends movies similar to the movie selected by the user.

## Features

- Movie recommendation based on content similarity
- Streamlit web interface
- Displays movie posters using TMDB API
- Fast recommendations using cosine similarity

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Requests

## Project Structure

Movie-Recommendation-System/

├── app.py

├── requirements.txt

├── README.md

├── dataset/

│ ├── movies.csv

│ └── credits.csv

├── model/

│ ├── preprocessing.py

│ ├── processed_movies.csv

│ ├── train_model.py

│ ├── movies.pkl

│ └── similarity.pkl

└── static/

## How to Run

### Install Dependencies

pip install -r requirements.txt

### Create Processed Dataset

cd model

python preprocessing.py

### Train Model

python train_model.py

### Start Application

cd ..

streamlit run app.py

## Author

Your Name

B.Tech Mini Project