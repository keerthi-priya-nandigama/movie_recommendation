import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------------------------
# Load Processed Dataset
# ---------------------------------

movies = pd.read_csv("processed_movies.csv")

# ---------------------------------
# Convert Text into Vectors
# ---------------------------------

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = cv.fit_transform(movies['tags']).toarray()

# ---------------------------------
# Calculate Cosine Similarity
# ---------------------------------

similarity = cosine_similarity(vectors)

# ---------------------------------
# Save Processed Movie Data
# ---------------------------------

pickle.dump(
    movies,
    open("movies.pkl", "wb")
)

# ---------------------------------
# Save Similarity Matrix
# ---------------------------------

pickle.dump(
    similarity,
    open("similarity.pkl", "wb")
)

print("===================================")
print("Model Trained Successfully")
print("movies.pkl Created")
print("similarity.pkl Created")
print("===================================")
