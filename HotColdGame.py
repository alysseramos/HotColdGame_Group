import pygame           # Importing pygame allows us to have all the available modules into the pygame package
import pygame.mixer     # Importing pygame.mixer loads the audio file into the program
import pygame_menu      # Importing pygame.menu is for creating menus and GUIs
import random           # Importing random allows the program to generate a random number/location

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 153, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)
gray = (128, 128, 128)

colorcircle = white  # This is the user color at the beginning of the game
hidden_color = black  # This is hidden color of the hidden circle. It is black to blend into the background

# Set the screen size using a tuple of screen_width and screen_height.
# In this case, the screen size is set to 800 pixels by 800 pixels.
screen_size = screen_width, screen_height = 800, 800

# Create a Pygame display window using the screen size tuple.
# The set_mode() method returns a Pygame Surface object that can be used to draw on the display.
screen = pygame.display.set_mode(screen_size)

# Define a constant SCREEN_SIZE to hold the value 800.
SCREEN_SIZE = 800

# Create another Pygame display window using a tuple with the constant SCREEN_SIZE twice.
# The set_mode() method returns a Pygame Surface object that can be used to draw on the display.
SCREEN = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# At the beginning of the game, it is placing the users circle in the middle of the screen
posx = 400
posy = 400

# Storing values to equal zero. These values are the hidden circles x and y coordinates.
# These values change once set_random_position is ran
hidden_x = 0
hidden_y = 0

circle_size = 0  # The size of the circle, this value changes once the set_difficulty is chosen. Storing as zero for now

# This is how much the circle moves. This value changes once set_difficulty is chosen. Storing as zero for now
move_size = 0

num_moves = 0   # This counts how many moves the user takes to find the hidden circle

# This is the users previous x and y position. This is currently storing as zero but will change in set_circle_color
# This will help us determine if the user is getting further away from the hidden circle or closer
previous_x = 0
previous_y = 0


def set_difficulty(level, difficulty):
    """
    This function is ran once the user has selected what difficulty he/she would like to play the game at. The user gets
    three options. Easy, Medium, or Hard. The difficulty changes the circle size and how far the circle moves.
    :param level: This stores the name of each difficulty. Easy, Medium, Hard
    :param difficulty: This is the difficulty level. Easy, Medium, and Hard are equaled to 1,2,3.
    """
    global circle_size, move_size   # Bring in the circle_size and the move_size, so it has the ability to change

    # This is Easy mode.
    if difficulty == 1:
        circle_size = 50
        move_size = 50

    # This is Medium mode
    elif difficulty == 2:
        circle_size = 25
        move_size = 25

    # This is Hard mode
    elif difficulty == 3:
        circle_size = 10
        move_size = 10


def set_circle_color():
    """
    This function changes the hidden circle and user circle colors. If the user circle is getting further away from the
    hidden circle, it changes the user circle to blue. If the user circle is getting closer to the hidden circle it
    changes the user circle to red. If the user circle is on top/overlapping the hidden circle, it changes the hidden
    circle and the user circle to green.
    """
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

        # store the current x, y to previous x, y to get ready for the new user's move
        previous_x = posx
        previous_y = posy

    # This if statement changes the users color to white when the user is at the center
    if posx == 400:
        if posy == 400:
            colorcircle = white
        return

    # store the current x, y to previous x, y to get ready for the new user's move
    previous_x = posx
    previous_y = posy


def display_text():
    """
    This function displays the in game text on the screen. It reminds the users how to debug the program, how to
    restart, and also how to go back to the home. It also tells the user how many moves they have done. Lastly, this
    function promotes a message once the user finds the hidden circle.
    """
    font = pygame.font.SysFont(None, 24)  # This is the font type and font size.

    line = font.render('#' + str(num_moves) + " Moves", True, yellow)
    SCREEN.blit(line, (50, 50))  # The location on the screen

    line = font.render("D = Debug", True, yellow)
    SCREEN.blit(line, (700, 50))  # The location on the screen

    line = font.render("R = Restart", True, yellow)
    SCREEN.blit(line, (700, 70))  # The location on the screen

    line = font.render("H = Home", True, yellow)
    SCREEN.blit(line, (700, 90))  # The location on the screen

    # When the user finds the hidden circle, it displays one last message
    if hidden_color == green:
        line = font.render('You found the circle in #' + str(num_moves) + " moves!", True, yellow)
        SCREEN.blit(line, (265, 400))  # The location on the screen


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
    """
    This function actually runs the game. This function allows the user to move their circle up, down, left and right.
    It counts the total number of moves, allows the user to Debug, go back to the home page or restart the game.
    """
    # Brings in these variables. All are subject to change
    global posx, posy, hidden_color, hidden_x, hidden_y, num_moves

    clock = pygame.time.Clock()

    # This sets the random position of the hidden circle
    set_random_position()

    run_me = True

    while run_me:
        # Limits the game to be played at 60FPS
        clock.tick(60)

        for event in pygame.event.get():
            # Allow the user to x out of the program
            if event.type == pygame.QUIT:
                run_me = False

            # Left arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # This if statement makes sure the circle does not travel off the screen
                    if posx > circle_size:
                        # Move the circle by the level of difficulty the user has chosen (either by 50, 25 or 10)
                        posx = posx - move_size
                        # If the user has not found the hidden circle, add one to the total number of moves
                        if hidden_color != green:
                            num_moves = num_moves + 1

            # Right arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # This if statement makes sure the circle does not travel off the screen
                    if posx < 800 - circle_size:
                        # Move the circle by the level of difficulty the user has chosen (either by 50, 25 or 10)
                        posx = posx + move_size
                        # If the user has not found the hidden circle, add one to the total number of moves
                        if hidden_color != green:
                            num_moves = num_moves + 1

            # Up arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # This if statement makes sure the circle does not travel off the screen
                    if posy > circle_size:
                        # Move the circle by the level of difficulty the user has chosen (either by 50, 25 or 10)
                        posy = posy - move_size
                        # If the user has not found the hidden circle, add one to the total number of moves
                        if hidden_color != green:
                            num_moves = num_moves + 1

            # Down arrow key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    # This if statement makes sure the circle does not travel off the screen
                    if posy < 800 - circle_size:
                        # Move the circle by the level of difficulty the user has chosen (either by 50, 25 or 10)
                        posy = posy + move_size
                        # If the user has not found the hidden circle, add one to the total number of moves
                        if hidden_color != green:
                            num_moves = num_moves + 1

            # Debug (D) key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    # If user has already found the hidden circle, keep hidden circle color to green
                    if hidden_color == green:
                        hidden_color = green
                    else:
                        hidden_color = gray

            # Restart (R) key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Set a new random position
                    set_random_position()
                    # Move user circle back to the center
                    posx = 400
                    posy = 400
                    # Insure the hidden circle color is hidden to the user
                    hidden_color = black
                    # Reset the number of moves
                    num_moves = 0

            # Home (H) key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    # Move user circle back to the center
                    posx = 400
                    posy = 400
                    # Insure the hidden circle color is hidden to the user
                    hidden_color = black
                    # Reset the number of moves
                    num_moves = 0
                    # Run display menu, gives the user a chance to change difficulty/see how to play/quit
                    display_menu()

        # Fills the screen with black (otherwise, the circle will leave a trail)
        screen.fill(black)

        # Draws both circles
        pygame.draw.circle(screen, colorcircle, (posx, posy), circle_size)
        pygame.draw.circle(screen, hidden_color, (hidden_x, hidden_y), circle_size)

        display_text()

        # This displays the pygame window
        pygame.display.flip()

        set_circle_color()

    # Without this, user can not x out of program completely
    pygame.display.quit()


def display_menu():
    pygame.display.set_caption('Hot Cold Game')
    img = pygame.image.load('HotColdIconImage.png')
    pygame.display.set_icon(img)

    menu = pygame_menu.Menu('Hot Cold Game', 600, 500, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Difficulty : ', [(' Easy ', 1), ('Medium', 2), (' Hard ', 3)], onreturn=set_difficulty('', 1),
                      onchange=set_difficulty)
    menu.add.button('Play', play_game)
    menu.add.button('How To Play', lambda: how_to_play_menu(menu))
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(SCREEN)


def how_to_play_menu(menu):
    instructions = "Objective: Find the hidden circle\n" \
                   "Use the arrow keys to move\n" \
                   "Red circle = Closer to hidden circle\n" \
                   "Blue circle = Further from hidden circle\n" \
                   "White circle = Center of the screen\n"
    menu.clear()
    menu.add.label(instructions)
    menu.add.button('Back', display_menu)


def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load('Fluffing-a-Duck.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)


def main():
    pygame.init()

    play_music()
    display_menu()


if __name__ == '__main__':
    main()
