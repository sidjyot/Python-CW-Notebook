import tweepy
import os
import json

bearer_token = os.environ['BEARER_TOKEN']

client = tweepy.Client(bearer_token=bearer_token)
query_str = "(Veritas OR Veeam OR HPE OR NUTANIX OR Netapp) lang:en"
response = client.search_recent_tweets(query_str, max_results=25)

tweets = response.data
for i in tweets:
  print(json.dumps(i.data, indent=4))
  