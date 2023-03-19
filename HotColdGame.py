import os, sys, math, pygame, pygame.mixer
from pygame.locals import *
import random

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


SCREEN_SIZE = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(SCREEN_SIZE)



# fps_limit = 60

colorcircle = white
hidden_color = black
posx = 400
posy = 400
circle = pygame.draw.circle(screen, colorcircle, (posx, posy), 50)
hidden_circle = pygame.draw.circle(screen, hidden_color, (200, 200), 50)


def set_random_position():

    global game

user_pos = SCREEN_SIZE / 2

inside_dist = game['circle_size']
outside_dist = SCREEN_SIZE - game['circle_size']

right_user_dist = user_pos - game['circle_size']
left_user_dist = user_pos + game['circle_size']

while True:

    x = random.randint (inside_dist, outside_dist)
    y = random.randint (inside_dist, outside_dist)

    if ( x < right_user_dist or x > left_user_dist) and ( y < right_user_dist or y > left_user_dist):
        game['hidden_x'] = x
        game['hidden_y'] = y





def play_game():

    global posx, posy, hidden_color

    clock = pygame.time.Clock()

    # set_random_position()

    run_me = True



    while run_me:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posx = posx - 10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    posx = posx + 10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    posy = posy - 10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    posy = posy + 10
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    hidden_color = green

        # fill the screen with black (otherwise, the circle will leave a trail)
        screen.fill(black)
        # redraw the circle
        pygame.draw.circle(screen, colorcircle, (posx, posy), 50)

        pygame.draw.circle(screen, hidden_color, (200, 200), 50)
        pygame.display.flip()


def main():

    pygame.init()
    pygame.display.set_caption('Hot Cold Game')

    play_game()

    pygame.quit()


if __name__ == '__main__':
    main()
