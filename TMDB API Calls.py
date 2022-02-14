#APIs
import requests
import json

# Search API Example: https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Jack+Reacher
# Movie API Example: https://api.themoviedb.org/3/movie/238?api_key={api_key}
# Daily File export link: https://developers.themoviedb.org/3/getting-started/daily-file-exports

api_url = 'https://api.themoviedb.org/3/'
api_name = 'movie/'
search_api = 'search/movie?api_key='
movie_name = input("Please enter the movie name: ")
movie_id = '238'
api_key = 'e923f2e7cb1393354feb3d8295676466'


api_call = api_url + api_name + movie_id + "?api_key=" + api_key
search_api_call = api_url + search_api + api_key + '&query=' + movie_name
response = requests.get(search_api_call)
response_dict = response.json()

print(json.dumps(response_dict, indent=4))
print(search_api_call)