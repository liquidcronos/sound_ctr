from typing import Tuple
import pygame
import numpy as np


class SoundGame:
    def __init__(self, set_point: float, ctr_interval: Tuple, initial_state=0):
        self._sample_rate = 44100
        self._amp = 4096

        self._set_point = set_point
        self.ctr_interval = ctr_interval
        self._ctr_action = ctr_interval[0]
        self._state = initial_state

        pygame.mixer.init(frequency=self._sample_rate,
                          size=-16, channels=2, buffer=2**12)

        self.buffer_length = int(44100 * 0.25)
        buf = np.zeros((self.buffer_length, 2), dtype=np.int16)
        sound = pygame.sndarray.make_sound(buf)
        self.buf = pygame.sndarray.samples(sound)

        sound.play(-1)

    def _set_sound_buffer(self, left_freq: float, right_freq: float):
        """Modifies the soundbuffer which is used to create sounds

        Args:
            left_freq (float): frequency of the sound in the left audio channel
            right_freq (float): frequency of the sound in the right audio channel
        """
        for i in range(0, self.buffer_length):
            self.buf[i][0] = self._amp*np.sin(2 * np.pi * i *
                                              left_freq / self._sample_rate)
            self.buf[i][1] = self._amp*np.sin(2 * np.pi * i *
                                              right_freq / self._sample_rate)

    def change_set_point(self, new_set_point: float):
        """Set the set point of the sound game to a new value

        Args:
            new_set_point (float): new set point
        """
        self._set_point = new_set_point
        self._set_sound_buffer(self._set_point, self._ctr_action)

    def _system_update(self, ctr_action: float):
        """Dynamic model used to update the state given the input

        Args:
            ctr_action (float): input
        """
        self._state = self._state + ctr_action

    def input_ctr_action(self, new_ctr_action: float):
        """Function to set a new control action of the game.

        This function should be used to interact with the game

        Args:
            new_ctr_action (float): the new control action

        Raises:
            ValueError: if the control action is not within the set range given during init
        """
        if not new_ctr_action >= self.ctr_interval[0] or \
           not new_ctr_action <= self.ctr_interval[1]:
            raise ValueError('input not within the control interval')
        self._ctr_action = new_ctr_action
        self._system_update(self._ctr_action)
        self._set_sound_buffer(self._set_point, self._state)

    def get_ctr_state(self):
        """Function returning the current state of the system for logging or publishing

        Returns:
            Dict: A dictionary containing the state of the system
                  including the error and last input
        """
        ctr_state = {'set_point': self._set_point,
                     'state': self._state,
                     'ctr_action': self._ctr_action,
                     'error': self._set_point - self._state}
        return ctr_state
