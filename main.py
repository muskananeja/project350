import pygame
import sys
from maze import Maze
from player import Player
from game import Game
from clock import Clock
from enemy import Enemy

pygame.init()
pygame.font.init()

class Main:
    def __init__(self, screen):
        """
        Initialize the main game class.
        :param screen: Pygame screen or surface to draw on.
        """
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("cyan")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()
        self.cli_cooldown = 0  # Cooldown timer to prevent re-entering CLI mode immediately

    def main(self, frame_size, tile):
        """
        The main game loop. Handles game initialization, events, and drawing.
        :param frame_size: Tuple with the dimensions of the game window.
        :param tile: Size of the tiles/cells in the maze.
        """
        cols, rows = frame_size[0] // tile, frame_size[1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        enemy = Enemy(10 * tile, 10 * tile)  # Initialize enemy at some location
        clock = Clock()

        maze.generate_maze()
        clock.start_timer()

        while self.running:
            self.screen.fill("gray")
            self.screen.fill(pygame.Color("darkslategray"), (603, 0, 752, 752))

            # Update CLI cooldown timer
            if self.cli_cooldown > 0:
                self.cli_cooldown -= 1

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # If keys are pressed
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

                # If keys are released
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

            # Check if the player has reached the CLI tower (only if cooldown is 0)
            if self.cli_cooldown == 0 and player.check_tower(maze.tower_cell, tile):
                self.enter_cli_mode(player)

            # Add check if player has reached the enemy
            if enemy.check_player(player.x, player.y, tile):
                print("Game Over! Enemy has caught the player!")
                self.game_over = True
                # You can add additional logic here like ending the game, reducing health, etc.

            # Check if the player has won the game
            if game.is_game_over(player):
                self.game_over = True
                player.left_pressed = False
                player.right_pressed = False
                player.up_pressed = False
                player.down_pressed = False
            
            # Update the enemy's movement towards the player
            enemy.update(player.x, player.y, tile)

            # Draw the maze, player, and additional game elements
            self._draw(maze, tile, player, game, clock, enemy)

            # Cap the frame rate to 60 FPS
            self.FPS.tick(60)

    def enter_cli_mode(self, player):
        """
        Enter the Command-Line Interface (CLI) mode for game control.
        Allows the player to input commands such as teleporting and exiting CLI mode.
        :param player: Player object to allow modifications (e.g., teleport).
        """
        print("You've reached the CLI Tower! Enter commands. Type 'exit' to resume the game.")
        
        while True:
            command = input("Enter command: ").strip().lower()  # Read command input from user
            
            if command == "exit":
                print("Exiting CLI mode.")
                self.cli_cooldown = 120  # Set cooldown for 120 frames (~2 seconds at 60 FPS)
                return  # Exit the CLI mode and resume the game
            elif command.startswith("teleport"):
                try:
                    _, x, y = command.split()
                    player.x = int(x) * 30  # Teleport the player to new coordinates
                    player.y = int(y) * 30
                    print(f"Teleported player to ({x}, {y}).")
                    self.cli_cooldown = 120
                    return
                except ValueError:
                    print("Invalid teleport command. Use 'teleport x y' format.")
            elif command == "quit":
                pygame.quit()  # Quit the game
                sys.exit()
            else:
                print("Unknown command. Available commands: 'teleport x y', 'exit', 'quit'.")

    def _draw(self, maze, tile, player, game, clock, enemy):
        """
        Draws all game elements on the screen including maze, player, enemy, and time.
        :param maze: Maze object to render.
        :param tile: Size of the tiles/cells in the maze.
        :param player: Player object to render.
        :param game: Game object for game state management.
        :param clock: Clock object for managing time.
        :param enemy: Enemy object to render.
        """
        # Draw the maze cells
        [cell.draw(self.screen, tile) for cell in maze.grid_cells]
        
        # Draw the goal point
        game.add_goal_point(self.screen)
        
        # Draw the player character
        player.draw(self.screen)
        
        # Draw the enemy character
        enemy.draw(self.screen)
        
        # Update player's movement and handle collision
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
