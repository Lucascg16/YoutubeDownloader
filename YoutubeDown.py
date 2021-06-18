from pytube import YouTube
print('Bem-Vindo ao YoutubeDownloader, insira o link do video que deseja baixar.')
print('Ele irá aparecer na pasta onde o script esta localizado.')
link = input("Video Link:")
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()