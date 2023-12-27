import pickle
import requests
import streamlit as st
import streamlit.components as components


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=c229e3e14cb82ac0062de6d535ebbca9".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data["poster_path"]
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path      


movies = pickle.load(open('C:/Users/Lenovo/PycharmProjects/movie recommender system/movie_list.pkl', 'rb'))
similarity = pickle.load(open('C:/Users/Lenovo/PycharmProjects/movie recommender system/similarity.pkl', 'rb'))


movie_list = movies['original_title'].values

st.header("Movie Recommendation System")

# creating a dropdown
selected_movie = st.selectbox('Select a movie', movie_list)


def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movies_id = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].original_title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster


if st.button("Recommend"):
    movie_name, movie_poster = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
