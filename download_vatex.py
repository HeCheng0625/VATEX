import wget
import os
import json
from tqdm import tqdm
from pytube import YouTube

download_json_file = "/home/v-detaixin/VATEX/vatex_public_test_english_v1.1.json"
with open(download_json_file, "r") as f:
    download_infos = json.load(f)
print(len(download_infos))

output_dir = "/home/v-detaixin/VATEX/vatex_public_test_english"

# for i in tqdm(range(10)):
#     videoID = download_infos[i]["videoID"]
#     video_id = videoID[:11]
#     start_time = videoID[11:].split("_")[1]
#     end_time = videoID[11:].split("_")[2]
#     youtube_url = f"https://www.youtube.com/watch?v={video_id}"
#     yt = YouTube(youtube_url)
#     video_stream = yt.streams.filter(file_extension="mp4").first()

#     output_path = f"{output_dir}/{video_id}_{start_time}_{end_time}.mp4"
#     video_stream.download(output_path=output_path)



