import sys

import pygame

from clock import Clock
from enemy import Enemy
from game import Game
from maze import Maze
from player import Player

pygame.init()
pygame.font.init()

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("impact", 30)
        self.message_color = pygame.Color("white")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()
        self.cli_cooldown = 0
        self.is_screen_black = False  # Flag to determine screen color
        self.black_screen_start_time = None  # Variable to store the time when the screen was changed to black
        self.lost = False  # Flag to determine if the player lost
        self.show_answer = False  # Flag to determine if the answer should be shown
        self.answer_start_time = None  # Variable to store the time when the answer was shown
    
    def main(self, frame_size, tile):
        cols, rows = frame_size[0] // tile, frame_size[1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        enemy = Enemy(10 * tile, 10 * tile)  # Initialize enemy at some location
        clock = Clock()

        maze.generate_maze()
        clock.start_timer()

        while self.running:
            # Check if 5 seconds have passed since the screen was changed to black
            if self.is_screen_black and (pygame.time.get_ticks() - self.black_screen_start_time) > 10000:
                self.is_screen_black = False  # Reset the flag to change screen color back to white

            # Check if 5 seconds have passed since the answer was shown
            if self.show_answer and (pygame.time.get_ticks() - self.answer_start_time) > 10000:
                self.show_answer = False  # Reset the flag to stop showing the answer

            if self.is_screen_black:
                self.screen.fill("black")
            else:
                self.screen.fill("gray")
            self.screen.fill(pygame.Color("black"), (603, 0, 752, 752))

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
                self.enter_cli_mode(player, maze)

            # Add check if player has reached the enemy
            if enemy.check_player(player.x, player.y, tile):
                if not self.game_over:
                    print("Game Over! Enemy has caught the player!")
                self.game_over = True
                self.lost = True  # Set the lost flag
                self.running = False  # Stop the game loop

            if game.is_game_over(player):
                self.game_over = True
                player.left_pressed = False
                player.right_pressed = False
                player.up_pressed = False
                player.down_pressed = False
                self.running = False  # Stop the game loop
            
            # Update the enemy's movement towards the player
            enemy.update(player.x, player.y, tile)

            self._draw(maze, tile, player, game, clock, enemy)
            self.FPS.tick(60)

        # Display the game over message after the loop ends
        self._draw(maze, tile, player, game, clock, enemy)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def enter_cli_mode(self, player, maze):
        print("You've reached the CLI Tower! Enter commands. Type 'exit' to resume the game.")
        
        while True:
            command = input("Enter command: ").strip().lower()
            
            if command == "exit":
                print("Exiting CLI mode.")
                self.cli_cooldown = 240
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
            elif command == "answer":
                print("Showing the answer for 5 seconds.")
                maze.solve_maze()  # Solve the maze to get the solution path
                self.show_answer = True  # Set the flag to show the answer
                self.answer_start_time = pygame.time.get_ticks()  # Store the current time

                return
            else:
                print("Unknown command. Available commands: 'teleport x y', 'exit', 'quit', 'answer'.")

    def _draw(self, maze, tile, player, game, clock, enemy):
        [cell.draw(self.screen, tile) for cell in maze.grid_cells]
        game.add_goal_point(self.screen)
        player.draw(self.screen)
        enemy.draw(self.screen)
        player.update(tile, maze.grid_cells, maze.thickness)
        self.instructions()
        if self.game_over:
            clock.stop_timer()
            if self.lost:
                self.screen.blit(game.lose_message(), (610, 120))
            else:
                self.screen.blit(game.message(), (610, 120))
        else:
            clock.update_timer()
        self.screen.blit(clock.display_timer(), (625, 200))
        if self.show_answer:
            self.draw_answer(maze, tile)
        pygame.display.flip()

    def draw_answer(self, maze, tile):
        """
        Draws the solution path on the screen with semi-transparent yellow color.
        :param maze: The maze object.
        :param tile: Size of each cell in pixels.
        """
        # Create a semi-transparent surface
        overlay = pygame.Surface((tile, tile), pygame.SRCALPHA)
        overlay.fill((255, 255, 0, 128))  # Yellow color with 50% opacity

        for cell in maze.solution_path:  # Use the solution path to draw the answer
            x = cell.x * tile
            y = cell.y * tile
            self.screen.blit(overlay, (x, y))

    def instructions(self):
        instructions1 = self.font.render('Use', True, self.message_color)
        instructions2 = self.font.render('Arrow Keys', True, self.message_color)
        instructions3 = self.font.render('to Move', True, self.message_color)
        self.screen.blit(instructions1, (655, 300))
        self.screen.blit(instructions2, (610, 331))
        self.screen.blit(instructions3, (630, 362))

    def change_screen_color_to_black(self):
        self.screen.fill(pygame.Color("black"))

if __name__ == "__main__":
    window_size = (602, 602)
    screen_size = (window_size[0] + 150, window_size[1])
    tile_size = 30

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Maze Game with CLI Tower")

    game = Main(screen)
    game.main(window_size, tile_size)