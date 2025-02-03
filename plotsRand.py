from board import Board
import numpy as np
import time
from agent import *
import matplotlib.pyplot as plt
import random

def BF(board: Board):
    return 0



def test(board: Board, heuristic: Callable[[Board], int]) -> tuple[list[str], float]:
    start = time.process_time()
    result, nodes = a_star_search(board, heuristic)
    end =  time.process_time()
    
    return result, nodes, end - start



def main():
    per_solv = [[] for _ in range(4)]
    num_nodes = [[] for _ in range(4)]
    avg_time = [[] for _ in range(4)]
    avg_len = [[] for _ in range(4)]
    i = 0
    M = [random.randint(10, 100) for _ in range(5)]
    S = [random.randint(1, 100) for _ in range(5)]
        
    def addToList(board, result, nodes, time, i):
        per_solv[i].append(1 if board.check_solution(result) == True else 0)
        num_nodes[i].append(nodes)
        avg_time[i].append(time)
        avg_len[i].append(len(result))
    
    for m, seed in zip(M, S):
        board = Board(m, seed)

        for func, itr in zip([BF, MT, CB, NA], [0, 1, 2, 3]):
            result, nodes, time = test(board, func)
            addToList(board, result, nodes, time, itr)
        
        print(f"Iteration done: M = {m}, Seed = {seed}\n")
        
    for i in range(4): per_solv[i] = [sum(per_solv[i]) / 5 * 100]
    per_solv = np.concatenate(per_solv).tolist()
    for i in range(4): num_nodes[i] = [sum(num_nodes[i])]
    num_nodes = np.concatenate(num_nodes).tolist()
    for i in range(4): avg_time[i] = [sum(avg_time[i]) / 5]
    avg_time = np.concatenate(avg_time).tolist() 
    for i in range(4): avg_len[i] = [sum(avg_len[i]) / 5]
    avg_len = np.concatenate(avg_len).tolist()
    
    lists = [per_solv, num_nodes, avg_time, avg_len]
    titles = ["Percent of Problems Solved for h(n)'s", "Number of Search Nodes for h(n)'s", "Average CPU Time for h(n)'s", "Average Solution Length for h(n)'s"]
    y_labels = ["Percent of Problems Solved", "Number of Search Nodes", "Average CPU Time", "Average Solution Length"]
    fileNames = ["perSolv_randPlots.png", "numNodes_randPlots.png", "avgCpu_randPlots.png", "soluLen_randPlots.png"]
    
    for x_axis, title, y_label, fileName in zip(lists, titles, y_labels, fileNames):
        plt.clf()
        plt.bar(["BF", "MT", "CB", "NA"], x_axis)
        plt.title(f"{title}")
        plt.xlabel("Hesuristic Function")
        plt.ylabel(y_label)
        plt.savefig("plots/randomPlots/" + fileName)

if __name__ == "__main__":
    main()
