# Assignment 2 - Recursion to solve a maze

## Author

Landon Lamie

## Description

You must write a program to traverse a 12 x 12 maze and find a successful path from a starting point to an exit. You are given a hard coded maze in the program as a 2d List (List of Lists), as well as some starting coordinates.

Each spot in the maze is represented by either a '#' or a '.' (dot). The #'s represent the walls of the maze, and the dots represent paths through the maze. Moves can be made only up, down, left, or right (not diagonally), one spot at a time, and only over paths (not into or across a wall).

The exit will be any spot that is on the outside of the maze. As your program attempts to find a path leading to the exit, it should place the character 'X' in each spot along the path. If a dead end is reached, your program should replace the X’s with 'O'. But, the spots with 'O' should be marked back to 'X' if these spots are part of a successful path leading to a final state.

The output of your program is the maze configuration after each move. In your testing, you may assume that each maze has a path from its starting point to its exit point. If there is no exit, you will arrive at the starting spot again.

In addition to solving the maze as is, I want you to also solve the transposition of the maze. There is a method stub in the main program for transposing the 2D array. This method is just that, a stub. You need to fill out the code to make that transpose method work. The program is already setup to solve both the original maze, and the transposed maze. Your program should be able to solve both of them without any issue.

You are required to use recursion to solve this problem.

Please remember to fill out this README file with the relevant information that is missing.

Also make sure that you comment your name at the top of each file, and add comments for each method.

Comment anything else that isn't obvious about what you are trying to do in the code.

Lastly, I also want you to comment the recursive method you implement thoroughly to show me that you know what is going on inside your method.

I have included some pictures of sample output at various points of solving below. Note that you do NOT have to change colors, but, you should know how to do that now and it might make reading your output a little easier.

![CIS237 Assignment 2 Output 1](https://barnesbrothers.net/cis237/assignmentImages/cis237_assignment_2_st_output_1.png)
![CIS237 Assignment 2 Output 2](https://barnesbrothers.net/cis237/assignmentImages/cis237_assignment_2_st_output_2.png)
![CIS237 Assignment 2 Output 3](https://barnesbrothers.net/cis237/assignmentImages/cis237_assignment_2_st_output_3.png)

### Notes

It might be useful while developing this program to use a smaller sized maze first, and then get it to work with the real ones. Especially when first trying to make sure that the program does what you are expecting. EX: expecting it to go right and then it actually goes right.

Don't forget that you must have a base case for your recursive method or you will continue to get a stack overflow.

## Grading
| Feature                   | Points |
|---------------------------|--------|
| Solve Maze 1              | 15     |
| Solve Maze 2              | 15     |
| Transpose Maze            | 10     |
| Used Recursion            | 10     |
| Places X's                | 10     |
| Places O's                | 10     |
| Prints Each Step          | 10     |
| Print Solved Result       | 5      |
| Document Recursive Method | 5      |
| Documentation             | 5      |
| README                    | 5      |
| **Total**                 | **100**|

## Outside Resources Used

None

## Known Problems, Issues, And/Or Errors in the Program

None
