from typing import Tuple
import pygame
import numpy as np


class SoundGame:
    def __init__(self, set_point, ctr_interval: Tuple, initial_state=0):
        self._sample_rate = 44100
        self._amp = 4096

        self.set_point = set_point
        self.ctr_interval = ctr_interval
        self.ctr_action = ctr_interval[0]
        self.state = initial_state

        pygame.mixer.init(frequency=self._sample_rate,
                          size=-16, channels=2, buffer=2**12)

        self.buffer_length = int(44100 * 0.25)
        buf = np.zeros((self.buffer_length, 2), dtype=np.int16)
        sound = pygame.sndarray.make_sound(buf)
        self.buf = pygame.sndarray.samples(sound)

        sound.play(-1)

    def set_sound_buffer(self, left_freq, right_freq):
        for i in range(0, self.buffer_length):
            self.buf[i][0] = self._amp*np.sin(2 * np.pi * i *
                                              left_freq / self._sample_rate)
            self.buf[i][1] = self._amp*np.sin(2 * np.pi * i *
                                              right_freq / self._sample_rate)

    def change_set_point(self, new_set_point):
        self.set_point = new_set_point
        self.set_sound_buffer(self.set_point, self.ctr_action)

    def system_update(self, ctr_action):
        self.state = self.state + ctr_action

    def input_ctr_action(self, new_ctr_action):
        if not (new_ctr_action >= self.ctr_interval[0]) or not (new_ctr_action <= self.ctr_interval[1]):
            raise ValueError('input not within the control interval')
        self.ctr_action = new_ctr_action
        self.system_update(self.ctr_action)
        self.set_sound_buffer(self.set_point, self.state)
