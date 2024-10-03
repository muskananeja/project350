import pygame
from game_files.cell import Cell
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
        self.grid_cells = [Cell(col, row, self.thickness)
                           for row in range(self.rows) for col in range(self.cols)]
        self.tower_cell = None  # Holds the CLI Tower cell.

    def generate_maze(self):
        """
        Generate the maze using a recursive backtracking algorithm.

        :return: List of all cells in the maze.
        """
        current_cell = self.grid_cells[0]
        array = []
        break_count = 1
        self.solution_path = []  # List to store the solution path

        while break_count != len(self.grid_cells):
            current_cell.visited = True
            # Add the current cell to the solution path
            self.solution_path.append(current_cell)
            next_cell = current_cell.check_neighbors(
                self.cols, self.rows, self.grid_cells)

            if next_cell:
                next_cell.visited = True
                break_count += 1
                array.append(current_cell)
                # Remove walls between adjacent cells
                self.remove_walls(current_cell, next_cell)
                current_cell = next_cell
            elif array:
                current_cell = array.pop()

        # Place the CLI tower at a random location
        self.tower_cell = random.choice(self.grid_cells)
        self.tower_cell.is_tower = True  # Mark the tower cell
        return self.grid_cells

    def solve_maze(self):
        """
        Solve the maze using Depth-First Search (DFS) and store the solution path.

        :return: List of cells representing the solution path.
        """
        start_cell = self.grid_cells[0]
        end_cell = self.grid_cells[-1]
        stack = [(start_cell, [start_cell])]
        visited = set()

        while stack:
            current_cell, path = stack.pop()
            if current_cell in visited:
                continue
            visited.add(current_cell)

            if current_cell == end_cell:
                self.solution_path = path
                return path

            neighbors = current_cell.get_neighbors(
                self.cols, self.rows, self.grid_cells)
            for neighbor in neighbors:
                if neighbor not in visited and not self.has_wall_between(current_cell, neighbor):
                    stack.append((neighbor, path + [neighbor]))

        return []

    def has_wall_between(self, cell1, cell2):
        """
        Check if there is a wall between two adjacent cells.

        :param cell1: The first cell.
        :param cell2: The second cell.
        :return: True if there is a wall between the cells, False otherwise.
        """
        dx = cell1.x - cell2.x
        dy = cell1.y - cell2.y

        if dx == 1:  # cell2 is to the left of cell1
            return cell1.walls['left'] or cell2.walls['right']
        elif dx == -1:  # cell2 is to the right of cell1
            return cell1.walls['right'] or cell2.walls['left']
        elif dy == 1:  # cell2 is above cell1
            return cell1.walls['top'] or cell2.walls['bottom']
        elif dy == -1:  # cell2 is below cell1
            return cell1.walls['bottom'] or cell2.walls['top']
        return True

    def remove_walls(self, current, next):
        """
        Remove the walls between two adjacent cells.

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
