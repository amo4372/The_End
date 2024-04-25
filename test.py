import pygame

def play(music):
	pygame.mixer.init()
	pygame.mixer.music.load(music)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
path = "music/HOYO-MiX - 轻涟 La vaguelette.mp3"
play(path)