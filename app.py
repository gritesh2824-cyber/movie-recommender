import streamlit as st
import pickle
import pandas as pd
import requests
import os

# 🔑 PUT YOUR API KEY HERE
API_KEY = os.getenv("API_KEY")


# 🎨 BACKGROUND + UI STYLE
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(to right, #141e30, #243b55);
            color: white;
        }

        h1 {
            text-align: center;
            color: #FFD700;
        }

        .stButton>button {
            background-color: #ff4b2b;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }

        .stSelectbox label {
            color: white;
            font-size: 18px;
        }

        img {
            border-radius: 15px;
            transition: transform 0.2s;
        }

        img:hover {
            transform: scale(1.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )


set_bg()

# ✅ Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# 🎬 Fetch poster (SAFE VERSION)
@st.cache_data
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except:
        return "https://via.placeholder.com/500x750?text=Error"


# 🎯 Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# 🎨 UI TITLE
st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# 🔘 Button
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.caption(names[i])
            st.image(posters[i])