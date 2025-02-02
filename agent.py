from __future__ import annotations
from board import Board
from collections.abc import Callable
import numpy as np

'''
Heuristics
'''
def MT(board: Board) -> int:
    return np.sum(board.solution != board.state)

def CB(board: Board) -> int:
    total = 0
    for num in range(0, 8):
        curP = np.argwhere(board.state == num)[0]
        goalP = np.argwhere(board.solution == num)[0]

        total += abs(curP[0] - goalP[0]) + abs(curP[1] - goalP[1])

    return total

def NA(board: Board) -> int:
    
    return 0



'''
A* Search 
'''
def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    queue = [[board, [], 0]]                                #Initialize a queue containing the current board, an empty list of steps and current cost
    seen = {}                                               #Create a dictionary to store boards we've already seen
    
    while(True):                                            #All boards are solvable, so repeat until solved
        curState = queue.pop(0)                             #Pop the head of the queue

        if curState[0].goal_test(): return curState[1]      #If the head is solved, return the solved path

        for move in curState[0].next_action_states():       #Iterate through the list of all possible moves
            if move[0].__str__() not in seen: seen[move[0].__str__()] = True          #If the board has not been seen, add it to the dictionary
            else: continue

            gh = curState[2] + heuristic(curState[0])       #Calculate the cost by using the current cost and a heuristic function
            
            if len(queue) == 0: queue.append([move[0], curState[1] + [move[1]], gh])        #Empty queue
            else:
                for i in range(len(queue) - 1, -1, -1):                                     #Iterate from the back, as all numbers should be getting bigger, thus faster placing
                    if queue[i][2] <= gh:
                        queue.insert(i + 1, [move[0], curState[1] + [move[1]], gh])         #Insert at correct spot and break
                        break
                    elif i == 0:
                        queue.insert(0, [move[0], curState[1] + [move[1]], gh])