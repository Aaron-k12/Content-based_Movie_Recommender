#content based recommender system

#Importing libraries
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    """
    Fetches api for poster
    
    Returns:
    Url with API for poster path
    """
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=943a37e8545ad0168b7f7aa93417f4a0'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    """
    Finds similar movies
    
    Returns:
    Recommended movies and posters(images) fetched from api
    
    """
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse= True, key= lambda x:x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


#Initialzing variables with movie pickle file
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

#Initializing variable with similarity pickle file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# User Interface for the recommender system
st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    'What would you like to watch?',
    (movies['title'].values))

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])


