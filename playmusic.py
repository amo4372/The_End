import settings
import winsound

def play(music):
    if settings.play_music_state:
        winsound.PlaySound(music, winsound.SND_ASYNC | winsound.SND_LOOP | winsound.SND_ALIAS)
def stop():
    winsound.PlaySound(None, winsound.SND_ASYNC)
def sound_play(sound):
    winsound.PlaySound(sound, winsound.SND_ASYNC | winsound.SND_ALIAS)