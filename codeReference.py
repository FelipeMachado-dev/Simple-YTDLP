import yt_dlp
from PySide6.QtCore import QThread, Signal
'''
Download a video, selecting the download path and video quality, if dosent set a video quality
by default it gets the highter avaiable, and if download path is not selected or invalid,
it'll be downloaded in the same folder as the .exe
'''
class teste(QThread):
    progress_changed = Signal(int)
    finished = Signal(str, bool)

    def download(url, audio, playlist, quality):
        if audio:
            path = 'C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Videos/' + '/%(title)s'

            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': path,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(url)
        else:
            quality_options ={
            '360p': 'bestvideo[height<=360]+bestaudio/best',
            '480p': 'bestvideo[height<=480]+bestaudio/best',
            '720p': 'bestvideo[height<=720]+bestaudio/best',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best',
            '1440p': 'bestvideo[height<=1440]+bestaudio/best',
        }
            
        quality = quality_options.get('bestvideo+bestaudio')

        path = 'C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Videos/' + '/%(title)s'

        ydl_opts = {
            'format': quality,
            'outtmpl': path,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    








    def DownloadVideo(url):
        
        quality_choose = input("VIDEO QUALITY (360, 480, 720, 1080, 1440): ")
        
        quality_options ={
            '360p': 'bestvideo[height<=360]+bestaudio/best',
            '480p': 'bestvideo[height<=480]+bestaudio/best',
            '720p': 'bestvideo[height<=720]+bestaudio/best',
            '1080p': 'bestvideo[height<=1080]+bestaudio/best',
            '1440p': 'bestvideo[height<=1440]+bestaudio/best',
        }
            
        quality = quality_options.get(quality_choose, 'bestvideo+bestaudio')

        path = 'C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Videos/' + '/%(title)s'

        ydl_opts = {
            'format': quality,
            'outtmpl': path,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)

    # Download only the audio from a video, ignoring the video format and converting to MP3

    def DownloadAudio(url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': "C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Audios/%(title)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)

    # Temporary menu used to test the functionalities of the program 
