import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'AIzaSyDgePMd5Mvpr36q_lK2dhluRllcZbV7emM'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

import json

def youtubesearch(search,searchresult):
    # answerbot = json.dumps({"channels": ["MKBHD"], "discription": ["MKBHDFUCKKDSLKNDLKSNDLNSDLKNL"],'url':["https://i.ytimg.com/vi/5NNO5Kb-PZo/default.jpg"]})
    # return answerbot
    # pass
    search_response = youtube.search().list(q=search, part='id,snippet', maxResults=searchresult).execute()
    videos = []
    video_url = []
    channels = []
    playlists = []
    channelsdiscription = []
    for search_result in search_response.get('items', []):
        # print("search res : ",search_result['id']['kind'])
        # print("snippet: ",search_result["snippet"]['thumbnails']['medium']['url'])
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['snippet']['title']))
            video_url.append('%s' % (search_result["snippet"]['thumbnails']['medium']['url']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append('%s' % (search_result['snippet']['title']))
            channelsdiscription.append('%s' % (search_result['snippet']['description']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append('%s' % (search_result['snippet']['title']))

    if searchresult == 20:
        answerbot = json.dumps({"channels":["MKBHD"],"discription":["MKBHDFUCKKDSLKNDLKSNDLNSDLKNL"]})
        return answerbot
    else:
        answerbot = json.dumps({[{"videos":videos},{"urls":video_url}]})
        return answerbot

    # print(videos[:])
    # for i in range(len(channels)):


# for i in range(100):
#     try:
#         youtubesearch(search=input("search here :  "),searchresult=10)
#     except HttpError:
#         print("Error")
