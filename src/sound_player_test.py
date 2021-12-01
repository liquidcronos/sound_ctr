from typing import Tuple
import pygame
import numpy as np


class sound_game:
    def __init__(self, set_point, ctr_interval: Tuple):
        self.sample_rate = 44100
        self.amp = 4096

        self.set_point = set_point
        self.ctr_interval = ctr_interval
        self.ctr_action = ctr_interval[0]

        pygame.mixer.init(frequency=self.sample_rate,
                          size=-16, channels=2, buffer=2**12)

        buf = np.zeros((44100, 2), dtype=np.int16)
        sound = pygame.sndarray.make_sound(buf)
        self.buf = pygame.sndarray.samples(sound)

        sound.play(-1)

    def set_sound_buffer(self, left_freq, right_freq):
        for i in range(0, self.sample_rate):
            self.buf[i][0] = self.amp*np.sin(2 * np.pi * i *
                                             left_freq / self.sample_rate)
            self.buf[i][1] = self.amp*np.sin(2 * np.pi * i *
                                             right_freq / self.sample_rate)

    def change_set_point(self, new_set_point):
        self.set_point = new_set_point
        self.set_sound_buffer(self.set_point, self.ctr_action)

    def input_ctr_action(self, new_ctr_action):
        if not (new_ctr_action >= self.ctr_interval[0]) or not (new_ctr_action <= self.ctr_interval[1]):
            raise ValueError('input not within the control interval')
        self.ctr_action = new_ctr_action
        self.set_sound_buffer(self.set_point, self.ctr_action)


test_class = sound_game(0, (350, 500))
pygame.time.wait(int(20))
test_class.change_set_point(440)
for i in range(20):
    test_class.input_ctr_action(380+10*i)
    pygame.time.wait(int(10))
