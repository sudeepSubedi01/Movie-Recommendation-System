import streamlit as st
import pickle as pkl
import requests

movies_df = pkl.load(open('movies.pkl', 'rb'))
# st.write(movies_df['title'].values)

similarity = pkl.load(open('similarity_file.pkl', 'rb'))
# st.write(similarity)

def fetch_poster(movie_id):
  response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8777d9c586942ee574e65ea12273a4bc&language=en-US')
  data = response.json()
  path = "https://image.tmdb.org/t/p/w500"+data['poster_path']
  # st.write(path)
  return path

def recommend(movie):
  movie_index = movies_df[movies_df['title'] ==  movie].index[0]
  distances = similarity[movie_index]
  distances = list(enumerate(distances))
  movies_list = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]
  
  recommended_movies = []
  recommended_movies_posters = []
  for i in movies_list:
    movie_id = movies_df.iloc[i[0]].movie_id
    recommended_movies.append(movies_df.iloc[i[0]].title)
    recommended_movies_posters.append(fetch_poster(movie_id))

  return recommended_movies, recommended_movies_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Enter a movie name to recommend similar movies:', movies_df['title'].values)

# st.button('Recommend')
if st.button('Recommend'):
  rec_names, rec_posters = recommend(selected_movie_name)
  # for i in rec_names:
  #   st.write(i)

  col1,col2,col3,col4,col5 = st.columns(5)
  with col1: 
    st.image(rec_posters[0])
    st.write(rec_names[0])
  with col2: 
    st.image(rec_posters[1])
    st.write(rec_names[1])
  with col3: 
    st.image(rec_posters[2])
    st.write(rec_names[2])
  with col4: 
    st.image(rec_posters[3])
    st.write(rec_names[3])
  with col5: 
    st.image(rec_posters[4])
    st.write(rec_names[4])