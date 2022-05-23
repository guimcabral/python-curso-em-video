# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import time
import vlc

p = vlc.MediaPlayer('ex021.mp3')
tempo_mp3 = 271

p.play()
time.sleep(tempo_mp3)
