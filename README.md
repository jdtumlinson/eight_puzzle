# Eight Puzzle Assignment

This repository contains the code for solving the _Eight Puzzle_ problem. In essense, there is a 3x3 board containing the numbers zero through eight. We want to move these numbers so that they appear in a goal state; in this case the goal state is having all numbers shown as follows:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 0]]

Three different heuristics functions are implented:
- The Manhattan Distance:
    Calculates how many moves it would require to move a number to the goal spot if the board only contained said number
- Missplaced Tiles:
    Calculates the number of misplaced tiles
- Manhattan Distance with Punishments:
    Calculate the Manhattan distance and adds "2" times the number of numbers that are in the spots of other numbers (i.e. adds 2 to the cost is number "1" is in the spot of number "3" and vice versa).

# To Run
To run the program use either `python3 main.py` to run a test of 50 different m-value and seed combinations as well as display graphs of average time or use `python3 test.py` to run a test of the algorithms, testing if they return the optimal path or not.
