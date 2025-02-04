from __future__ import annotations
from board import Board
from collections.abc import Callable
import numpy as np

'''
Heuristics
'''
def MT(board: Board) -> int:
    return np.sum(board.solution != board.state)                    #Return the number of items in the wrong spot

def CB(board: Board) -> int:
    total = 0
    for num in range(0, 8):                                         #Iterate through all numbers on the board
        curP = np.argwhere(board.state == num)[0]                   #Find where the current number is on the board in an x, y coordinate space
        goalP = np.argwhere(board.solution == num)[0]               #Find where the goal is...

        total += abs(curP[0] - goalP[0]) + abs(curP[1] - goalP[1])  #Calculate the Manhattan distance between the two

    return total                                                    #Return the total of all Manhattan distances

def NA(board: Board) -> int:
    total, swaps = 0, 0                                                                 #Similiar to the Manhattan distance but penalizes numbers that are in each others spaces (i.e. adds 2 to the cost is number "1" is in the spot of number "3" and vice versa)
    for num in range(0, 8):                                                             #Iterate through all numbers on the board
        curP = np.argwhere(board.state == num)[0]                                       #Find where the current number is on the board in an x, y coordinate space
        goalP = np.argwhere(board.solution == num)[0]                                   #Find where the goal is...

        total += abs(curP[0] - goalP[0]) + abs(curP[1] - goalP[1])                      #Calculate the Manhattan distance between the two
        if board.state[curP[0]][curP[1]] == board.state[goalP[0], goalP[1]]: swaps += 1 #If two pieces are in the each others spot, penalize that as it requires extra moves
        
    return total + 2 * swaps                                                            #Return the total of all Manhattan distances plus the number of items in each others spaces



'''
A* Search 
'''
def a_star_search(board: Board, heuristic: Callable[[Board], int]):
    queue = [[board, [], 0]]                                                                #Initialize a queue containing the current board, an empty list of steps and current cost
    seen = {}                                                                               #Create a dictionary to store boards we've already seen
    itr = 0                                                                                 #Number of iterations the while loop has ran through
    LIMIT = 180000                                                                       #The allowed limit of iterations
    numSearchNodes = 0
    
    while(True):                                                                            #All boards are solvable, so repeat until solved
        itr += 1                                                                            #Add one to the iteration count and return blank if it's past the allowed range
        if itr >= LIMIT: return [[], 0]
        
        curState = queue.pop(0)                                                             #Pop the head of the queue

        if curState[0].goal_test(): return [curState[1], numSearchNodes]                    #If the head is solved, return the solved path

        for move in curState[0].next_action_states():                                       #Iterate through the list of all possible moves
            if move[0].__str__() not in seen: seen[move[0].__str__()] = True                #If the board has not been seen, add it to the dictionary
            else: continue
            numSearchNodes += 1
            
            gh = curState[2] + heuristic(curState[0])                                       #Calculate the cost by using the current cost and a heuristic function
            
            if len(queue) == 0: queue.append([move[0], curState[1] + [move[1]], gh])        #Empty queue
            else:
                for i in range(len(queue) - 1, -1, -1):                                     #Iterate from the back, as all numbers should be getting bigger, thus faster placing
                    if queue[i][2] <= gh:
                        queue.insert(i + 1, [move[0], curState[1] + [move[1]], gh])         #Insert at correct spot and break
                        break
                    elif i == 0:
                        queue.insert(0, [move[0], curState[1] + [move[1]], gh])
                        break