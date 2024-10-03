import random

import pygame


class Enemy2:
    def __init__(self, x, y):
        """
        Initialize an Enemy2 object with position, size, and other attributes.

        :param x: Initial X position.
        :param y: Initial Y position.
        """
        self.x = int(x)
        self.y = int(y)
        self.enemy_size = 10
        self.rect = pygame.Rect(
            self.x, self.y, self.enemy_size, self.enemy_size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.speed = 5
        self.move_counter = 0
        self.move_delay = 0.5
        self.image_path = 'img/bug.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(self.image, (self.enemy_size, self.enemy_size))
        self.frozen = False

    def check_player(self, player_x, player_y, tile_size, margin=75):
        """
        Check if the enemy is within a certain margin around the player.

        :param player_x: X position of the player.
        :param player_y: Y position of the player.
        :param tile_size: Size of each tile in the grid.
        :param margin: Margin around the player to check.
        :return: True if the enemy is within the margin, False otherwise.
        """
        distance_x = abs(self.x - player_x)
        distance_y = abs(self.y - player_y)
        return (distance_x <= tile_size + margin and distance_y <= tile_size + margin)

    def get_current_cell(self, grid_cells, tile):
        """
        Get the current cell the enemy is in.

        :param grid_cells: List of all cells in the grid.
        :param tile: Size of each tile in the grid.
        :return: The current cell the enemy is in, or None if not found.
        """
        for cell in grid_cells:
            if cell.x == self.x // tile and cell.y == self.y // tile:
                return cell
        return None

    def check_move(self, tile, grid_cells, thickness):
        """
        Prevent the enemy from moving through walls and redirect it if necessary.

        :param tile: Size of each tile in the grid.
        :param grid_cells: List of all cells in the grid.
        :param thickness: Thickness of the cell walls.
        """
        current_cell = self.get_current_cell(grid_cells, tile)
        if not current_cell:
            return

        # Check walls and redirect if necessary
        if self.velX < 0 and current_cell.walls['left']:
            self.redirect_movement('left')
        elif self.velX > 0 and current_cell.walls['right']:
            self.redirect_movement('right')
        elif self.velY < 0 and current_cell.walls['top']:
            self.redirect_movement('top')
        elif self.velY > 0 and current_cell.walls['bottom']:
            self.redirect_movement('bottom')

    def redirect_movement(self, blocked_direction):
        """
        Randomly select a new movement direction for the enemy, except the blocked direction.

        :param blocked_direction: The direction that is blocked.
        """
        directions = ['left', 'right', 'up', 'down']
        if blocked_direction in directions:
            directions.remove(blocked_direction)

        direction = random.choice(directions)

        if direction == 'left':
            self.velX = -self.speed
            self.velY = 0
        elif direction == 'right':
            self.velX = self.speed
            self.velY = 0
        elif direction == 'up':
            self.velX = 0
            self.velY = -self.speed
        elif direction == 'down':
            self.velX = 0
            self.velY = self.speed

    def draw(self, screen):
        """
        Draw the enemy on the screen.

        :param screen: Pygame surface to draw on.
        """
        screen.blit(self.image, (self.x, self.y))

    def update(self, player_x, player_y, tile_size, grid_cells, thickness, screen_width, screen_height):
        """
        Update the enemy's position, moving it towards the player and avoiding walls.

        :param player_x: X position of the player.
        :param player_y: Y position of the player.
        :param tile_size: Size of each tile in the grid.
        :param grid_cells: List of all cells in the grid.
        :param thickness: Thickness of the cell walls.
        :param screen_width: Width of the screen.
        :param screen_height: Height of the screen.
        """
        self.move_counter += 1
        if self.move_counter < self.move_delay:
            return

        self.move_counter = 0

        # Calculate direction to the player
        direction_x = player_x - self.x
        direction_y = player_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5

        if distance != 0:
            direction_x /= distance
            direction_y /= distance
            self.velX = direction_x * self.speed * 0.2
            self.velY = direction_y * self.speed * 0.2

        self.check_move(tile_size, grid_cells, thickness)

        if (0 <= self.x + self.velX < screen_width - self.enemy_size and
                0 <= self.y + self.velY < screen_height - self.enemy_size):
            self.x += self.velX
            self.y += self.velY
        else:
            # Boundary checks to prevent going off-screen
            if self.x < 0:
                self.x = 0
            elif self.x + self.enemy_size > screen_width - 10:
                self.x = screen_width - self.enemy_size

            if self.y < 0:
                self.y = 0
            elif self.y + self.enemy_size > screen_height:
                self.y = screen_height - self.enemy_size

        self.rect.topleft = (int(self.x), int(self.y))

        if self.frozen:
            self.speed = 0
