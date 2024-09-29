import pygame
import random

class Enemy2:
    def __init__(self, x, y):
        self.x = int(x)  # enemy position on the x-axis
        self.y = int(y)  # enemy position on the y-axis
        self.enemy_size = 10  # size of the enemy
        self.rect = pygame.Rect(self.x, self.y, self.enemy_size, self.enemy_size)  # for rendering and collision
        self.color = (250, 120, 60)  # enemy color
        self.velX = 0  # velocity on the x-axis
        self.velY = 0  # velocity on the y-axis
        self.speed = 8  # movement speed
        self.move_counter = 0  # counter for movement delay
        self.move_delay = 2 # frames to wait before next move

    def check_player(self, player_x, player_y, tile_size):
        """Check if the enemy has reached the player."""
        return (self.x // tile_size == player_x // tile_size and
                self.y // tile_size == player_y // tile_size)

    def get_current_cell(self, grid_cells, tile):
        """Get the current cell the enemy is in."""
        for cell in grid_cells:
            if cell.x == self.x // tile and cell.y == self.y // tile:
                return cell
        return None  # Return None if no cell is found

    def check_move(self, tile, grid_cells, thickness):
        """Prevent the enemy from moving through walls and redirect it."""
        current_cell = self.get_current_cell(grid_cells, tile)
        if not current_cell:
            return  # If there's no current cell, exit the function

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
        """Randomly select a new movement direction for the enemy, 
        except the assigned direction."""
        directions = ['left', 'right', 'up', 'down']

        # Remove the blocked direction from the list
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
        """Draw the enemy on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, player_x, player_y, tile_size, grid_cells, thickness, screen_width, screen_height):
        """Update the enemy's position, moving it towards the player and avoiding walls."""
        self.move_counter += 1  # Increment frame counter
        if self.move_counter < self.move_delay:
            return  # Skip movement update until the counter hits move_delay

        self.move_counter = 0  # Reset counter

        # Calculate direction to the player
        direction_x = player_x - self.x
        direction_y = player_y - self.y

        # Calculate the distance using the distance formula
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5

        # Avoid division by zero if the enemy is exactly on the player
        if distance != 0:
            # Normalize the direction vector
            direction_x /= distance
            direction_y /= distance

            # Move the enemy towards the player with a fraction of the speed
            self.velX = direction_x * self.speed * 0.5  # Adjust for slower change
            self.velY = direction_y * self.speed * 0.5  # Adjust for slower change

        # Check if the enemy can move without hitting walls
        self.check_move(tile_size, grid_cells, thickness)

        # Update the enemy's position
        self.x += self.velX
        self.y += self.velY

        # Boundary checks to prevent going off-screen
        if self.x < 5:  # Left boundary
            self.x = 0
        elif self.x + self.enemy_size > screen_width:  # Right boundary
            self.x = screen_width - self.enemy_size-5

        if self.y < 3:  # Top boundary
            self.y = 0
        elif self.y + self.enemy_size > screen_height-5:  # Bottom boundary
            self.y = screen_height - self.enemy_size

        # Update the enemy's rectangle for rendering
        self.rect.topleft = (int(self.x), int(self.y))

        # Check if the enemy has reached the player
        if self.check_player(player_x, player_y, tile_size):
            self.screen.fill(pygame.Color("black"))

