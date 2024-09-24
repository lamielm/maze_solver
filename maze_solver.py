# Name: Landon Lamie
# Class: CIS 226 T-Th
# Date: 10/01/2024

"""Maze Solver Module"""


class MazeSolver:
    """This class is used for solving a 2d list maze.

    You might want to add other methods to help you out.
    A print maze method would be very useful, and probably necessary to print the solution.
    If you are real ambitious, you could make a separate class to handle that."""

    def __init__(self):
        """Constructor for MazeSolver"""

        # NOTE: Though not required, you may wan to define some class level
        # variables here that you are able to access and set anywhere during
        # recursion. This is why the init constructor is defined here for you.

        # Make a flag for when the puzzle is solved (LL)
        pass

    def solve_maze(self, maze, x_start, y_start):
        """This is the public method that will allow someone to use this class to solve the maze.
        Feel free to change the return type, or add more parameters if you like.
        But, it can be done exactly as it is here without adding anything other
        than code in the body."""
        pass

    def _maze_traversal(self, current_y, current_x):
        # Move down
        # I need to move from [0][0] to [1][0].  This is [y][x].
        # Move up
        # I need to move from [1][0] to [0][0].  This is [y][x].
        # Move right
        # I need to move from [0][0] to [0][1].  This is [y][x].
        # Move left
        # I need to move from [0][1] to [0][0].  This is [y][x].

        """This should be the recursive method that gets called to solve the maze.
        Feel free to have it return something if you would like. But, it can be
        done without having it return anything. Also feel free to change the
        signature to take in parameters that you might need.

        This is only a very small starting point.
        More than likely you will need to pass in at a minimum the current position
        in X and Y maze coordinates. EX: _maze_traversal(current_x, current_y)"""
        pass
