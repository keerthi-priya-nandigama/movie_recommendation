import pandas as pd
import ast


# -------------------------------
# Load datasets
# -------------------------------

movies = pd.read_csv("../dataset/movies.csv")
credits = pd.read_csv("../dataset/credits.csv")


# -------------------------------
# Merge datasets
# -------------------------------

movies = movies.merge(credits, on="title")


# -------------------------------
# Select useful columns
# -------------------------------

movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew"
    ]
]


# -------------------------------
# Remove missing values
# -------------------------------

movies.dropna(inplace=True)


# -------------------------------
# Convert genres
# -------------------------------

def convert(text):

    L = []

    for i in ast.literal_eval(text):
        L.append(i["name"])

    return L


movies["genres"] = movies["genres"].apply(convert)


# -------------------------------
# Convert keywords
# -------------------------------

movies["keywords"] = movies["keywords"].apply(convert)


# -------------------------------
# Convert cast
# -------------------------------

def convert_cast(text):

    L = []

    counter = 0

    for i in ast.literal_eval(text):

        if counter != 3:

            L.append(i["name"])

            counter += 1

        else:
            break

    return L


movies["cast"] = movies["cast"].apply(convert_cast)


# -------------------------------
# Fetch Director
# -------------------------------

def fetch_director(text):

    L = []

    for i in ast.literal_eval(text):

        if i["job"] == "Director":

            L.append(i["name"])

            break

    return L


movies["crew"] = movies["crew"].apply(fetch_director)


# -------------------------------
# Split overview into words
# -------------------------------

movies["overview"] = movies["overview"].apply(lambda x: x.split())


# -------------------------------
# Remove spaces
# Example:
# Sam Worthington -> SamWorthington
# Science Fiction -> ScienceFiction
# -------------------------------

movies["genres"] = movies["genres"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["keywords"] = movies["keywords"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["cast"] = movies["cast"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)

movies["crew"] = movies["crew"].apply(
    lambda x: [i.replace(" ", "") for i in x]
)


# -------------------------------
# Create Tags
# -------------------------------

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)


# -------------------------------
# Keep only required columns
# -------------------------------

new_df = movies[
    [
        "movie_id",
        "title",
        "tags"
    ]
]


# -------------------------------
# Convert list into string
# -------------------------------

new_df["tags"] = new_df["tags"].apply(
    lambda x: " ".join(x)
)

new_df["tags"] = new_df["tags"].apply(
    lambda x: x.lower()
)


# -------------------------------
# Save processed dataset
# -------------------------------

new_df.to_csv(
    "processed_movies.csv",
    index=False
)


print("--------------------------------")
print("Dataset Processed Successfully!")
print("--------------------------------")

print(new_df.head())