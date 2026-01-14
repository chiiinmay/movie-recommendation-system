# 🎬 Movie Recommendation System

This project implements a **Content-Based Movie Recommendation System** using machine learning techniques. The system recommends movies based on similarity in content such as movie genres and descriptions. A user-friendly interface is provided using **Streamlit**.

---

## 📌 Project Objective

With the rapid growth of online streaming platforms, users often find it difficult to choose movies that match their preferences.  
The objective of this project is to build an intelligent system that recommends relevant movies based on content similarity, without requiring user ratings or history.

---

## 🧠 Approach & Methodology

The recommendation system follows a **content-based filtering** approach:

1. Movie metadata such as **overview** and **genres** are combined into a single textual feature.
2. Text data is converted into numerical vectors using **CountVectorizer**.
3. **Cosine similarity** is computed between movie vectors to measure similarity.
4. Based on similarity scores, the system recommends the top 5 most similar movies for a given input movie.

---

## 🗂️ Dataset

- Dataset: TMDB 5000 Movies Dataset  
- Attributes used:
  - `title`
  - `overview`
  - `genres`

The dataset is preprocessed to remove missing values and combine relevant features before model training.

---

## 🧪 Model & Tools Used

- **Python**
- **Pandas** – data handling
- **Scikit-learn**
  - CountVectorizer
  - Cosine Similarity
- **Streamlit** – web application deployment
- **Jupyter Notebook** – core evaluation and experimentation

---

## 🚀 Project Structure

movie-recommendation-system/
│
├── movie_recommendation_system.ipynb # Main evaluation notebook
├── app.py # Streamlit application
├── movies.csv # Dataset
├── requirements.txt # Required dependencies
└── README.md # Project documentation

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
## 🌐 Live Demo

The Movie Recommendation System is deployed using Streamlit and can be accessed here:

👉 https://movie-recommendation-system-jgvtvy5ywekwqrpmenpbzs.streamlit.app/
