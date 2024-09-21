import pygame
from random import choice

class Cell:
    def __init__(self, x, y, thickness):
        """
        Initialize the cell object at (x, y) with walls and other properties and the end
        """

        self.x = x  # Column index of the cell
        self.y = y  # Row index of the cell
        self.thickness = thickness  # Thickness of the cell walls

        # Walls surrounding the cell: top, right, bottom, left
        self.walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True
        }

        self.visited = False  # Flag to check if the cell has been visited during maze generation
        self.is_tower = False  # This flag marks whether the cell contains the CLI Tower.

    def draw(self, sc, tile):
        """
        Draws the walls of the cell on the screen.
        :param sc: Pygame screen or surface to draw on.
        :param tile: Size of each cell in pixels.
        """
        x = self.x * tile
        y = self.y * tile

        # Draw walls
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y), (x + tile, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('black'), (x + tile, y), (x + tile, y + tile), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('black'), (x + tile, y + tile), (x, y + tile), self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y + tile), (x, y), self.thickness)

        # Draw the tower (if this cell contains the CLI tower)
        if self.is_tower:
            pygame.draw.circle(sc, pygame.Color('red'), (x + tile // 2, y + tile // 2), tile // 4)

    def check_cell(self, x, y, cols, rows, grid_cells):
        """
        Checks if the cell at position (x, y) exists within the grid boundaries.
        :param x: Column index to check.
        :param y: Row index to check.
        :param cols: Total number of columns in the grid.
        :param rows: Total number of rows in the grid.
        :param grid_cells: List of all cells in the grid.
        :return: The cell at (x, y) if it exists, otherwise None.
        """
        def find_index(x, y):
            """ Helper function to calculate index in a 1D list """
            return x + y * cols

        if 0 <= x < cols and 0 <= y < rows:
            return grid_cells[find_index(x, y)]
        else:
            return None

    def check_neighbors(self, cols, rows, grid_cells):
        """
        Finds all unvisited neighboring cells and returns one at random.
        :param cols: Total number of columns in the grid.
        :param rows: Total number of rows in the grid.
        :param grid_cells: List of all cells in the grid.
        :return: A random unvisited neighboring cell, or None if none exist.
        """
        neighbors = []

        # Get neighbors
        top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
        right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
        left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)

        # Add unvisited neighbors to the list
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)

        if neighbors:
            # Return a random unvisited neighbor
            return choice(neighbors)
        else:
            return None
