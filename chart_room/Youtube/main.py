import argparse
import subprocess
import sys
try:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ModuleNotFoundError:
    subprocess.call([sys.executable, "-m", "pip", "install","google-api-python-client","google-auth-httplib2"])
finally:
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError

DEVELOPER_KEY = 'AIzaSyDgePMd5Mvpr36q_lK2dhluRllcZbV7emM'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(q=options.q, part='id,snippet', maxResults=options.max_results).execute()

    videos = []
    video_url = []
    channels = []
    playlists = []
    for search_result in search_response.get('items', []):
        # print("search res : ",search_result['id']['kind'])
        # print("snippet: ",search_result["snippet"]['thumbnails']['medium']['url'])
        if search_result['id']['kind'] == 'youtube#video':
            videos.append('%s' % (search_result['snippet']['title']))
            video_url.append('%s' % (search_result["snippet"]['thumbnails']['medium']['url']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append('%s' % (search_result['snippet']['title']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append('%s' % (search_result['snippet']['title']))
    print(videos[:])
    print("{:>30}".format("Videos"), '\n',  "--"*45)
    for i in range(len(videos)):
        print(videos[i],video_url[i])
    print("{:>30}".format("Channels"), '\n',  "--"*45)
    print ('\n'.join(channels), '\n')
    print("{:>30}".format("Playlists"), '\n',  "--"*45)
    print ('\n'.join(playlists), '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='CaseyNeistat')
    parser.add_argument('--max-results', help='Max results', default=4)
    args = parser.parse_args()

try:
    youtube_search(args)
except Exception as HttpError:
    print(HttpError)
