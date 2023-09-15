import sys
import os.path
import numpy as np
import pafy
import soundfile as sf 
import json
import subprocess as sp
from tqdm import tqdm

# Set output settings
audio_codec = 'flac'
audio_container = 'flac'
video_codec = 'h264'
video_container = 'mp4'

video_save_path = 'vatex_public_test_english/video'
audio_save_path =  'vatex_public_test_english/audio'

download_json_file = "/home/v-detaixin/VATEX/vatex_public_test_english_v1.1.json"
with open(download_json_file, "r") as f:
    download_infos = json.load(f)
print(len(download_infos))

dl_list = []
for i in range(len(download_infos)):
    videoID = download_infos[i]["videoID"]
    video_id = videoID[:11]
    start_time = videoID[11:].split("_")[1]
    end_time = videoID[11:].split("_")[2]
    dl_list.append((video_id, start_time, end_time))

print(dl_list[0], dl_list[1000])

# ! pip install git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl


for i in tqdm(range(len(dl_list))):
    ytid, ts_start, ts_end = dl_list[i]

    # Get the URL to the video page
    video_page_url = 'https://www.youtube.com/watch?v={}'.format(ytid)

    # Get the direct URLs to the videos with best audio and with best video (with audio)
    video = pafy.new(video_page_url)

    best_video = video.getbestvideo()
    best_video_url = best_video.url
    print("Video URL: " + best_video_url)

    best_audio = video.getbestaudio()
    best_audio_url = best_audio.url
    print("Audio URL: " + best_audio_url)

    # Get output video and audio filepaths
    basename_fmt = '{}_{}_{}'.format(ytid, ts_start, ts_end)
    video_filepath = os.path.join(video_save_path, basename_fmt + '.' + video_container)
    audio_filepath = os.path.join(audio_save_path, basename_fmt + '.' + audio_codec)

    try:
        video_command = 'ffmpeg' + ' ' + '-n' + ' ' + '-ss' + ' ' + str(int(ts_start)) + ' ' + '-i' + ' ' + '"' + best_video_url + '"' + ' ' + '-t' + ' ' + str(int(ts_end) - int(ts_start)) + ' ' + '-f' + ' ' + video_container + ' ' + '-framerate' + ' ' + '30' + ' ' + '-vcodec' + ' ' + 'h264' + ' ' + video_filepath
        print(video_command)
        os.system(video_command)
    except:
        pass

    try:
        audio_command = 'ffmpeg' + ' ' + '-n' + ' ' + '-ss' + ' ' + str(int(ts_start)) + ' ' + '-i' + ' ' + '"' + best_audio_url + '"' + ' ' + '-t' + ' ' + str(int(ts_end) - int(ts_start)) + ' ' + '-vn' + ' ' + '-ac' + ' ' + '2' + ' ' + '-sample_fmt' + ' ' + 's16' + ' ' + '-acodec' + ' ' + audio_codec + ' ' + '-ar' + ' ' + '44100' + ' ' + audio_filepath
        print(audio_command)
        os.system(audio_command)
    except:
        pass

