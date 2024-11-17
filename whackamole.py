import pygame
import random

WIDTH = 640
HEIGHT = 512
GRID_SIZE = 32
LINE_WIDTH = 1 #what is it supposed to be??
BOARD_ROWS = 16
BOARD_COLS = 20
SQUARE_SIZE = 32
# SPACE = 55
# RED = (255, 0, 0)
# BG_COLOR = (255, 255, 245)
LINE_COLOR = (0, 0, 0)
GAME_OVER_FONT = 40


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Whackamole")
mole_image = pygame.image.load("mole.png")


def draw_grid():
    #draw horizontal lines
    for i in range (1,BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i*SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    # pygame.draw.line(screen, "darkblue", (32, 0), (32, 512))
    #draw vertical grids
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH)

def get_cell_from_mouse_pos(pos):
    x, y = pos
    col = x // (SQUARE_SIZE)
    row = y // (SQUARE_SIZE)
    return row, col

def draw_mole(mole_position):
    row, col = mole_position
    x = (col * SQUARE_SIZE) + (SQUARE_SIZE // 2)
    y = (row * SQUARE_SIZE) + (SQUARE_SIZE // 2)
    mole_surf = mole_image.get_rect(center=(x, y))
    #screen.blit(mole_image, (x, y))
    screen.blit(mole_image, mole_surf)


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_position = (0, 0)

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    clicked_cell = get_cell_from_mouse_pos(mouse_pos)
                    print(f" clicked cell: {clicked_cell}")
                    print(f" mole position: {mole_position}")
                    if clicked_cell == mole_position:
                        mole_position = (random.randint(0, BOARD_ROWS - 1), random.randint(0, BOARD_COLS - 1))
                        print("clicked mole")


                    x, y = event.pos
                    print(event.pos)


            screen.fill("light blue")
            draw_grid()
            draw_mole(mole_position)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()




if __name__ == "__main__":
    main()
