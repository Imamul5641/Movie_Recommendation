import streamlit as st
import pickle
import requests

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Define the function to fetch movie posters using OMDB API
def fetch_poster(movie_name):
    api_key = st.secrets["key"]
    search_url = f"http://www.omdbapi.com/?apikey={api_key}&t={movie_name}"

    response = requests.get(search_url)
    data = response.json()

    # Check if the movie poster exists
    if 'Poster' in data and data['Poster'] != 'N/A':
        return data['Poster']
    else:
        return "No poster found for this movie"


# Define the function to recommend similar movies
def recommend(movie):
    recommended_movie_names = movies.loc[movies['title'] == movie, 'recommend'].iloc[0]
    recommended_movie_posters = []
    for i in recommended_movie_names:
        # Fetch the movie poster for each recommended movie
        recommended_movie_posters.append(fetch_poster(i))
    return recommended_movie_names, recommended_movie_posters


# Load the movie data from the pickle file
with open('recommend.pkl', 'rb') as f:
    movies = pickle.load(f)

# Get the list of movie titles
movies_list = movies['title'].values

# Set the title of the Streamlit app
st.title('Movie Recommender System')

# Create a dropdown to select movies
option = st.selectbox(
    'Search Movies by Name',
    movies_list)

# Display the recommendation button
if st.button('Recommend'):
    # Call the recommend function to get recommended movies and posters
    names, posters = recommend(option)

    # Display the recommended movies and their posters
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
