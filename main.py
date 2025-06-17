import yt_dlp

def DownloadVideo(url):
    ydl_opts = {
        'format': 'bestvideo[height1080]+bestaudio/best',
        'outtmpl': 'C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Videos',
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
        'outtmpl': "C:/Users/Laboratório KIDS/Desktop/Teste YT-DLP/Audios",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)

while True:
    print("SELECT ONE OPTION:\n" \
    "1- DOWNLOAD VIDEO\n" \
    "2- DOWNLOAD AUIDIO\n" \
    "3- EXIT")

    opt = input("")

    if opt == "1":
        DownloadVideo(url = input("URL: "))
    elif opt == "2":
        DownloadAudio(url = input("URL: "))
    elif opt == "3":
        break
    else:
        print("\nINVALID OPTION\n")   
