import curses
from spicy_snake.screen_helpers import prepare_screen
from spicy_snake.playground import Playground

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1) #FIXME: is this correct?
DOWN = (0, 1)

KEY_COMMANDS = {68: LEFT, 67: RIGHT, 65: UP, 66: DOWN}

SNAKE_SYMBOL = "0"
WALL_SYMBOL = "#"


def draw(player_position, pg, win, screen):
    x, y = player_position
    screen.clear()
    # draw the player:
    #TODO: separate function draw_player and draw_playground
    screen.addch(y, x, SNAKE_SYMBOL, curses.color_pair(1))
    # draw the playground:
    for pgx in range(pg.xsize + 1):
        for pgy in range(pg.ysize + 1):
            if pg.is_obstacle((pgx, pgy)):
                screen.addch(pgy, pgx, WALL_SYMBOL, curses.color_pair(2))
    win.refresh()
    screen.refresh()

win, screen = prepare_screen()

def move_player(player_position, direction):
    dx,dy=direction
    x, y = player_position
    x += dx
    y += dy
    return x, y

def game_loop(screen):
    player_position = 5, 5  # player position
    pg = Playground(30, 14)  #FIXME: should this be initialized before?
    draw(player_position, pg, win, screen)

    while True:

        # move the player
        char = win.getch() # returns the code of a pressed key
        direction = KEY_COMMANDS.get(char)  # direction is a tuple or None
        if direction:
            player_position = move_player(player_position, direction)
            draw(player_position, pg, win, screen)

if __name__ == "__main__":

    curses.wrapper(game_loop)
    curses.endwin()
