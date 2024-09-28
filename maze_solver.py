# Name: Landon Lamie
# Class: CIS 226 T-Th
# Date: 10/01/2024

"""Maze Solver Module"""


class MazeSolver:
    """This class is used for solving a 2d list maze.

    You might want to add other methods to help you out.
    A print maze method would be very useful, and probably necessary to print the solution.
    If you are real ambitious, you could make a separate class to handle that."""

    def __init__(self, status="incomplete"):
        """Constructor for MazeSolver"""
        # Allows for a flag to be set for whether to continue the recursion steps, or to return to previous branch (not sure terminology, but step back out essentially)
        self.status = status
        pass

    def solve_maze(self, maze, x_start, y_start):
            self._maze_traversal(maze, x_start, y_start)
        
    def _maze_traversal(self, maze, current_y, current_x):
        # Move down
        # I need to move from [0][0] to [1][0].  This is [y][x].
        #       [Current_y + 1][current_x]
        # Move up
        # I need to move from [1][0] to [0][0].  This is [y][x].
        #       [Current_y - 1][current_x]
        # Move right
        # I need to move from [0][0] to [0][1].  This is [y][x].
        #       [Current_y][current_x + 1]
        # Move left
        # I need to move from [0][1] to [0][0].  This is [y][x].
        #       [Current_y][current_x - 1]
        
        # This flag helps back out of recursion, and will turn to "complete" once the base case is met.
        if self.status == "incomplete":
            # Base case  Each is looking for values outside of the available index's of the maze
            if current_y < 0 or current_y >= len(maze) or current_x < 0 or current_x >= len(maze[0]):
                print(f"You've successfully navigated the maze (maybe)")
                self.status = "complete"

            # Turn the spot X if it's a dot (new)            
            else:
                if maze[current_y][current_x] == ".":
                        maze[current_y][current_x] = "X"
                # Turn the spot O if it's an X (not new, back tracking)
                else:
                    return
                
                for row in maze:
                    print(" ".join(row))

                print()

                # Recursive call to go down
                self._maze_traversal(maze, current_y + 1, current_x)
                # Recursive call to go right
                self._maze_traversal(maze, current_y, current_x + 1)
                # Recursive call to go up
                self._maze_traversal(maze, current_y - 1, current_x)
                # Recursive call to go left
                self._maze_traversal(maze, current_y, current_x - 1)

                maze[current_y][current_x] = "O"
                return        

