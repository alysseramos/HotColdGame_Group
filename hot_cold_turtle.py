#!/usr/bin/env python3

"""
The Hot/Cold Game

The user has to try to find a hidden circle using his circle to move around the screen.
The game's objective is to see how many moves it takes you to find a hidden circle
on the screen using another circle to navigate.

The hidden circle (same color as the screen background) will be randomly placed on the screen

The user’s circle will always start in the center of the screen

Allow the user to select the difficulty of the game by controlling the size of the circle
and the distance it moves on each attempt

The user’s circle will be red (hot) when getting closer or blue (cold) when getting further away from the hidden circle

The game has the following key options:
Up, Down, Left, and Right arrows
D = Toggle debug mode (displays the display the hidden circle)
H = Move the user’s circle home position x=0, y=0
R = Reset the game

The game will always display a running total of the number of moves
"""

__author__ = 'Debbie Johnson'
__version__ = '1.0'
__copyright__ = "Copyright 2022.03.01, Midterm Assignment"
__github__ = "https://github.com/dejohns2/CSC365_Spring2022_Code_Examples"

import turtle  # used to config the screen and turtle (pen used to draw with)
import random  # used to randomly place the hidden circle on the screen


# global variables used to control the game
s = None           # used to configure the screen
t = None           # pen used to draw the circles and text on the screen
num_moves = 0      # running total of the number of moves to find the hidden circle
circle_size = 100  # set the difficulty of the game by the size of the circles
move_size = 100    # set the difficulty of the game by the size of the circles

# previous location of the user's circle used to determine if the user is getting closer or further away
previous_x = 0
previous_y = 0

# current location of the user's circle
x = 0  # start at the center of screen and used to move right (+) or left (-)
y = 0  # start at the center of screen and used to move up (+) or down (-)

# used to control the hidden circle location
hidden_x = 0  # from the center of the screen right (+) left (-)
hidden_y = 0  # from the center of the screen up (+) down (-)

user_color = 'blue'     # the color of the user's circle: (closer) cold=blue, (further) hot=red
hidden_color = 'black'  # the default for the hidden circle is black to match the screen background color


def set_center_location():
    """
    user's circle will be placed in the middle of the screen based on the circle size
    divide the circle size in half and then move to down (-y) and to the left (-x) by multiplying by -1
    :return: None
    """
    global x, y

    # user's circle will be placed in the middle of the screen based on the circle size
    # divide the circle size in half and then move to down (-y) and to the left (-x) by multiplying by -1
    center_pos = int(circle_size / 2) * -1

    x = center_pos  # user's circle will be in the center of screen moving right or left
    y = center_pos  # user's circle will be placed in the screen moving up or down


def set_hidden_location():
    """
    This function will keep looping until a valid hidden location is generated
    Generate a random x & y location for the hidden circle based on the default screen size
    Making sure that the hidden circle isn't too close to the user's circle and
    abs(x) & abs(y) can't be within twice the user's circle size + 10

    left & right max: -420 & 420
    bottom & top max: -300 & 300

    :return: None
    """
    global hidden_x, hidden_y

    while True:
        hidden_x = random.randint(-420, 420)  # left & right position max
        hidden_y = random.randint(-300, 300)  # bottom & top position max

        # make sure the hidden circle isn't too close to the user's circle
        # can't be within twice the user's circle size + 10
        if abs(hidden_x) > (circle_size * 2 + 10) and abs(hidden_y) > (circle_size * 2 + 10):
            break


def set_circle_color():
    """
    set the amount the user's circle must overlap by the dimension of both circles added together minus 10
    if the circle overlap
        then set both circles to different green colors
    else
        if the user's circle x location has changed then determine if they are closer or further away from previous x
            if previous x distance is less than current x distance
            then set red else blue
        if the user's circle y location has changed then determine if they are closer or further away from previous y
            if previous y distance is less than current y distance
            then set red else blue
    store the current x, y to previous x, y to get ready for the new user's move
    :return: None
    """
    global previous_x, previous_y, user_color, hidden_color

    # set the amount the user's circle must overlap by the dimension of both circles added together minus 10
    overlap = circle_size * 2 - 10

    # if the circle overlap then set both circles to different green colors
    if abs(x - hidden_x) < overlap and abs(y - hidden_y) < overlap:
        hidden_color = 'green yellow'
        user_color = 'green'
    else:
        # if the user's circle x location has changed then determine if they are closer or further away from previous x
        if previous_x != x:
            # if previous x distance is less than current x distance then set red otherwise blue
            if abs(previous_x - hidden_x) > abs(x - hidden_x):
                user_color = 'red'
            else:
                user_color = 'blue'

        # if the user's circle y location has changed then determine if they are closer or further away from previous y
        if previous_y != y:
            # if previous y distance is less than current y distance then set red otherwise blue
            if abs(previous_y - hidden_y) > abs(y - hidden_y):
                user_color = 'red'
            else:
                user_color = 'blue'

    # store the current x, y to previous x, y to get ready for the new user's move
    previous_x = x
    previous_y = y


def debug():
    """
    Toggles debug mode making it easier to test the game.
    If the hidden circle color is black (same as the background) change it to gray otherwise change it back to black.
    then call display_game to clear & redraw the screen based on the update hidden color
    :return: None
    """
    global hidden_color

    if hidden_color == 'black':
        hidden_color = 'gray'
    else:
        hidden_color = 'black'

    display_game()


def move_home():
    """
    call the function that set's the user's circle location to the center based on it's size
    then call display_game to clear & redraw the screen based on the update user's circle location
    :return: None
    """
    set_center_location()  # call the function that set's the user's circle location to the center based on it's size
    display_game()


def move_left():
    """
    Subtract move_size from the x coordinate which will be used move the circle to the left
    add one to the user's total moves
    then call display_game to clear & redraw the screen based on the update user's circle location
    :return: None
    """
    global x, num_moves

    x -= move_size  # move to the left of center
    num_moves += 1
    display_game()


def move_right():
    """
    Add move_size to the x coordinate which will be used move the circle to the right
    add one to the user's total moves
    then call display_game to clear & redraw the screen based on the update user's circle location
    :return: None
    """
    global x, num_moves

    x += move_size  # move to the right of center
    num_moves += 1
    display_game()


def move_up():
    """
    Add move_size to the y coordinate which will be used move the circle up
    add one to the user's total moves
    then call display_game to clear & redraw the screen based on the update user's circle location
    :return: None
    """
    global y, num_moves

    y += move_size  # move top of center
    num_moves += 1
    display_game()


def move_down():
    """
    Subtract move_size from y coordinate which will be used move the circle to the down
    add one to the user's total moves
    then call display_game to clear & redraw the screen based on the update user's circle location
    :return: None
    """
    global y, num_moves

    y -= move_size  # move down of center
    num_moves += 1
    display_game()


def display_instructions():
    """
    Display the current total number of user's moves
    and game's instruction on the screen in the upper left-hand corner
    :return: None
    """
    t.penup()            # don't want to see icon moving on the screen
    t.pencolor('white')  # text color
    t.goto(-450, 370)    # from the current position which is center after clear, move left 350 up 350
    t.write("Total moves = " + str(num_moves), font=("Verdana", 12, "bold"))
    t.goto(-450, 330)    # from the current position which is center after clear, move left 350 up 350
    t.write("Use arrows to move", font=("Verdana", 12, "bold"))
    t.goto(-450, 310)    # from the current position which is center after clear, move left 350 up 350
    t.write("d = debug", font=("Verdana", 12, "bold"))
    t.goto(-450, 290)    # from the current position which is center after clear, move left 350 up 350
    t.write("h = home", font=("Verdana", 12, "bold"))
    t.goto(-450, 270)    # from the current position which is center after clear, move left 350 up 350
    t.write("r = reset", font=("Verdana", 12, "bold"))


def display_hidden_circle():
    """
    Display the hidden circle based on the circle size, hidden location (x,y) and hidden color
    :return: None
    """
    t.penup()                   # pickup the pen so it doesn't draw when repositioning it
    t.goto(hidden_x, hidden_y)  # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()                 # start drawing the outline of the circle
    t.pencolor(hidden_color)    # set the outline color
    t.fillcolor(hidden_color)   # set the fill color
    t.begin_fill()              # start the fill of whatever is being drawn
    t.circle(circle_size)       # diameter of the circle
    t.end_fill()                # done drawing the object to complete the fill


def display_user_circle():
    """
    Display the user's circle based on the circle size, location (x,y) and user's color
    :return: None
    """
    t.penup()                   # pickup the pen so it doesn't draw when repositioning it
    t.goto(x, y)                # move to the updated x (left-right) and y (up-down) location from center
    t.pendown()                 # start drawing the outline of the circle
    t.pencolor(user_color)      # set the outline color
    t.fillcolor(user_color)     # set the fill color
    t.begin_fill()              # start the fill of whatever is being drawn
    t.circle(circle_size)       # diameter of the circle
    t.end_fill()                # done drawing the object to complete the fill


def display_game():
    """
    Clear all turtle drawings
    Set the user's circle and hidden circle colors
    Draw the user's circle and the hidden circle
    Display the game instructions
    :return: None
    """
    t.clear()  # clear the previous turtle drawings
    set_circle_color()
    display_hidden_circle()
    display_user_circle()
    display_instructions()


def setup_game():
    """
    Set the number of user's moves to zero
    Set the hidden's circle color to black (same as background)
    Clear the previous game's turtle drawing
    set the screen tracer to false and turtle speed to fastest
    Set the window title and background color
    Get the user's input for the size of the circles and size of the move
    Calculate the where to place the user's circle based on it's size in the center of the screen
    Generate a random location for the hidden circle
    Setup the on key press listeners
    :return: None
    """
    global num_moves, circle_size, move_size, hidden_color

    num_moves = 0           # set the number of user's moves back to zero
    hidden_color = 'black'  # set the hidden circle to black which is the same color as the screen background

    t.clear()                   # clear the screen from the previous game
    s.tracer(False)             # turn animation off which causes screen flickering as the circle gets redrawn
    t.speed('fastest')          # draw quickly
    s.title('Hot Cold Game')    # set the title bar of the window
    s.bgcolor('black')          # set the window's background color which is the came color as the hidden circle

    # try to get the user's choice for the size of the cirle and the size of the movement
    # if the user closes the the inputs without entering a valid value
    # then set the default sizes both to 50
    try:
        circle_size = int(turtle.numinput('Circle', '"Size of circles (10-100)', minval=10, maxval=100))
        move_size = int(turtle.numinput('Circle', 'Size of move (10-100)', minval=10, maxval=100))
    except:
        circle_size = 50
        move_size = 50

    set_center_location()  # call the function that set's the user's circle location to the center based on it's size
    set_hidden_location()   # generate the random x & y location for the hidden circle

    s.onkeypress(debug, 'd')
    s.onkeypress(start_game, 'r')
    s.onkeypress(move_home, 'h')
    s.onkeypress(move_up, 'Up')
    s.onkeypress(move_down, 'Down')
    s.onkeypress(move_right, 'Right')
    s.onkeypress(move_left, 'Left')
    s.listen()  # start listening for keys being pressed


def start_game():
    """
    Calls setup game to configure the game based on user's input
    Display the game
    Keep the screen main looping
    :return: None
    """
    setup_game()    # configure how the turtle window screen will look like
    display_game()  # display the game based on current settings
    s.mainloop()    # keep the turtle window open until the user closes it


# if this is the program starting module, then run the main function
if __name__ == '__main__':
    s = turtle.Screen()     # set the global screen object used to configure the screen
    t = turtle.Turtle()     # set the global pen (cursor) used to draw with
    start_game()            # start the game & keep it looping
