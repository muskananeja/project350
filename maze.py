import pygame
from cell import Cell
import random

class Maze:
    def __init__(self, cols, rows):
        """
        Initialize the Maze object.
        :param cols: Number of columns in the maze.
        :param rows: Number of rows in the maze.
        """
        self.cols = cols
        self.rows = rows
        self.thickness = 4  # Thickness of the walls
        self.grid_cells = [Cell(col, row, self.thickness) for row in range(self.rows) for col in range(self.cols)]
        self.tower_cell = None  # Holds the CLI Tower cell.

    def generate_maze(self):
        """
        Generates the maze using a recursive backtracking algorithm.
        """
        current_cell = self.grid_cells[0]
        array = []
        break_count = 1

        while break_count != len(self.grid_cells):
            current_cell.visited = True
            next_cell = current_cell.check_neighbors(self.cols, self.rows, self.grid_cells)

            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                self.remove_walls(current_cell, next_cell)  # Remove walls between adjacent cells
                current_cell = next_cell
            elif array:
                current_cell = array.pop()

        # Place the CLI tower at a random location
        self.tower_cell = random.choice(self.grid_cells)
        self.tower_cell.is_tower = True  # Mark the tower cell
        return self.grid_cells

    def remove_walls(self, current, next):
        """
        Removes the walls between two adjacent cells.
        :param current: The current cell.
        :param next: The neighboring cell.
        """
        dx = current.x - next.x
        dy = current.y - next.y

        if dx == 1:  # Next cell is to the left of current cell
            current.walls['left'] = False
            next.walls['right'] = False
        elif dx == -1:  # Next cell is to the right of current cell
            current.walls['right'] = False
            next.walls['left'] = False
        elif dy == 1:  # Next cell is above the current cell
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif dy == -1:  # Next cell is below the current cell
            current.walls['bottom'] = False
            next.walls['top'] = False

    def draw(self, sc, tile):
        """
        Draw the maze by drawing each cell.
        :param sc: Pygame screen object.
        :param tile: Size of each cell in pixels.
        """
        for cell in self.grid_cells:
            cell.draw(sc, tile)
