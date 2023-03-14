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

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((0, 0, 0))
s = pygame.Surface(screen.get_size(), pygame.SRCALPHA, 32)
pygame.draw.line(s, (0, 0, 0), (250, 250), (250 + 200, 250))

width = 1

posx = 250
posy = 250

"""
def play_music():


def set_difficulty(level, difficulty):


def display_text():


def set_random_position():


def set_circle_colors():

    
def play_game():
"""

def draw_circle():
    circle = pygame.draw.circle(screen, 'WHITE', (posx, posy), 40)
    circle

def main():
    """
    for a_radius in range(width):
        radius = 200
        pygame.gfxdraw.aacircle(s, 250, 250, radius - a_radius, (0, 0, 0))

    screen.blit(s, (0, 0))
    """
    draw_circle()

    pygame.display.flip()

    try:
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    posx = posx + 10
                if event.key == pygame.K_ESCAPE or event.unicode == "q":
                    break
                screen.fill(BLACK)
                pygame.draw.circle(screen, 'WHITE', (posx, posy), 40)
                pygame.display.flip()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
