from typing import Tuple
import pygame
from pygame.constants import JOYAXISMOTION
from sound_game import SoundGame


class JoystickSoundGame(SoundGame):
    def __init__(self, set_point: float, ctr_interval: Tuple, initial_state=0):

        self._joystick_gain = 5
        self._joystick_input = 0
        SoundGame.__init__(self, set_point, ctr_interval, initial_state)

    def update_joystick_input(self, events):
        """Listens to all pygame events and automatically extracts a joystick axis event.
           This event is then used to set the update to the system

        Args:
            events Pygame.events : Events returned by `pygame.event.get()`
        """
        for event in events:
            if event.type == JOYAXISMOTION:
                if event.axis == 1:  # axis 1 is forward/backward movement
                    self._joystick_input = -1 * event.value * \
                        self._joystick_gain  # -1 so that forward is up

        self.input_ctr_action(self._joystick_input)
