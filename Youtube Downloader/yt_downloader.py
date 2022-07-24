#Importación de la libreria
from pytube import YouTube


link = 'Aqui va tu link :)'
yt = YouTube(link)

#Obtener el titulo del video
print('Titulo: ', yt.title)
#Obtener las vistas del video
print('Vistas: ', yt.views)

#Descargar el video con la mayor resolución
yd = yt.streams.get_highest_resolution()


yd.download()