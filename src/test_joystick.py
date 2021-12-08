import pygame
from pygame.constants import JOYAXISMOTION
from sound_game import SoundGame


if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    test_class = SoundGame(0, (-100, 100), initial_state=400)
    pygame.time.wait(int(40))
    test_class.change_set_point(440)

    ctr_action = 0
    while True:
        for event in pygame.event.get():
            if event.type == JOYAXISMOTION:
                if event.axis == 1:  # axis 1 is forward/backward movement
                    ctr_action = event.value*5.

        test_class.input_ctr_action(ctr_action)
        ctr_state = test_class.get_ctr_state()
        print(ctr_state['error'])
        pygame.time.wait(1)
