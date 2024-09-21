import pygame

class Enemy:
    # Initializing enemy object with position, size, and other attributes
    def __init__(self, x, y):
        self.x = int(x)  # Initial X position
        self.y = int(y)  # Initial Y position
        self.enemy_size = 10  # Size of the enemy
        self.rect = pygame.Rect(self.x, self.y, self.enemy_size, self.enemy_size)  # Rectangle for rendering and collision
        self.color = (250, 0, 0)  # Enemy color (red)
        self.velX = 0  # X-axis velocity
        self.velY = 0  # Y-axis velocity
        self.speed = 0.2  # Movement speed
    
    # Check if the enemy has reached the player
    def check_player(self, player_x, player_y, tile_size):
        """Check if the enemy has reached the player."""
        return self.x // tile_size == player_x // tile_size and self.y // tile_size == player_y // tile_size
    
    # Draw the enemy on the screen
    def draw(self, screen):
        """Draw the enemy on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)
    
    # Update the enemy's position, moving it towards the player
    def update(self, player_x, player_y, tile_size):
        """Update the enemy's position, moving it towards the player."""
        # Calculate direction to the player
        direction_x = player_x - self.x
        direction_y = player_y - self.y
        
        # Calculate the distance using the distance formula
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5
        
        # Avoid division by zero if the enemy is exactly on the player
        if distance != 0:
            # Normalize the direction vector (make it a unit vector)
            direction_x /= distance
            direction_y /= distance
            
            # Move the enemy towards the player
            self.velX = direction_x * self.speed
            self.velY = direction_y * self.speed
        
        # Update the enemy's position
        self.x += self.velX
        self.y += self.velY
        
        # Update the enemy's rectangle for rendering
        self.rect.topleft = (int(self.x), int(self.y))
        
        # Check if the enemy has reached the player
        if self.check_player(player_x, player_y, tile_size):
            print("Enemy has reached the player!")