import numpy as np
import matplotlib.pyplot as plt
import pygame
from pygame.constants import JOYAXISMOTION
from joystick_sound_game import JoystickSoundGame

if __name__ == "__main__":
    pygame.init()
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)

    test_class = JoystickSoundGame(440, (-100, 100), initial_state=350)

    iterations = 200
    state_response_log = np.zeros((3, iterations))
    for i in range(iterations):
        print(iterations-i)
        test_class.update_joystick_input(pygame.event.get())

        ctr_state = test_class.get_ctr_state()
        state_response_log[0, i] = ctr_state['set_point']
        state_response_log[1, i] = ctr_state['state']
        state_response_log[2, i] = ctr_state['error']
        pygame.time.wait(1)

    plt.plot(state_response_log[0, :], label='Setpoint')
    plt.plot(state_response_log[1, :], label='State')
    plt.legend()
    plt.savefig("step_response.png")
