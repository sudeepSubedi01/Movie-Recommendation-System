# Movie Recommendation System

## Virtual Environment
1. virtualenv myvenv
2. venv\Scripts\activate

## TMDB API
Hit this api:
https://api.themoviedb.org/3/movie/{movie_id}?api_key=8777d9c586942ee574e65ea12273a4bc&language=en-US

## Running streamlit app
1. streamlit run app.py

## Adding large files to GitHub using lfs
1. git lfs install
2. git lfs track "*.pkl"
3. git lfs --all origin main
4. git add .
5. git commit -m 'large files to github'
6. git push
7. git push -u origin main

## Creating requirement.txt
1. pip freeze > requirements.txt
OR, pipreqs --encoding=utf8
OR, manually create a file and add libraries to install