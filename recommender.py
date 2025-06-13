import pickle
import requests
import urllib.parse
import streamlit as st

movies = pickle.load(open('model_file/movies.pkl', 'rb'))
similarity = pickle.load(open('model_file/similarity.pkl', 'rb'))

def fetch_poster(movie_name):
    api_key = "Your_OMDB_api_key"
    url = f"https://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url).json()
    poster_url = response.get("Poster", "")
    if not poster_url or poster_url == "N/A":
        poster_url = "https://via.placeholder.com/500x750?text=No+Poster"
    
    query = urllib.parse.quote(movie_name + " movie")
    google_link = f"https://www.google.com/search?q={query}"
    return poster_url, google_link

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x : x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    recommended_links = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        poster_url, google_url = fetch_poster(title)

        recommended_movies.append(title)
        recommended_posters.append(poster_url)
        recommended_links.append(google_url)

    return recommended_movies, recommended_posters, recommended_links