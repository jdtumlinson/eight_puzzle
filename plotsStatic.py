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
    per_solv = [[] for _ in range(5)]
    num_nodes = [[] for _ in range(5)]
    avg_time = [[] for _ in range(5)]
    avg_len = [[] for _ in range(5)]
    i = 0                           #iteration count
    M = [10, 20, 30, 40, 50]        #m-values
    S = [21, 77, 39, 84, 402]       #seeds
        
    def addToList(board: Board, result: list[str], nodes: int, time: float, itr: int) -> None:
        """Function to add results of a_star_search() to a list

        Args:
            board (Board): Board object
            result (list[str]): Output list of results from running a_star_search()
            nodes (int): Number of nodes
            time (float): CPU run time
        
        Returns:
            None
        """
        per_solv[itr].append(1 if board.check_solution(result) == True else 0)
        num_nodes[itr].append(nodes)
        avg_time[itr].append(time)
        avg_len[itr].append(len(result))
    
    #Iterate through the m-values and seeds
    for m, seed in zip(M, S):
        board = Board(m, seed)

        #Repeat for each function
        for func in [BF, MT, CB, NA]:
            result, nodes, time = test(board, func)
            addToList(board, result, nodes, time, i)

        i += 1        
        print(f"Iteration done: M = {m}, Seed = {seed}\n")
        
    #Calculate results
    for i in range(5): per_solv[i] = [sum(per_solv[i]) / 4 * 100]
    per_solv = np.concatenate(per_solv).tolist()
    for i in range(5): num_nodes[i] = [sum(num_nodes[i]) / 5000]
    num_nodes = np.concatenate(num_nodes).tolist()
    for i in range(5): avg_time[i] = [sum(avg_time[i]) / 4 * 50]
    avg_time = np.concatenate(avg_time).tolist() 
    for i in range(5): avg_len[i] = [sum(avg_len[i]) / 4 * 5]
    avg_len = np.concatenate(avg_len).tolist()
    
    w = 0.2
    bar1 = np.arange(len(M))
    bar2 = [i + w for i in bar1]
    bar3 = [i + w for i in bar2]
    bar4 = [i + w for i in bar3]
    mVal = ["10", "20", "30", "40", "50"]
    plt.bar(bar1, per_solv, w, color="red", label="Percent Solved")
    plt.bar(bar2, num_nodes, w, color="blue", label="Number of Search Nodes")
    plt.bar(bar3, avg_time, w, color="green", label="Average CPU Time")
    plt.bar(bar4, avg_len, w, color="yellow", label="Average Solution Length")
    plt.xlabel("m-values")
    plt.legend()
    plt.xticks([0, 1, 2, 3, 4], mVal)
    plt.title("m-Value Statistics")
    plt.savefig("plots/combinedPlots.png")
    plt.show()
    
    
    
    #Output graphs to correct files

    # for x_axis, title, y_label, fileName in zip(lists, titles, y_labels, fileNames):
    #     plt.clf()
    #     plt.bar(["BF", "MT", "CB", "NA"], x_axis)
    #     plt.title(f"{title}")
    #     plt.xlabel("Hesuristic Function")
    #     plt.ylabel(y_label)
    #     plt.savefig("plots/staticPlots/" + fileName)

if __name__ == "__main__":
    main()
