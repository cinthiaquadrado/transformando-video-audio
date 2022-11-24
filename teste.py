import moviepy.editor

#Carregando arquivo de vídeo
video = moviepy.editor.VideoFileClip('agostinho.mp4')

#Extraindo apenas o áudio
audio = video.audio

#Saída de arquivo
audio.write_audiofile('audio_agostinho.mp3')
