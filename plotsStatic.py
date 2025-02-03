from board import Board
import numpy as np
import time
from agent import *
import matplotlib.pyplot as plt

def BF(board: Board) -> int:
    """Breadth first search heurisitc

    Args:
        board (Board): Board object

    Returns:
        int: Always 0
    """
    return 0



def test(board: Board, heuristic: Callable[[Board], int]) -> tuple[list[str], int, float]:
    """Function used to test a heuristic function

    Args:
        board (Board): Board object
        heuristic (Callable[[Board], int]): Heurisitic function

    Returns:
        tuple[list[str], int, float]: A list of result strings, the number nodes, and CPU run time
    """
    start = time.process_time()
    result, nodes = a_star_search(board, heuristic)
    end =  time.process_time()
    
    return result, nodes, end - start



def main():
    #Create lists for all graphs
    per_solv = [[] for _ in range(4)]
    num_nodes = [[] for _ in range(4)]
    avg_time = [[] for _ in range(4)]
    avg_len = [[] for _ in range(4)]
    i = 0                       #iteration count
    M = [10,20,30,40,50]        #m-values
    S = [21, 77, 39, 8, 402]    #seeds
        
    def addToList(board: Board, result: list[str], nodes: int, time: float) -> None:
        """Function to add results of a_star_search() to a list

        Args:
            board (Board): Board object
            result (list[str]): Output list of results from running a_star_search()
            nodes (int): Number of nodes
            time (float): CPU run time
        
        Returns:
            None
        """
        per_solv[i].append(1 if board.check_solution(result) == True else 0)
        num_nodes[i].append(nodes)
        avg_time[i].append(time)
        avg_len[i].append(len(result))
    
    #Iterate through the m-values and seeds
    for m, seed in zip(M, S):
        board = Board(m, seed)

        #Repeat for each function
        for func in [BF, MT, CB, NA]:
            result, nodes, time = test(board, func)
            addToList(board, result, nodes, time)
        
        print(f"Iteration done: M = {m}, Seed = {seed}\n")
        
    #Calculate results
    for i in range(4): per_solv[i] = [sum(per_solv[i]) / 5 * 100]
    per_solv = np.concatenate(per_solv).tolist()
    for i in range(4): num_nodes[i] = [sum(num_nodes[i])]
    num_nodes = np.concatenate(num_nodes).tolist()
    for i in range(4): avg_time[i] = [sum(avg_time[i]) / 5]
    avg_time = np.concatenate(avg_time).tolist() 
    for i in range(4): avg_len[i] = [sum(avg_len[i]) / 5]
    avg_len = np.concatenate(avg_len).tolist()
    
    #Lists for graphs
    lists = [per_solv, num_nodes, avg_time, avg_len]
    titles = ["Percent of Problems Solved for h(n)'s", "Number of Search Nodes for h(n)'s", "Average CPU Time for h(n)'s", "Average Solution Length for h(n)'s"]
    y_labels = ["Percent of Problems Solved", "Number of Search Nodes", "Average CPU Time", "Average Solution Length"]
    fileNames = ["perSolv_randPlots.png", "numNodes_randPlots.png", "avgCpu_randPlots.png", "soluLen_randPlots.png"]
    
    #Output graphs to correct files
    for x_axis, title, y_label, fileName in zip(lists, titles, y_labels, fileNames):
        plt.clf()
        plt.bar(["BF", "MT", "CB", "NA"], x_axis)
        plt.title(f"{title}")
        plt.xlabel("Hesuristic Function")
        plt.ylabel(y_label)
        plt.savefig("plots/staticPlots/" + fileName)

if __name__ == "__main__":
    main()
