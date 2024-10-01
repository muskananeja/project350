import pygame
from game_files.function import Main

pygame.init()
pygame.font.init()

if __name__ == "__main__":
    """
    Initializes the game window and starts the main game loop.
    """
    window_size = (602, 602)  # Size of the game window
    # Size of the screen including the sidebar
    screen_size = (window_size[0] + 150, window_size[1])
    tile_size = 30  # Size of each tile in the grid

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("LookBack Maze")

    game = Main(screen)
    game.main(window_size, tile_size)
