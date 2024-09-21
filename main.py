import pygame
import sys
from maze import Maze
from player import Player
from game import Game
from clock import Clock

pygame.init()
pygame.font.init()

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("cyan")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()
        self.cli_cooldown = 0
        self.is_screen_black = False  # Flag to determine screen color
        self.black_screen_start_time = None  # Variable to store the time when the screen was changed to black
    
    def main(self, frame_size, tile):
        cols, rows = frame_size[0] // tile, frame_size[1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        clock = Clock()

        maze.generate_maze()
        clock.start_timer()

        while self.running:
            # Check if 5 seconds have passed since the screen was changed to black
            if self.is_screen_black and (pygame.time.get_ticks() - self.black_screen_start_time) > 10000:
                self.is_screen_black = False  # Reset the flag to change screen color back to white

            if self.is_screen_black:
                self.screen.fill("black")
            else:
                self.screen.fill("white")
            self.screen.fill(pygame.Color("darkslategray"), (603, 0, 752, 752))

            if self.cli_cooldown > 0:
                self.cli_cooldown -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if not self.game_over:
                        if event.key == pygame.K_LEFT:
                            player.left_pressed = True
                        if event.key == pygame.K_RIGHT:
                            player.right_pressed = True
                        if event.key == pygame.K_UP:
                            player.up_pressed = True
                        if event.key == pygame.K_DOWN:
                            player.down_pressed = True

                if event.type == pygame.KEYUP:
                    if not self.game_over:
                        if event.key == pygame.K_LEFT:
                            player.left_pressed = False
                        if event.key == pygame.K_RIGHT:
                            player.right_pressed = False
                        if event.key == pygame.K_UP:
                            player.up_pressed = False
                        if event.key == pygame.K_DOWN:
                            player.down_pressed = False

            if self.cli_cooldown == 0 and player.check_tower(maze.tower_cell, tile):
                self.enter_cli_mode(player)

            if game.is_game_over(player):
                self.game_over = True
                player.left_pressed = False
                player.right_pressed = False
                player.up_pressed = False
                player.down_pressed = False

            self._draw(maze, tile, player, game, clock)
            self.FPS.tick(60)

    def enter_cli_mode(self, player):
        print("You've reached the CLI Tower! Enter commands. Type 'exit' to resume the game.")
        
        while True:
            command = input("Enter command: ").strip().lower()
            
            if command == "exit":
                print("Exiting CLI mode.")
                self.cli_cooldown = 120
                return
            elif command.startswith("teleport"):
                try:
                    _, x, y = command.split()
                    player.x = int(x) * 30
                    player.y = int(y) * 30
                    print(f"Teleported player to ({x}, {y}).")
                    self.is_screen_black = True  # Set the flag to change screen color
                    self.black_screen_start_time = pygame.time.get_ticks()  # Store the current time
                    self.cli_cooldown = 120
                    return
                except ValueError:
                    print("Invalid teleport command. Use 'teleport x y' format.")
            elif command == "quit":
                pygame.quit()
                sys.exit()
            else:
                print("Unknown command. Available commands: 'teleport x y', 'exit', 'quit'.")

    def _draw(self, maze, tile, player, game, clock):
        """
        Draws all game elements on the screen including maze, player, and time.
        :param maze: Maze object to render.
        :param tile: Size of the tiles/cells in the maze.
        :param player: Player object to render.
        :param game: Game object for game state management.
        :param clock: Clock object for managing time.
        """
        # Draw the maze cells
        [cell.draw(self.screen, tile) for cell in maze.grid_cells]
        
        # Draw the goal point
        game.add_goal_point(self.screen)
        
        # Draw the player character
        player.draw(self.screen)
        
        # Pass the correct arguments to player.update() - tile, grid_cells, and thickness
        player.update(tile, maze.grid_cells, maze.thickness)

        # Display instructions and timer
        self.instructions()
        if self.game_over:
            clock.stop_timer()
            self.screen.blit(game.message(), (610, 120))
        else:
            clock.update_timer()

        # Display the timer on the screen
        self.screen.blit(clock.display_timer(), (625, 200))

        # Update the display with the new drawings
        pygame.display.flip()

    def instructions(self):
        """
        Display the game instructions on the screen.
        """
        instructions1 = self.font.render('Use', True, self.message_color)
        instructions2 = self.font.render('Arrow Keys', True, self.message_color)
        instructions3 = self.font.render('to Move', True, self.message_color)
        self.screen.blit(instructions1, (655, 300))
        self.screen.blit(instructions2, (610, 331))
        self.screen.blit(instructions3, (630, 362))

    def change_screen_color_to_black(self):
        """
        Change the screen fill color to black.
        """
        self.screen.fill(pygame.Color("black"))

if __name__ == "__main__":
    # Set window size and tile size
    window_size = (602, 602)
    screen_size = (window_size[0] + 150, window_size[1])
    tile_size = 30

    # Create the Pygame display window
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Maze Game with CLI Tower")

    # Initialize and run the main game
    game = Main(screen)
    game.main(window_size, tile_size)