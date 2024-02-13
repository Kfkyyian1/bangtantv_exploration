### DATA EXTRACTION###
import isodate  # to convert string duration to seconds
from dateutil import parser  # Import the parser module from dateutil
from googleapiclient.discovery import build
import pandas as pd
import json  # import in both json and pprint so output results are more legible
import pprint

api_key = 'XXXX' #replace XXXX with your youtube api code

channel_ids = ['UCLkAepWjdylmXSltofFvsYQ']  # input BTS youtube channel video ID

api_service_name = "youtube"
api_version = "v3"

# Get credentials and create an API client
youtube = build(
    api_service_name, api_version, developerKey=api_key)

# Function to get channel stats


def get_channel_stats(youtube, channel_ids):
    all_data = []

    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id=','.join(channel_ids)
    )
    response = request.execute()

    # loop through items
    for item in response['items']:
        data = {'channelName': item['snippet']['title'],
                'subscribers': item['statistics']['subscriberCount'],
                'views': item['statistics']['viewCount'],
                'totalVideos': item['statistics']['videoCount'],
                'playlistId': item['contentDetails']['relatedPlaylists']['uploads']
                }
        all_data.append(data)

    return (pd.DataFrame(all_data))


channel_stats = get_channel_stats(youtube, channel_ids)

# to see channel stats. Can see channelName is BANGTANTV, 77100000 subscribers, 22026469510 views, 2424 totalVideos, and playlist ID.
channel_stats

# Function to get video ids
playlist_id = "UULkAepWjdylmXSltofFvsYQ"


def get_video_ids(youtube, playlist_id):
    video_ids = []
    next_page_token = None  # Initialize next_page_token

    while True:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=playlist_id,
            maxResults=50,  # this is the max in api parameters. Note that added in next page token below to get all 2424 videos
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break  # exit the loop if there are no more pages

    return video_ids


video_ids = get_video_ids(youtube, playlist_id)
# we can see code works but there's only 5 video IDs inititally. We know that BTS channel has 2424 videos.
# to print output that is more readable
pprint.pprint(video_ids)
# check number of video ids
len(video_ids)

# Collecting video description from each video_id
request = youtube.videos().list(
    part="snippet,contentDetails,statistics",
    id=video_ids[0:5]  # testing to get 5 video info first
)
response = request.execute()
pprint.pprint(response)

# Creating a function to create dictionary that will store all video details


def get_video_details(youtube, video_ids):
    all_video_info = []

    # This line starts a loop that iterates through the video IDs in groups of 50.
    # It helps in sending requests to the YouTube API in chunks because there is a limit on the number of video IDs you can request at once.
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=','.join(video_ids[i:i+50])
        )
        response = request.execute()

        for video in response['items']:
            stats_to_keep = {'snippet': ['channelTitle', 'title', 'description', 'tags', 'publishedAt'],
                             'statistics': ['viewCount', 'likeCount', 'favouriteCount', 'commentCount'],
                             'contentDetails': ['duration', 'definition', 'caption']
                             }
            video_info = {}
            video_info['video_id'] = video['id']

            for k in stats_to_keep.keys():
                for v in stats_to_keep[k]:
                    try:
                        # attempts to get the specified information from the video details. If it fails (due to missing information), it sets the value to None.
                        video_info[v] = video[k][v]
                    except:
                        video_info[v] = None

            all_video_info.append(video_info)
    return pd.DataFrame(all_video_info)


video_df = get_video_details(youtube, video_ids)
pprint.pprint(video_df)  # FINAL DATASET

### Data Cleaning ###
# Checking for null values
video_df.isnull().any()  # there is null for favouriteCount

# Check data type. change view, like, comment counts to numeric
video_df.dtypes  # check data type.
numeric_cols = ['viewCount', 'likeCount', 'favouriteCount', 'commentCount']
video_df[numeric_cols] = video_df[numeric_cols].apply(
    pd.to_numeric, errors='coerce', axis=1)

# CREATE NEW COLUMN that states the video publish day in the week
# 1- Convert 'publishedAt' column to datetime objects
video_df['publishedAt'] = video_df['publishedAt'].apply(
    lambda x: parser.parse(x))
# 2- Create a new column 'publishDayName' that represents the day of the week
video_df['publishDayName'] = video_df['publishedAt'].apply(
    lambda x: x.strftime("%A"))

# CREATE NEW COLUMN that shows video duration in seconds. Now showing string like PT2M25S. Convert YT duration to seconds.
# 1- import isodate  # Import the isodate module
# 2- Convert 'duration' column to seconds
video_df['durationSecs'] = video_df['duration'].apply(
    lambda x: isodate.parse_duration(x).total_seconds())
# 3- Display both 'durationSecs' and 'duration' columns
print(video_df[['durationSecs', 'duration']])

# export video_df to CSV
video_df.to_csv('video_df.csv', index=False)
