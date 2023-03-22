import pygame
import pygame.mixer
import pygame_menu
import random

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 153, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
YELLOW = (255, 255, 0)
gray = (128, 128, 128)

screen_size = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(screen_size)

SCREEN_SIZE = 800
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

colorcircle = white
hidden_color = black
posx = 400
posy = 400
circle_size = 50
hidden_x = 200
hidden_y = 200
move_size = 0

num_moves = 0

previous_x = 0
previous_y = 0


def set_difficulty(level, difficulty):

    global circle_size, move_size

    if difficulty == 3:
        circle_size = 10
        move_size = 10
    elif difficulty == 2:
        circle_size = 25
        move_size = 25
    else:
        circle_size = 50
        move_size = 50


def set_circle_color():

    global previous_x, previous_y, hidden_color, colorcircle, posy, posx, hidden_x, hidden_y

    # set the amount the user's circle must overlap by the dimension of both circles added together minus 9
    overlap = circle_size * 2 - 9

    # if the circle overlap then set both circles to different green colors
    if abs(posx - hidden_x) < overlap and abs(posy - hidden_y) < overlap:
        hidden_color = green
        colorcircle = (115, 230, 0)
    else:
        # if the user's circle x location has changed then determine if they are closer or further away from previous x
        if previous_x != posx:
            # if previous x distance is less than current x distance then set red otherwise blue
            if abs(previous_x - hidden_x) > abs(posx - hidden_x):
                colorcircle = red
            else:
                colorcircle = blue

        # if the user's circle y location has changed then determine if they are closer or further away from previous y
        if previous_y != posy:
            # if previous y distance is less than current y distance then set red otherwise blue
            if abs(previous_y - hidden_y) > abs(posy - hidden_y):
                colorcircle = red
            else:
                colorcircle = blue

    if posx == 400:
        if posy == 400:
            colorcircle = white
        return

    # store the current x, y to previous x, y to get ready for the new user's move
    previous_x = posx
    previous_y = posy


def display_text():

    font = pygame.font.SysFont(None, 24)

    line = font.render("Find the hidden circle", True, YELLOW)
    SCREEN.blit(line, (50, 50))

    line = font.render("Use arrows to move", True, YELLOW)
    SCREEN.blit(line, (50, 70))

    line = font.render("Red = Warmer", True, YELLOW)
    SCREEN.blit(line, (50, 100))

    line = font.render("Blue = Colder", True, YELLOW)
    SCREEN.blit(line, (50, 120))

    line = font.render("White = Center", True, YELLOW)
    SCREEN.blit(line, (50, 140))

    line = font.render('#' + str(num_moves) + " Moves", True, YELLOW)
    SCREEN.blit(line, (50, 170))

    line = font.render("D = Debug", True, YELLOW)
    SCREEN.blit(line, (700, 50))

    line = font.render("R = Restart", True, YELLOW)
    SCREEN.blit(line, (700, 70))

    line = font.render("H = Home", True, YELLOW)
    SCREEN.blit(line, (700, 90))

    if hidden_color == green:
        line = font.render('You found the circle in #' + str(num_moves) + " moves!", True, YELLOW)
        SCREEN.blit(line, (265, 400))


def set_random_position():

    global circle_size, hidden_x, hidden_y

    user_pos = SCREEN_SIZE // 2

    inside_dist = circle_size
    outside_dist = SCREEN_SIZE - circle_size
    right_user_dist = user_pos - circle_size
    left_user_dist = user_pos + circle_size

    while True:

        x = random.randint(inside_dist, outside_dist)
        y = random.randint(inside_dist, outside_dist)

        if (x < right_user_dist or x > left_user_dist) and (y < right_user_dist or y > left_user_dist):
            hidden_x = x
            hidden_y = y
            return


def play_game():

    global posx, posy, hidden_color, hidden_x, hidden_y, num_moves

    clock = pygame.time.Clock()

    set_random_position()

    run_me = True

    while run_me:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_me = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    posx = posx - 10
                    num_moves = num_moves + 1
                    if hidden_color == green:
                        num_moves = num_moves - 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    posx = posx + 10
                    num_moves = num_moves + 1
                    if hidden_color == green:
                        num_moves = num_moves - 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    posy = posy - 10
                    num_moves = num_moves + 1
                    if hidden_color == green:
                        num_moves = num_moves - 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    posy = posy + 10
                    num_moves = num_moves + 1
                    if hidden_color == green:
                        num_moves = num_moves - 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    if hidden_color == green:
                        hidden_color = green
                    else:
                        hidden_color = gray

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    set_random_position()
                    posx = 400
                    posy = 400
                    hidden_color = black
                    num_moves = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    posx = 400
                    posy = 400
                    hidden_color = black
                    num_moves = 0
                    display_menu()

        # fill the screen with black (otherwise, the circle will leave a trail)
        screen.fill(black)

        # redraw the circle
        pygame.draw.circle(screen, colorcircle, (posx, posy), circle_size)

        pygame.draw.circle(screen, hidden_color, (hidden_x, hidden_y), circle_size)
        display_text()

        pygame.display.flip()
        set_circle_color()

    pygame.display.quit()


def display_menu():

    pygame.display.set_caption('Hot Cold Game')
    menu = pygame_menu.Menu('Hot/Cold Game', 400, 300, theme=pygame_menu.themes.THEME_BLUE)

    menu.add.selector('Difficulty : ', [(' Easy ', 1), ('Medium', 2), (' Hard ', 3)], onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


def main():

    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load('Fluffing-a-Duck.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    display_menu()
    set_random_position()


if __name__ == '__main__':
    main()
