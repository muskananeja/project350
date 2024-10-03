import sys
import pygame
from game_files.clock import Clock
from game_files.enemy import Enemy
from game_files.enemy2 import Enemy2
from game_files.game import Game
from game_files.maze import Maze
from game_files.player import Player

pygame.init()
pygame.font.init()


class Main:
    def __init__(self, screen):
        """
        Initialize the Main class with the game screen and various attributes.

        :param screen: Pygame surface to draw on.
        """
        self.screen = screen
        self.font = pygame.font.Font("fonts/popmedium.ttf", 25)
        self.font1 = pygame.font.Font("fonts/popmedium.ttf", 8)
        self.message_color = pygame.Color("white")
        self.message_color1 = pygame.Color("green")
        self.running = True
        self.game_over = False
        self.FPS = pygame.time.Clock()
        self.cli_cooldown = 0
        self.is_screen_black = False
        self.black_screen_start_time = None
        self.lost = False
        self.show_answer = False
        self.answer_start_time = None
        self.enemies_frozen = False
        self.freeze_start_time = None
        self.in_cli = False
        self.enemy2_spawn = False

    def main(self, frame_size, tile):
        """
        Main game loop to handle events, updates, and rendering.

        :param frame_size: Tuple containing the width and height of the game frame.
        :param tile: Size of each tile in the grid.
        """
        cols, rows = frame_size[0] // tile, frame_size[1] // tile
        maze = Maze(cols, rows)
        game = Game(maze.grid_cells[-1], tile)
        player = Player(tile // 3, tile // 3)
        enemy = Enemy(15 * tile, 15 * tile)
        enemy2 = Enemy2(10 * tile, 9 * tile)
        clock = Clock()

        maze.generate_maze()
        clock.start_timer()

        while self.running:
            if self.is_screen_black and (pygame.time.get_ticks() - self.black_screen_start_time) > 10000:
                self.is_screen_black = False

            if self.show_answer and (pygame.time.get_ticks() - self.answer_start_time) > 10000:
                self.show_answer = False

            if self.enemies_frozen and (pygame.time.get_ticks() - self.freeze_start_time) > 15000:
                print("Enemies unfrozen, and angry. RUN!!!")
                self.enemies_frozen = False
                self.freeze_penalty(enemy, player)

            self.screen.fill("black" if self.is_screen_black else "gray")
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
                self.enter_cli_mode(player, enemy, maze)

            if not enemy.frozen and enemy.check_player(player.x, player.y, tile):
                if not self.game_over:
                    print("Game Over! Enemy has caught the player!")
                self.game_over = True
                self.lost = True
                self.running = False

            if self.enemy2_spawn:
                if enemy2.check_player(player.x, player.y, tile):
                    print("You have lost visibility")
                    self.screen.fill(pygame.Color("black"))
                    enemy2.update(player.x, player.y, tile, maze.grid_cells,
                          maze.thickness, frame_size[0], frame_size[1])

            if game.is_game_over(player):
                self.game_over = True
                player.left_pressed = False
                player.right_pressed = False
                player.up_pressed = False
                player.down_pressed = False
                self.running = False

            enemy.update(player.x, player.y, tile)

            player.update(tile, maze.grid_cells, 2)

            self._draw(maze, tile, player, game, clock, enemy)
            if self.in_cli:
                self.draw_enemy2(enemy2)
                self.enemy2_spawn = True
            self.FPS.tick(60)

        self._draw(maze, tile, player, game, clock, enemy, enemy2)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def _draw(self, maze, tile, player, game, clock, enemy):
        """
        Draw all game elements on the screen.

        :param maze: Maze object containing the grid cells.
        :param tile: Size of each tile in the grid.
        :param player: Player object.
        :param game: Game object.
        :param clock: Clock object.
        :param enemy: Enemy object.
        :param enemy2: Enemy2 object.
        """
        [cell.draw(self.screen, tile) for cell in maze.grid_cells]
        game.add_goal_point(self.screen)
        player.draw(self.screen)
        enemy.draw(self.screen)
        player.update(tile, maze.grid_cells, maze.thickness)
        self.instructions(player, enemy)
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

    def draw_enemy2(self, enemy2):
        enemy2.draw(self.screen)

    def enter_cli_mode(self, player, enemy, maze):
        """
        Enter CLI mode to accept commands from the player.

        :param player: Player object.
        :param enemy: Enemy object.
        :param maze: Maze object.
        """

        self.in_cli = True

        print(
            "You've reached the CLI Tower! Enter commands. Type 'exit' to resume the game.")

        while True:
            command = input("Enter command: ").strip().lower()

            if command == "exit":
                self.in_cli = False
                print("Exiting CLI mode.")
                self.cli_cooldown = 240
                return
            elif command.startswith("teleport"):
                try:
                    _, x, y = command.split()
                    player.x = int(x) * 30
                    player.y = int(y) * 30
                    print(f"Teleported player to ({x}, {y}).")
                    self.is_screen_black = True
                    self.black_screen_start_time = pygame.time.get_ticks()
                    self.in_cli = False
                    self.cli_cooldown = 240
                    return
                except ValueError:
                    print("Invalid teleport command. Use 'teleport x y' format.")
            elif command == "quit":
                pygame.quit()
                sys.exit()
            elif command == "answer":
                print("Showing the answer for 5 seconds.")
                maze.solve_maze()
                self.show_answer = True
                self.answer_start_time = pygame.time.get_ticks()
                self.in_cli = False
                self.cli_cooldown = 600
                player.lose_control()
                player.speed = 2.5
                return
            elif command == "freeze":
                print("Freezing all enemies for 10 seconds.")
                self.enemies_frozen = True
                self.freeze_start_time = pygame.time.get_ticks()
                enemy.frozen = True
                self.in_cli = False
                self.cli_cooldown = 240
                return
            else:
                print(
                    "Unknown command. Available commands: 'teleport x y', 'answer', 'freeze', 'exit', 'quit'.")

    def draw_answer(self, maze, tile):
        """
        Draw the solution path of the maze on the screen.

        :param maze: Maze object containing the solution path.
        :param tile: Size of each tile in the grid.
        """
        overlay = pygame.Surface((tile, tile), pygame.SRCALPHA)
        overlay.fill((255, 255, 0, 128))

        for cell in maze.solution_path:
            x = cell.x * tile
            y = cell.y * tile
            self.screen.blit(overlay, (x, y))

    def instructions(self, player, enemy):
        """
        Display game instructions and player/enemy coordinates on the screen.

        :param player: Player object.
        :param enemy: Enemy object.
        :param enemy2: Enemy2 object.
        """
        instructions1 = self.font.render('Use', True, self.message_color)
        instructions2 = self.font.render(
            'Arrow Keys', True, self.message_color)
        instructions3 = self.font.render('to Move', True, self.message_color)
        commandsshow = self.font1.render(
            'Available Commands in CLI', True, self.message_color)
        commandslist1 = self.font1.render(
            'teleport x y = Teleports to X, Y', True, self.message_color1)
        commandslist2 = self.font1.render(
            'answer = Shows the Path to Exit', True, self.message_color1)
        commandslist3 = self.font1.render(
            'freeze = Freezes all enemies', True, self.message_color1)
        commandslist4 = self.font1.render(
            'exit = Exit the CLI', True, self.message_color1)
        playercoordinates = self.font1.render(f"Player coordinates: ({
                                              player.x // 28.75}, {player.y // 28.75})", True, self.message_color)
        enemycoordinates = self.font1.render(f"Enemy coordinates: ({
                                             enemy.x // 28.75}, {enemy.y // 28.75})", True, self.message_color)

        self.screen.blit(instructions1, (650, 300))
        self.screen.blit(instructions2, (605, 331))
        self.screen.blit(instructions3, (625, 362))
        self.screen.blit(commandsshow, (610, 410))
        self.screen.blit(commandslist1, (610, 425))
        self.screen.blit(commandslist2, (610, 437))
        self.screen.blit(commandslist3, (610, 449))
        self.screen.blit(commandslist4, (610, 461))
        self.screen.blit(playercoordinates, (610, 567))
        self.screen.blit(enemycoordinates, (610, 579))
        

    def freeze_penalty(self, enemy, player):
        """
        Apply a penalty when enemies are unfrozen, increasing their speed and reducing the player's speed.

        :param enemy: Enemy object.
        :param player: Player object.
        """
        enemy.frozen = False
        enemy.speed += 1
        player.speed -= 3
