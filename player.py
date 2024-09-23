import pygame

class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.player_size = 10
        self.rect = pygame.Rect(self.x, self.y, self.player_size, self.player_size)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
        self.image_path = 'img/player.png'  # Path to the player image
        self.image = pygame.image.load(self.image_path)  # Load the image
        self.image = pygame.transform.scale(self.image, (self.player_size, self.player_size))  # Scale the image

    def check_tower(self, tower_cell, tile_size):
        """Check if the player has reached the CLI tower."""
        return self.x // tile_size == tower_cell.x and self.y // tile_size == tower_cell.y

    def get_current_cell(self, grid_cells, tile):
        """Get the current cell the player is in."""
        for cell in grid_cells:
            if cell.x == self.x // tile and cell.y == self.y // tile:
                return cell

    def check_move(self, tile, grid_cells, thickness):
        """Prevent the player from moving through walls."""
        current_cell_x = self.x // tile
        current_cell_y = self.y // tile
        current_cell = self.get_current_cell(grid_cells, tile)

        # Get the absolute position of the current cell
        current_cell_abs_x = current_cell_x * tile
        current_cell_abs_y = current_cell_y * tile

        # Check left wall
        if self.left_pressed:
            if current_cell.walls['left']:
                if self.x <= current_cell_abs_x + thickness:
                    self.velX = 0  # Stop horizontal movement

        # Check right wall
        if self.right_pressed:
            if current_cell.walls['right']:
                if self.x + self.player_size >= current_cell_abs_x + tile - thickness:
                    self.velX = 0

        # Check top wall
        if self.up_pressed:
            if current_cell.walls['top']:
                if self.y <= current_cell_abs_y + thickness:
                    self.velY = 0

        # Check bottom wall
        if self.down_pressed:
            if current_cell.walls['bottom']:
                if self.y + self.player_size >= current_cell_abs_y + tile - thickness:
                    self.velY = 0

    def update(self, tile, grid_cells, thickness):
        """Update the player's position based on movement flags and check for wall collisions."""
        # Set the velocity based on pressed keys
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

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))  # Draw the image at the player's position

    def move(self, dx, dy):
        self.x += dx
        self.y += dy