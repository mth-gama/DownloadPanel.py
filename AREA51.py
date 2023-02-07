from pytube import YouTube


#link = input('Link do video: ')
link = 'https://youtu.be/1MzHInax0eE'
# yt = YouTube(link)
def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Status: {round(pct_completed, 2)} %")
    
yt = YouTube(
        link,
        on_progress_callback=on_progress,
        use_oauth=False,
        allow_oauth_cache=True
    )

out = yt.streams\
    .filter(progressive=True, file_extension='mp4')\
    .order_by('resolution')\
    .desc()\
    .first()\
    .download()
#printando titulo do video selecionado
print(yt.title)

#Exibe o link da tumbnail do video
print(yt.thumbnail_url)

