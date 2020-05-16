from pyfirmata import Arduino, util, INPUT
""" Reference: https://stackoverflow.com/questions/51464455/
why-when-import-pygame-it-prints-the-version-and-welcome-message-how-delete-it/51470016"""
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

PIN = 0
DISPLAY_WIDTH = 80
DISPLAY_HEIGHT = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCALE_FACTOR = 10

board = Arduino('/dev/ttyACM0')
board.analog[PIN].mode = INPUT

values = []


def plot_wave(screen, values):
    """
    Function to plot waveform
    :param screen: pygame object
    :param values: y coordinates, list
    :return: None
    """
    for i in range(0, DISPLAY_WIDTH + 1):
        screen.set_at((i, DISPLAY_HEIGHT - int(values[i] * SCALE_FACTOR)), BLACK)
        print(len(values))
        pygame.display.update()


def main():
    """ Main function"""
    it = util.Iterator(board)
    it.start()
    board.analog[PIN].enable_reporting()

    screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    screen.fill(WHITE)
    pygame.display.update()

    while True:
        value = board.analog[PIN].read()
        # print(value)
        values.append(value)
        if len(values) > DISPLAY_WIDTH:
            values.pop(0)
        if len(values) < DISPLAY_WIDTH:
            for i in range(0, len(values)):
                screen.set_at((i, int(values[i] * SCALE_FACTOR)), BLACK)
                print(len(values))
                pygame.display.update()
        else:
            plot_wave(screen, values)


if __name__ == "__main__":
    main()
