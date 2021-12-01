import pygame
import numpy as np

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2**12)
frequency = 440
amp = 4096
sample_rate = 44100

buf = np.zeros((44100, 2), dtype=np.int16)
for i in range(0, sample_rate):
    buf[i][0] = amp*np.sin(2 * np.pi * i * 0.8 *
                           frequency / sample_rate)
    buf[i][1] = amp*np.sin(2 * np.pi * i *
                           frequency / sample_rate)

print(buf)
#sound = pygame.mixer.Sound(buffer=buf)
sound = pygame.sndarray.make_sound(buf)
sound.play(0)
pygame.time.wait(int(sound.get_length() * 1000))
