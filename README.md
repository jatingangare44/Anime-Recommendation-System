# Anime Recommendation System Using Machine Learning

Recommendation systems are essential tools in today's digital era, helping users discover new content based on their preferences. In this project, we have built an anime recommendation system using machine learning, specifically leveraging **Cosine Similarity** to suggest similar animes to users based on their selected anime.

## About this project:

This project is a **Streamlit web application** that recommends animes similar to a user-selected anime. It uses a content-based recommendation algorithm to match the features of an anime with others in the dataset.

### Features:
- A simple and intuitive interface where users can select an anime and receive recommendations.
- The recommendations are based on Cosine Similarity calculated between anime features.

### Demo:
* [Click here to run it live on the server](https://anime-recommender-system.herokuapp.com/)

## Dataset Used:
The dataset used in this project is the **Anime Dataset**. It contains various features such as anime titles, genres, descriptions, etc., that are used to compute similarities between different animes.

* [Dataset link](https://www.kaggle.com/azathoth/anime-recommendation-dataset)

## Concepts Used to Build the Model:
**Cosine Similarity:**
1. **Cosine Similarity** measures the cosine of the angle between two non-zero vectors. It is used to determine how similar two documents (or in this case, animes) are.
2. The similarity score ranges from 0 to 1:
    - 1 indicates that the two items are very similar.
    - 0 indicates no similarity.
3. We use the anime features such as genres and descriptions to build vectors and compute similarity.

## How to Run the Project:

### Steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/jatingangare44/Anime-Recommendation-System-ML-JG.git
    ```

2. **Create a Conda Environment:**

    ```bash
    conda create -n anime_recommender python=3.7.10 -y
    conda activate anime_recommender
    ```

3. **Install the Required Dependencies:**

    Install the required Python packages by running:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Application:**

    After installing the requirements, you can run the application using Streamlit:

    ```bash
    streamlit run app.py
    ```

    This will open the web application in your browser where you can select an anime and get similar anime recommendations.

## License:

This project is licensed under the **MIT License**.

## Author:

- **Author**: Jatin Gangare
- **Email**: jating22it@student.mes.ac.in
- **GitHub**: [jatingangare44](https://github.com/jatingangare44)

## Package Setup:

This project is packaged as a Python module. You can install the package by running:

```bash
python setup.py install
