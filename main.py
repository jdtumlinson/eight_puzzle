from board import Board
import numpy as np
import time
from agent import *
import matplotlib.pyplot as plt

def main():
    
    for m in [10,20,30,40,50]:
        results = []
        for seed in range(0,10):
            # Sets the seed of the problem so all students solve the same problems
            board = Board(m, seed)
            
            start =  time.process_time()   
            '''
            ***********************************************
            Solve the Board state here with A*
            ***********************************************
            '''
            def BF(board: Board):
                return 0
            
            result = a_star_search(board, BF)
            # result = a_star_search(board, MT)
            # result = a_star_search(board, CB)
            # result = a_star_search(board, NA)
            
            end =  time.process_time()
            solution_cpu_time = end-start
            results.append(solution_cpu_time)

            print(f"M: {m}\nSeed: {seed}\nTime: {solution_cpu_time}")
        plt.plot([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], results)
        plt.xlabel("Seed")
        plt.ylabel("Time")
        plt.show()
        results = []

if __name__ == "__main__":
    main()
