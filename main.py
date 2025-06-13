import streamlit as st
import pickle
from recommender import recommend

movies = pickle.load(open('model_file/movies.pkl', 'rb'))
movie_list = movies['title'].values

st.set_page_config(page_title="Movie Recommender",
                   page_icon="🎬")

st.markdown(""" 
    <style>
            .poster-container {
                transition:transform 0.3s ease;
                display:block;
                overflow:hidden;
                border-radius:12px;
            }
            .poster-container:hover {
                transform:scale(1.05);
                z-index:10;
            }
    </style>
""", unsafe_allow_html=True)


st.title("🍿 Movie Recommendation System")

selected_movie = st.selectbox("🎬 Select a Movie:", movie_list)
if st.button("🚀 Recommend movies"):
    with st.spinner("Finding Similar Movies for Youu 😉..."):
        names, posters, links = recommend(selected_movie)
        st.success("Top Similar Movies:")
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.markdown(f"""
                            <a href="{links[i]}" target="_blank" style="text-decoration: none;">
                                <div class="poster-container">
                                    <img src="{posters[i]}" style="width:100%;"/>
                                </div>
                                <h5 style="text-align:center; font-size:15px; margin-top:10px; color:black;">{names[i]} </h5>
                            </a>
                        """, unsafe_allow_html=True)