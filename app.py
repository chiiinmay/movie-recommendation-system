import streamlit as st
import pickle
import requests

st.set_page_config(page_title="Movie Recommendation System", layout="wide")

API_KEY = "20689da8b5f883002cfab7cba8504228"

# Load artifacts
movies = pickle.load(open("artifacts/movie_list.pkl", "rb"))
similarity = pickle.load(open("artifacts/similarity.pkl", "rb"))

# Debug text (MUST SHOW)
st.write("Movies loaded:", movies.shape)
st.write("Similarity shape:", similarity.shape)

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    if data.get("poster_path"):
        return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    return "https://via.placeholder.com/300x450?text=No+Poster"

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        key=lambda x: x[1],
        reverse=True
    )

    names = []
    posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movie_id))

    return names, posters

st.title("🎬 Movie Recommendation System Using Machine Learning")

selected_movie = st.selectbox("Select a movie", movies['title'].values)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)
