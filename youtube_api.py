import csv
import json
import requests
#import beautifulsoup4
import pandas
import os

youtube_key = os.environ['YOUTUBE_API_KEY']
api_url = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCJFp8uSYCjXOMnkUyb3CQ3Q&key=AIzaSyDdHiuQ3IvsZKC7CuaVDf4QDkLatQ_vRMw" 
api_reponse = requests.get(api_url)
videos = json.loads(api_reponse.text)
#print(videos)

with open("youtube_videos.csv", "w") as csv_file:
  csv_writer = csv.writer(csv_file)
  csv_writer.writerow(["publishedAt", "title", "description", "thumbnailurl"])
  if videos.get("items") is not None:
    for video in videos.get("items"):
      video_data_row = [
        video["snippet"]["publishedAt"],
        video["snippet"]["title"],
        video["snippet"]["description"],
        video["snippet"]["thumbnails"]["default"]["url"]
        ]
      csv_writer.writerow(video_data_row)
