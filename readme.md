下载 youtube_dl
注意必须是这个版本
pip install git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl

下载 pafy
import pafy

运行 download_vatex.py 即可

只需要修改这三个路径
video_save_path = 'vatex_public_test_english/video'
audio_save_path =  'vatex_public_test_english/audio'
download_json_file = "/home/v-detaixin/VATEX/vatex_public_test_english_v1.1.json"

NOTE:
第一次运行会报错
cd 到 /opt/conda/envs/codec/lib/python3.8/site-packages/pafy
把 backend_youtube_dl.py 第 50 和 54 行注释了
