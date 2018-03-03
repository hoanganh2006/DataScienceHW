# Dependencies
import json

# Load JSON
with open('../Resources/youtube_response.json') as video_file:
    video_json = json.load(video_file)

# Isolate "data items" for easy reading
data = video_json["data"]
data_items = data["items"]

# Retrieve the video's title
title = data_items[0]["title"]
print("Title: ", title)

# Retrieve the video's rating
rating = data_items[0]["rating"]
print("Rating:", rating)

# Retrieve the link to the video's default thumbnail
default_thumbnail = data_items[0]["thumbnail"]["default"]
print("Thumbnail: ", default_thumbnail)

# Retrieve the number of views this video has
view_count = data_items[0]["viewCount"]
print("View count:", view_count)
