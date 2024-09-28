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
    print(f"Choices: 1 for normal maze, 2 for transposed maze")
   
    user_selection = ""

    # UI for choosing regular or transposed maze
    while user_selection != "1" or user_selection != "2":
        user_selection = input(f"What would you like to solve?\n>")

        if user_selection == "1":
            # Solve the original maze
            print(f"Printing Original Maze")
            maze_solver.solve_maze(maze1, X_START, Y_START)
            return
        elif user_selection == "2":
            # Solve the transposed maze
            print(f"Printing Transposed Maze")
            maze_solver.solve_maze(maze2, X_START, Y_START)
            return
        else:
            print("Invalid input, try again")


def transpose_maze(maze_to_transpose):
    # X become Y and Y becomes X.  0,0 stays.  1,0 becomes 0,1.  1,2 becomes 2,1
    copy_of_maze = maze_to_transpose[:]
    transposed_maze = []
    #Break the list of list down into rows
    for row_index in range(len(copy_of_maze[0])):
        new_row = []
        # Break the list into columns
        for col_index in range(len(copy_of_maze)):
            # Create the new transposed rows, and append it to the empty "new_row" list
            new_row.append(copy_of_maze[col_index][row_index])
        # After each row iteration, you append the new transposed list to the empty transposed maze
        transposed_maze.append(new_row)
    return transposed_maze
    

