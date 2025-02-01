    # queue = [[board, [], 0]]
    # j = 0
    # while(True):
    #     curState = queue.pop(0)
    #     if curState[0].goal_test(): return curState[1]

    #     nextMoves = curState[0].next_action_states()
    #     j += 1
    #     print(j)
    #     for move in nextMoves: 
    #         gh = curState[2] + heuristic(curState[0]) + 1

    #         if len(queue) == 0: queue.append([move[0], curState[1] + [move[1]], gh])
    #         else:
    #             for i in range(len(queue) - 1, 0, -1):
    #                 if queue[i][2] < gh: 
    #                     queue.insert(i, [move[0], curState[1] + [move[1]], gh])
    #                     break
    #                 elif i == 0: queue.insert(0, [move[0], curState[1] + [move[1]], gh])
    
l = [[1, 0], [4, 0], [6, 0], [7, 1], [9, 0], [9, 0]]
val = 7
for i in range(len(l) - 1, -1, -1):
    if l[i][0] <= val:
        l.insert(i + 1, [val, 2])
        break
        
print(l)