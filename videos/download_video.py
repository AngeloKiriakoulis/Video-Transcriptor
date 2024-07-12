from pytube import YouTube

# We download a specific amount of Youtube Videos, by URL & Pytube, using the dataset in https://ivi.fnwi.uva.nl/isis/mediamill/datasets/videostory.php

# Be careful with excessive download attempts, YouTube monitors API usage and imposes limits.s

# Most libraries that handle multimedia files support FFmpeg, an open-source tool for recording, converting, and streaming audio and video.

LINES_READ = 10

# Read the .txt file with the urls up until a point 
def URLsFromTXT(file) -> list:
  with open(file=file, mode= "r") as f:
    videos = [f.readline() for _ in range(LINES_READ)]
  return videos

# Pytube to download the videos, indexing used to simplify names.
# We are going to use this method in the main program, if we need to download videos.
def downloadVideos(videos) -> None:
  url_list = URLsFromTXT(videos)
  video_name=1 #Index goes up by one when a video is downloaded
  for url in url_list:
    try:
      youtubeObject = YouTube(url) #Initialize Object/Client that retrieves videos
      youtubeObject = youtubeObject.streams.get_highest_resolution() #Set extra parameters
      youtubeObject.download(output_path="videos",filename=str(video_name) + ".mp4") #Download videos to the folder and name them correctly 
      print("Download is completed successfully")
      video_name+=1
    except:
      print("An error has occurred")
