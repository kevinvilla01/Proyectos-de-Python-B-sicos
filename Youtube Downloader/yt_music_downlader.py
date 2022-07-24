#Importación de la libreria
from pytube import YouTube


link = 'Aqui va tu link :)'
yt = YouTube(link)

#Obtener el titulo del video
print('Titulo: ', yt.title)
#Obtener las vistas del video
print('Vistas: ', yt.views)

#Solo tomar el audio
yd = yt.streams.get_audio_only()


yd.download()