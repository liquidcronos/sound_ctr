import pygame
from sound_game import SoundGame


if __name__ == "__main__":
    test_class = SoundGame(0, (-100, 100), initial_state=400)
    pygame.time.wait(int(40))
    test_class.change_set_point(440)
    for i in range(80):
        test_class.input_ctr_action(20)
        pygame.time.wait(1)
