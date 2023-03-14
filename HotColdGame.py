#!/usr/bin/env python

"""Proof of concept gfxdraw example"""

import pygame
import pygame.gfxdraw
import random

# game data that never changes
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 233, 0)

SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# game data that can change values
game = {
    'circle_size': 50,          # 50 = level 1, 25 = level 2, 10 = level 3
    'move_size': 50,            # 50 = level 1, 25 = level 2, 10 = level 3
    'prev_x': 0,                # used to determine if getting hotter or colder
    'prev_y': 0,                # used to determine if getting hotter or colder
    'user_x': SCREEN_SIZE / 2,  # centered based on half of the screen size
    'user_y': SCREEN_SIZE / 2,  # centered based on half of the screen size
    'hidden_x': 0,              # randomly generated based on screen size
    'hidden_y': 0,              # randomly generated based on screen size
    'user_color': WHITE,        # right at the start of the game, but will change to red, blue or green
    'hidden_color': BLACK,      # will make the hidden circle the same color as background
    'num_moves': 0              # keep track of the current number of moves

}

def main():

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screen.fill((0, 0, 0))
    s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
    pygame.draw.line(s, (0, 0, 0), (250, 250), (250 + 200, 250))

    width = 1
    for a_radius in range(width):
        radius = 200
        pygame.gfxdraw.aacircle(s, 250, 250, radius - a_radius, (0, 0, 0))

    screen.blit(s, (0, 0))

    pygame.draw.circle(screen, "green", (50, 100), 10)
    pygame.draw.circle(screen, "pink", (50, 50), 20, 5)

    pygame.display.flip()
    try:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
            pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
