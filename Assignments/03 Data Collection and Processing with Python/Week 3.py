# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
import requests_with_caching
import json

def get_movies_from_tastedive(movie):
    baseurl="https://tastedive.com/api/similar"
    params_dict={}
    params_dict["q"]= movie
    params_dict["type"]="movies"
    params_dict["limit"] =5
    page = requests_with_caching.get(baseurl, params=params_dict)
    return page.json()

def extract_movie_titles(page):
    mylist = [key['Name'] for key in page['Similar']['Results']]
    return mylist

def get_related_titles(li):
    total=[]
    for x in li:
        ind = extract_movie_titles(get_movies_from_tastedive(x))
        print(ind)
        for i in ind:
            if i not in total:
                total.append(i)
    return total



#   get_related_titles(["Black Panther", "Captain Marvel"])
#   get_related_titles([])