import streamlit as st
import pickle
import pandas as pd
import requests
import streamlit.components.v1 as components

def fetch_video(movie):
    url = f"https://www.youtube.com/results?search_query={movie}+bollywood+movie+trailer"
    res = requests.get(url)
    idx = res.text.find("videoRenderer") + 15
    link = ""
    for i in res.text[idx:]:
        if(i==','):
            break
        link = link + i
    link = eval(link+'}')
    return "https://youtu.be/" + link['videoId']

def fetch_Url(movie_id):
    url = f"https://vidsrc.to/embed/movie/{movie_id}"
    return url

# def fetch_poster(movie_id):
#     # url = f"https://vidsrc.to/embed/movie/{movie_id}"
#     url = f"https://vidsrc.to/embed/movie/tt17048514"
#     # url = f"https://api.themoviedb.org/3/movie/{movie_id}"

#     # headers = {
#     # "accept": "application/json",
#     # "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OGNkMjRlYTAxMTU0ZThmZWZkZWUyMGZjMTVhNDMzYiIsInN1YiI6IjY0YWZlY2E5M2UyZWM4MDEwZGFlZDc5MCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.89nfxOM_BaMEycsW6O6f9nyq9OZixEDyMWOQsxuZ8fc"
#     # }

#     response = requests.get(url)
#     # print(response.text)
#     # data = response.json()
#     return response.text
#     try:
#         return "https://image.tmdb.org/t/p/w500" + data['poster_path']
#     except:
#         return "https://www.shutterstock.com/image-vector/no-image-vector-isolated-on-white-1481369594"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x : x[1])[0:10]

    recommend = []
    recommend_posters = []
    movie_id = []
    for i in movies_list:
        movie_id.append(movies.iloc[i[0]].id)
        recommend.append(movies.iloc[i[0]].title)
        # recommend_posters.append(fetch_poster(movie_id))
        recommend_posters.append(fetch_video(movies.iloc[i[0]].title))
    return movie_id,recommend,recommend_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.set_page_config(page_title="Movie Recommender System",layout="wide")
st.title('Movie Recommender System')
selected_movie = st.selectbox(
    'Name of the movie you want recommendations for ?',
     movies['title'].values
)

if st.button('Recommend'):
    with st.spinner("Checking Recommedations....."):
        id,names,posters = recommend(selected_movie)
        with st.container():
            colk, col1, col = st.columns([1,4,1])
            with colk:
                st.write(' ')
            with col1:
                st.video(posters[0])
                
                with st.container():
                    st.subheader(f"[{names[0]}]({fetch_Url(id[0])})")

            with col:
                st.write(' ')
        with st.container():
            col2, col3, col4, col5 = st.columns(4)
            with col2:
                st.video(posters[1])
                st.subheader(f"[{names[1]}]({fetch_Url(id[1])})")
            with col3:
                st.video(posters[2])
                st.subheader(f"[{names[2]}]({fetch_Url(id[2])})")
            with col4:
                st.video(posters[3])
                st.subheader(f"[{names[3]}]({fetch_Url(id[3])})")
            with col5:
                st.video(posters[4])
                st.subheader(f"[{names[4]}]({fetch_Url(id[4])})")

        with st.container():
            col6, col7, col8, col9, col10 = st.columns(5)
            with col6:
                st.video(posters[5])
                st.subheader(f"[{names[5]}]({fetch_Url(id[5])})")
            with col7:
                st.video(posters[6])
                st.subheader(f"[{names[6]}]({fetch_Url(id[6])})")
            with col8:
                st.video(posters[7])
                st.subheader(f"[{names[7]}]({fetch_Url(id[7])})")
            with col9:
                st.video(posters[8])
                st.subheader(f"[{names[8]}]({fetch_Url(id[8])})")
            with col10:
                st.video(posters[9])
                st.subheader(f"[{names[9]}]({fetch_Url(id[9])})")
    