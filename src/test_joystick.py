import pygame
from pygame.constants import JOYAXISMOTION
from joystick_sound_game import JoystickSoundGame


if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)

    test_class = JoystickSoundGame(440, (-100, 100), initial_state=400)

    while True:
        test_class.update_joystick_input(pygame.event.get())
        ctr_state = test_class.get_ctr_state()
        print(ctr_state['error'])
        pygame.time.wait(1)
