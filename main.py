from board import Board
import numpy as np
import time
from agent import *
import matplotlib.pyplot as plt

def BF(board: Board):
    return 0

def test(board: Board, heuristic: Callable[[Board], int]) -> tuple[list[str], float]:
    start = time.process_time()
    result = a_star_search(board, heuristic)
    end =  time.process_time()
    
    return result, end - start

def main():
    bf_avgs, mt_avgs, cb_avgs, na_avgs, i = [], [], [], [], 0
    for m in [10,20,30,40,50]:
        bf_results, mt_results, cb_results, na_results = [], [], [], []
        for seed in range(0,10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)
            '''
            ***********************************************
            Solve the Board state here with A*
            ***********************************************
            '''

            result, time = test(board, BF)
            bf_results.append(time)
            result, time = test(board, MT)
            mt_results.append(time)
            result, time = test(board, CB)
            cb_results.append(time)
            result, time = test(board, NA)
            na_results.append(time)
            
            i += 1
            if i % 10 != 0: print(f"Test {i} of 50 completed.")
            else: print(f"Test {i} of 50 completed. New m value beginning.\n")
            
        bf_avgs.append(sum(bf_results) / 10)
        mt_avgs.append(sum(mt_results) / 10)
        cb_avgs.append(sum(cb_results) / 10)
        na_avgs.append(sum(na_results) / 10)
        
    for results, title in zip([bf_avgs, mt_avgs, cb_avgs, na_avgs], ["BF Average Times", "MT Average Times", "CB Average Times", "NA Average Times"]):
        plt.plot([10,20,30,40,50], results)
        plt.title(title)
        plt.xlabel("Seed")
        plt.ylabel("Time")
        plt.show()

if __name__ == "__main__":
    main()
