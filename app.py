import streamlit as st
import pickle
def load_css():
    with open("static/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------------------------
# Load Model Files
# ---------------------------------
movies = pickle.load(open("model/movies.pkl", "rb"))
similarity = pickle.load(open("model/similarity.pkl", "rb"))

# ---------------------------------
# Recommendation Function
# ---------------------------------
def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:11]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


# ---------------------------------
# Title
# ---------------------------------
st.title("🎬 Movie Recommendation System")

st.write("A Content-Based Movie Recommendation System using Machine Learning")

# ---------------------------------
# Movie Selection
# ---------------------------------
selected_movie = st.selectbox(
    "Choose a Movie",
    movies["title"].values
)

# ---------------------------------
# Recommendation Button
# ---------------------------------
if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.success("Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")
st.caption("Developed using Python, Pandas, Scikit-Learn, and Streamlit")