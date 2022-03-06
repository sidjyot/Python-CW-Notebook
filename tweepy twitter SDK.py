import tweepy
import os
import json

bearer_token = os.environ['BEARER_TOKEN']

client = tweepy.Client(bearer_token=bearer_token)

response = client.search_recent_tweets("Elon Musk")

tweets = response.data
for i in tweets:
  print(json.dumps(i.data, indent=4))
  