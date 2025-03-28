import streamlit as st
import joblib
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

st.set_page_config(page_title="Movie Recommender", layout="wide")

@st.cache_resource
def load_movie_data():
    movie_df = joblib.load("model_helpers/movie_metadata.pkl")
    similarity_matrix = joblib.load("model_helpers/similarity.pkl")
    return movie_df, similarity_matrix

movie_df, similarity_matrix = load_movie_data()


@st.cache_data
def recommend_movies(movie_name, num_recommendations=5):
    if movie_name not in movie_df["title"].values:
        return []
    
    movie_index = movie_df[movie_df["title"] == movie_name].index[0]
    distances = similarity_matrix[movie_index]
    sorted_indices =distances[0:num_recommendations+1]
    recommended_movies = []
    for i, _ in sorted_indices:
        recommended_movies.append({
            "title": movie_df.iloc[i]["title"],
            "poster_url": f"https://image.tmdb.org/t/p/original/{movie_df.iloc[i]['poster_path']}",
            "genres": movie_df.iloc[i]["genres"]
        })
    
    return recommended_movies

def main():
    st.title("🎬 Movie Recommendation System")

    movie_name = st.selectbox(
        "Type a movie name:", 
        sorted(movie_df["title"].values),
        index=None,
        placeholder="Select a movie..."
    )

    num_recommendations = st.slider(
        "Select number of recommendations:", 
        min_value=5, 
        max_value=20, 
        step=5, 
        value=5
    )

    if st.button("Get Recommendations"):
        if movie_name:
            with st.spinner('Fetching recommendations...'):
                recommendations = recommend_movies(movie_name, num_recommendations)
                
                if recommendations:
                    st.subheader(f"Recommended Movies Similar to {movie_name}")
                    cols = st.columns(5)
                    
                    for idx, movie in enumerate(recommendations):
                        with cols[idx % 5]:
                            try:
                                response = requests.get(movie["poster_url"])
                                if response.status_code == 200:
                                    image = Image.open(BytesIO(response.content))
                                    st.image(image, use_container_width=True)
                                else:
                                    st.image("https://via.placeholder.com/150", use_container_width=True)
                            except Exception:
                                st.image("https://via.placeholder.com/150", use_container_width=True)
                            
                            st.write(f"**{movie['title']}**")
                            st.write(f"Genres: {movie['genres']}")
                else:
                    st.warning("No recommendations found. Try another movie.")
        else:
            st.warning("Please select a movie first.")


if __name__ == "__main__":
    main()