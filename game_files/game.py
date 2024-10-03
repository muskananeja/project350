import pygame

pygame.font.init()


class Game:
    def __init__(self, goal_cell, tile):
        """
        Initialize the Game object with the goal cell and tile size.

        :param goal_cell: The cell where the goal is located.
        :param tile: Size of each tile in the grid.
        """
        self.font = pygame.font.SysFont("impact", 35)
        self.message_color = pygame.Color("white")
        self.goal_cell = goal_cell
        self.tile = tile

    def add_goal_point(self, screen):
        """
        Add the goal point image to the screen at the goal cell's position.

        :param screen: Pygame surface to draw on.
        """
        img_path = 'img/gate.png'
        img = pygame.image.load(img_path)
        img = pygame.transform.scale(img, (self.tile, self.tile))
        screen.blit(img, (self.goal_cell.x * self.tile,
                    self.goal_cell.y * self.tile))

    def message(self):
        """
        Render the winning message.

        :return: Pygame surface with the winning message.
        """
        msg = self.font.render('You Win!!', True, self.message_color)
        return msg

    def lose_message(self):
        """
        Render the losing message.

        :return: Pygame surface with the losing message.
        """
        msg = self.font.render('You Lose!!', True, self.message_color)
        return msg

    def is_game_over(self, player):
        """
        Check if the player has reached the goal point.

        :param player: Player object.
        :return: True if the player has reached the goal point, False otherwise.
        """
        goal_cell_abs_x, goal_cell_abs_y = self.goal_cell.x * \
            self.tile, self.goal_cell.y * self.tile
        return player.x >= goal_cell_abs_x and player.y >= goal_cell_abs_y
