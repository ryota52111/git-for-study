import youtube_dl
# ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s','format':'137'})

# with ydl:
#     result = ydl.extract_info(
#         'https://www.youtube.com/watch?v=CkYoNINcruQ&list=RDCkYoNINcruQ&start_radio=1',
#         download=True # We just want to extract the info
#     )

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl':  "sample_music" + '.%(ext)s',
    'postprocessors': [
        {'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
         'preferredquality': '192'},
        {'key': 'FFmpegMetadata'},
    ],
}

ydl = youtube_dl.YoutubeDL(ydl_opts)
info_dict = ydl.extract_info("https://www.youtube.com/watch?v=CkYoNINcruQ&list=RDCkYoNINcruQ&start_radio=1", download=True)