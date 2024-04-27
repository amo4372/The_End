import settings
import winsound

def play(music):
	if settings.play_music_state:
		winsound.PlaySound(music, winsound.SND_ASYNC | winsound.SND_ALIAS)
def stop():
	winsound.PlaySound(None, winsound.SND_ASYNC)