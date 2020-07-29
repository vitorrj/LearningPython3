import json
import requests


def get_movies_from_tastedive(movie):
    base_url = "https://tastedive.com/api/similar"
    moviesParam = {}
    moviesParam['q'] = movie
    moviesParam['type'] = "movie"
    moviesParam['limit'] = 5

    page = requests.get(base_url, moviesParam)
    recommendations = page.json()
    print(recommendations.keys())
    similar_movies = []
    for elements in recommendations['Similar']['Results']:
        similar_movies.append(elements['Name'])
    print(similar_movies)
    dict = {'Similar': similar_movies}
    return dict


print(get_movies_from_tastedive("Baby Driver"))
print(get_movies_from_tastedive("Pulp Fiction"))