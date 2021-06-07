from pytube import YouTube
link = input("Video Link:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download(filename='Downloads')