from tkinter import * 
import pytube

link = 'https://youtu.be/1MzHInax0eE'

yt = pytube.YouTube(link)

yt.streams.first().download()

print('O download esta sendo efetuado')