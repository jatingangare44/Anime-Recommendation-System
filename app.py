import pickle
import streamlit as st


def recommend(anime):
    """
    Recommends similar animes based on the selected anime using the similarity matrix.
    """
    index = new_df[new_df['title'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_anime_names = []
    for i in distances[1:6]:
        recommended_anime_names.append(new_df.iloc[i[0]].title)

    return recommended_anime_names


# Streamlit UI
st.title('Anime Recommender System')
st.subheader("Developed by Jatin Gangare")

# Load the necessary data
new_df = pickle.load(open('artifacts/anime_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/anime_similarity.pkl', 'rb'))

# Text input for anime name
selected_anime = st.selectbox(
    "Type or select an anime from the dropdown",
    new_df['title'].values
)

if selected_anime:
    st.write(f"You have selected: **{selected_anime}**")

    if st.button('Show Recommendations'):
        recommended_anime_names = recommend(selected_anime)
        st.write("Here are the top 5 recommended animes for you:")
        for i, anime in enumerate(recommended_anime_names, 1):
            st.write(f"{i}. {anime}")
