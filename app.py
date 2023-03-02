import streamlit as st
import pickle
import pandas as pd

movie_list = pickle.load(open('C:\\Users\\Akshay\\movies.pkl','rb'))
movies = pd.DataFrame(movie_list)

distance = pickle.load(open("C:\\Users\\Akshay\\distance.pkl", 'rb'))

st.title("Get Your Movie")

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = distance[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse= True, key = lambda x:x[1])[1:6]
    
    recommended_movies =[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies 

option = st.selectbox("What you like to watch",
        movies['title'].values)

if st.button('Recommend'):
        recommendetions = recommend(option)
        for i in recommendetions:
                st.write(i)