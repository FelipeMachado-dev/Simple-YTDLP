import yt_dlp

def DownloadVideo(url):
    
    quality_choose = input("VIDEO QUALITY (360, 480, 720, 1080, 1440): ")
    
    quality_options ={
        '360': 'bestvideo[height<=360]+bestaudio/best',
        '480': 'bestvideo[height<=480]+bestaudio/best',
        '720': 'bestvideo[height<=720]+bestaudio/best',
        '1080': 'bestvideo[height<=1080]+bestaudio/best',
        '1440': 'bestvideo[height<=1440]+bestaudio/best',
    }
        
    quality = quality_options.get(quality_choose, 'bestvideo+bestaudio')

    path = 'C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Videos/' + '/%(title)s'
#'C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Videos/'
    ydl_opts = {
        'format': quality,
        'outtmpl': path,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

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

while True:
    print("SELECT ONE OPTION:\n" \
    "1- DOWNLOAD VIDEO\n" \
    "2- DOWNLOAD AUDIO\n" \
    "3- EXIT\n")

    opt = input("OPTION: ")

    if opt == "1":
        url = input("URL: ")
        DownloadVideo(url)
    elif opt == "2":
        url = input("URL: ")
        DownloadAudio(url)
    elif opt == "3":
        break
    else:
        print("\nINVALID OPTION\n")   
