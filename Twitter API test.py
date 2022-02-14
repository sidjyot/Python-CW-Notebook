#Twitter APIs 
import requests
import json
import yaml

def process_yaml():
    with open("config.yaml") as file:
        return yaml.safe_load(file)

def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]        

def create_twitter_url():
    handle = "sidjyot"
    max_results = 100
    mrf = "max_results={}".format(max_results)
    q = "query=from:{}".format(handle)
    url = "https://api.twitter.com/2/tweets/search/recent?{}&{}".format(
        mrf, q
    )
    return url

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def main():
    url = create_twitter_url()
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    res_json = twitter_auth_and_connect(bearer_token, url)
    print(json.dumps(res_json, indent = 4))

if __name__ == "__main__":
    main()




# The URL we are creating is:
# https://api.twitter.com/2/tweets/search/recent?max_results=100&query=from:sidjyot

# api_url = 'https://api.twitter.com/2/tweets/'
# search_api = 'search/recent?max_results=100&query=from:sidjyot'
# search_api_call = api_url + search_api 
# response = requests.get(search_api_call)
# response_dict = response.json()
# print(json.dumps(response_dict, indent=4))
# print(search_api_call)
