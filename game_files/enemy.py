import pygame


class Enemy:
    def __init__(self, x, y):
        """
        Initialize an Enemy object with position, size, and other attributes.

        :param x: Initial X position.
        :param y: Initial Y position.
        """
        self.x = int(x)
        self.y = int(y)
        self.enemy_size = 25
        self.rect = pygame.Rect(
            self.x, self.y, self.enemy_size, self.enemy_size)
        self.velX = 0
        self.velY = 0
        self.speed = 0.2
        self.image_path = 'img/enemy.png'
        self.image = pygame.image.load(self.image_path)
        self.image = pygame.transform.scale(
            self.image, (self.enemy_size, self.enemy_size))
        self.frozen = False

    def check_player(self, player_x, player_y, tile_size):
        """
        Check if the enemy has reached the player.

        :param player_x: X position of the player.
        :param player_y: Y position of the player.
        :param tile_size: Size of each tile in the grid.
        :return: True if the enemy has reached the player, False otherwise.
        """
        return self.x // tile_size == player_x // tile_size and self.y // tile_size == player_y // tile_size

    def draw(self, screen):
        """
        Draw the enemy on the screen.

        :param screen: Pygame surface to draw on.
        """
        screen.blit(self.image, (self.x, self.y))

    def update(self, player_x, player_y, tile_size):
        """
        Update the enemy's position, moving it towards the player.

        :param player_x: X position of the player.
        :param player_y: Y position of the player.
        :param tile_size: Size of each tile in the grid.
        """
        direction_x = player_x - self.x
        direction_y = player_y - self.y
        distance = (direction_x ** 2 + direction_y ** 2) ** 0.5

        if distance != 0:
            direction_x /= distance
            direction_y /= distance
            self.velX = direction_x * self.speed
            self.velY = direction_y * self.speed

        self.x += self.velX
        self.y += self.velY
        self.rect.topleft = (int(self.x), int(self.y))

        if self.frozen:
            self.speed = 0

        if not self.frozen and self.check_player(player_x, player_y, tile_size):
            print("Enemy has reached the player!")
