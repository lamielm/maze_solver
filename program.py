# Name: Landon Lamie
# Class: CIS 226 T-Th
# Date: 10/01/2024

"""Program code"""

# First-party imports
from maze_solver import MazeSolver


def main(*args):
    """Method to run program"""

    # Starting Coordinates
    X_START = 1
    Y_START = 1

    # The first maze that needs to be solved.
    # NOTE: You may want to make a smaller version to test and debug with.
    # You don't have to, but it might make your life easier.
    maze1 = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#", ".", "#", "#", "#", "#", ".", "#"],
        ["#", "#", "#", ".", "#", ".", ".", ".", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", "#", "#", "#", ".", "#", ".", "."],
        ["#", "#", "#", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", "#", ".", "#", ".", "#", ".", "#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", "#"],
        ["#", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
        ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    # Create new instance of a MazeSolver
    maze_solver = MazeSolver()

    # Create the second maze by transposing the first maze
    maze2 = transpose_maze(maze1)  # May need to make a copy of this list ([:])

    # Solve the original maze
    maze_solver.solve_maze(maze1, X_START, Y_START)

    # Solve the transposed maze
    maze_solver.solve_maze(maze2, X_START, Y_START)


def transpose_maze(maze_to_transpose):
    # X become Y and Y becomes X.  0,0 stays.  1,0 becomes 0,1.  1,2 becomes 2,1
    maze_transposed = []
    return []
