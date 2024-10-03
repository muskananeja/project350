import pygame
import random
import time


class Player:
    def __init__(self, x, y):
        """
        Initialize a Player object with position, size, and other attributes.

        :param x: Initial X position.
        :param y: Initial Y position.
        """
        self.x = int(x)
        self.y = int(y)
        self.player_size = 25
        self.rect = pygame.Rect(
            self.x, self.y, self.player_size, self.player_size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 2.5

        # Load multiple images for animation
        self.image_paths = [
            'img/player/player1.png', 'img/player/player2.png', 'img/player/player3.png',
            'img/player/player4.png', 'img/player/player5.png', 'img/player/player6.png'
        ]
        self.images = [pygame.image.load(img_path)
                       for img_path in self.image_paths]
        self.images = [pygame.transform.scale(
            img, (self.player_size, self.player_size)) for img in self.images]
        self.current_image_index = 0
        self.animation_speed = 8  # Number of frames to wait before switching to the next image
        self.frame_count = 2  # Frame counter to control animation speed


        # Variables for losing control
        self.is_losing_control = False
        self.control_loss_start_time = 0
        self.control_loss_duration = 10  # 10 seconds of losing control

    def lose_control(self):
        """Start the control loss process."""
        self.is_losing_control = True
        self.control_loss_start_time = time.time()

    def random_movement(self):
        """Randomly move the player while control is lost."""
        self.velX = random.choice([-self.speed, 0, self.speed])
        self.velY = random.choice([-self.speed, 0, self.speed])

    def check_tower(self, tower_cell, tile_size):
        """
        Check if the player has reached the CLI tower.

        :param tower_cell: The cell where the CLI tower is located.
        :param tile_size: Size of each tile in the grid.
        :return: True if the player has reached the CLI tower, False otherwise.
        """
        return self.x // tile_size == tower_cell.x and self.y // tile_size == tower_cell.y

    def get_current_cell(self, grid_cells, tile):
        """
        Get the current cell the player is in.

        :param grid_cells: List of all cells in the grid.
        :param tile: Size of each tile in the grid.
        :return: The current cell the player is in, or None if not found.
        """
        for cell in grid_cells:
            if cell.x == self.x // tile and cell.y == self.y // tile:
                return cell
        return None

    def check_move(self, tile, grid_cells, thickness):
        """
        Prevent the player from moving through walls.

        :param tile: Size of each tile in the grid.
        :param grid_cells: List of all cells in the grid.
        :param thickness: Thickness of the cell walls.
        """
        current_cell_x = self.x // tile
        current_cell_y = self.y // tile
        current_cell = self.get_current_cell(grid_cells, tile)

        if not current_cell:
            return

        current_cell_abs_x = current_cell_x * tile
        current_cell_abs_y = current_cell_y * tile

        # Check left wall
        if self.left_pressed and current_cell.walls['left'] and self.x <= current_cell_abs_x + thickness:
            self.velX = 0

        # Check right wall
        if self.right_pressed and current_cell.walls['right'] and self.x + self.player_size >= current_cell_abs_x + tile - thickness:
            self.velX = 0

        # Check top wall
        if self.up_pressed and current_cell.walls['top'] and self.y <= current_cell_abs_y + thickness:
            self.velY = 0

        # Check bottom wall
        if self.down_pressed and current_cell.walls['bottom'] and self.y + self.player_size >= current_cell_abs_y + tile - thickness:
            self.velY = 0

    def update(self, tile, grid_cells, thickness):
        """
        Update the player's position based on movement flags and check for wall collisions.

        :param tile: Size of each tile in the grid.
        :param grid_cells: List of all cells in the grid.
        :param thickness: Thickness of the cell walls.
        """

        # Handle loss of control
        if self.is_losing_control:
            self.random_movement()
            # End control loss after 10 seconds
            if time.time() - self.control_loss_start_time > self.control_loss_duration:
                self.is_losing_control = False  # Regain control

        else:
            # Normal movement control

            self.velX = 0
            self.velY = 0

            # Horizontal movement
            if self.left_pressed and not self.right_pressed:
                self.velX = -self.speed
            elif self.right_pressed and not self.left_pressed:
                self.velX = self.speed

            # Vertical movement
            if self.up_pressed and not self.down_pressed:
                self.velY = -self.speed
            elif self.down_pressed and not self.up_pressed:
                self.velY = self.speed

            # Check if the player can move without hitting walls
            self.check_move(tile, grid_cells, thickness)

        # Apply velocity to the player's position
        self.x += self.velX
        self.y += self.velY

        # Update the player's rectangle for rendering
        self.rect.topleft = (int(self.x), int(self.y))

        # Update the frame count and switch to the next image if needed
        self.frame_count += 1
        if self.frame_count >= self.animation_speed:
            self.frame_count = 0
            self.current_image_index = (
                self.current_image_index + 1) % len(self.images)

    def draw(self, screen):
        """
        Draw the current image of the player at its position.

        :param screen: Pygame surface to draw on.
        """
        screen.blit(self.images[self.current_image_index], (self.x, self.y))

    def move(self, dx, dy):
        """
        Move the player by a specified amount.

        :param dx: Amount to move in the X direction.
        :param dy: Amount to move in the Y direction.
        """
        self.x += dx
        self.y += dy
