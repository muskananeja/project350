import pygame
from random import choice


class Cell:
    def __init__(self, x, y, thickness):
        """
        Initialize a Cell object with coordinates (x, y) and wall thickness.

        :param x: Column index of the cell.
        :param y: Row index of the cell.
        :param thickness: Thickness of the cell walls.
        """
        self.x = x
        self.y = y
        self.thickness = thickness
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False
        self.is_tower = False

    def draw(self, sc, tile):
        """
        Draw the cell's walls and tower (if present) on the given surface.

        :param sc: Pygame surface to draw on.
        :param tile: Size of each cell in pixels.
        """
        x = self.x * tile
        y = self.y * tile

        # Draw cell walls
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('black'), (x, y),
                             (x + tile, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color(
                'black'), (x + tile, y), (x + tile, y + tile), self.thickness)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color(
                'black'), (x + tile, y + tile), (x, y + tile), self.thickness)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('black'),
                             (x, y + tile), (x, y), self.thickness)

        # Draw tower if present
        if self.is_tower:
            custom_image = pygame.image.load('img/tower.png')
            custom_image = pygame.transform.scale(custom_image, (tile, tile))
            sc.blit(custom_image, (x, y))

    def check_cell(self, x, y, cols, rows, grid_cells):
        """
        Check if the cell at (x, y) exists within the grid boundaries.

        :param x: Column index to check.
        :param y: Row index to check.
        :param cols: Total number of columns in the grid.
        :param rows: Total number of rows in the grid.
        :param grid_cells: List of all cells in the grid.
        :return: The cell at (x, y) if it exists, otherwise None.
        """
        def find_index(x, y):
            """Calculate the index in a 1D list based on 2D coordinates."""
            return x + y * cols

        if 0 <= x < cols and 0 <= y < rows:
            return grid_cells[find_index(x, y)]
        return None

    def check_neighbors(self, cols, rows, grid_cells):
        """
        Find all unvisited neighboring cells and return one at random.

        :param cols: Total number of columns in the grid.
        :param rows: Total number of rows in the grid.
        :param grid_cells: List of all cells in the grid.
        :return: A random unvisited neighboring cell, or None if none exist.
        """
        neighbors = []

        # Get neighboring cells
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
            return choice(neighbors)
        return None

    def get_neighbors(self, cols, rows, grid_cells):
        """
        Get all neighboring cells regardless of their visited status.

        :param cols: Total number of columns in the grid.
        :param rows: Total number of rows in the grid.
        :param grid_cells: List of all cells in the grid.
        :return: List of all neighboring cells.
        """
        neighbors = []

        # Get neighboring cells
        top = self.check_cell(self.x, self.y - 1, cols, rows, grid_cells)
        right = self.check_cell(self.x + 1, self.y, cols, rows, grid_cells)
        bottom = self.check_cell(self.x, self.y + 1, cols, rows, grid_cells)
        left = self.check_cell(self.x - 1, self.y, cols, rows, grid_cells)

        if top:
            neighbors.append(top)
        if right:
            neighbors.append(right)
        if bottom:
            neighbors.append(bottom)
        if left:
            neighbors.append(left)

        return neighbors
