g = 0 

def print_board(elements): 
    for i in range(9): 
        if i % 3 == 0: 
            print() 
        if elements[i] == -1: 
            print("_", end=" ") 
        else: 
            print(elements[i], end=" ") 
    print() 

def solvable(start): 
    inv = 0 
    arr = [x for x in start if x != -1] 
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if arr[i] > arr[j]: 
                inv += 1 
    return inv % 2 == 0 

def heuristic(start, goal): 
    h = 0 
    for i in range(9): 
        if start[i] == -1: 
            continue 
        goal_index = goal.index(start[i]) 
        h += abs(i - goal_index) // 3 + abs(i - goal_index) % 3 
    return h 

def moveleft(state, pos): 
    new_state = state[:] 
    new_state[pos], new_state[pos - 1] = new_state[pos - 1], new_state[pos] 
    return new_state 

def moveright(state, pos): 
    new_state = state[:] 
    new_state[pos], new_state[pos + 1] = new_state[pos + 1], new_state[pos] 
    return new_state 

def moveup(state, pos): 
    new_state = state[:] 
    new_state[pos], new_state[pos - 3] = new_state[pos - 3], new_state[pos] 
    return new_state 

def movedown(state, pos): 
    new_state = state[:] 
    new_state[pos], new_state[pos + 3] = new_state[pos + 3], new_state[pos] 
    return new_state 

def movetile(start, goal): 
    emptyat = start.index(-1) 
    row, col = divmod(emptyat, 3) 
    candidates = [] 

    if col - 1 >= 0: 
        left = moveleft(start, emptyat) 
        candidates.append((heuristic(left, goal), left)) 
    if col + 1 < 3: 
        right = moveright(start, emptyat) 
        candidates.append((heuristic(right, goal), right)) 
    if row - 1 >= 0: 
        up = moveup(start, emptyat) 
        candidates.append((heuristic(up, goal), up)) 
    if row + 1 < 3: 
        down = movedown(start, emptyat) 
        candidates.append((heuristic(down, goal), down)) 

    candidates.sort(key=lambda x: x[0]) 
    return candidates[0][1] 

def solveEight(start, goal, visited): 
    global g 
    g += 1 
    print(f"\nMove {g}:") 
    print_board(start) 

    if start == goal: 
        print("\nPuzzle solved!") 
        return True 

    visited.add(tuple(start)) 
    next_state = movetile(start, goal) 

    if tuple(next_state) in visited: 
        print("Cycle detected. Backtracking...") 
        return False 

    return solveEight(next_state, goal, visited) 

def main(): 
    global g 
    g = 0 
    start = [] 
    goal = [] 

    print("Enter the start state (use -1 for empty space):") 
    for _ in range(9): 
        start.append(int(input())) 

    print("Enter the goal state (use -1 for empty space):") 
    for _ in range(9): 
        goal.append(int(input())) 

    print("\nStart State:") 
    print_board(start) 

    if solvable(start): 
        visited = set() 
        if solveEight(start, goal, visited): 
            print(f"\nSolved in {g} moves.") 
        else: 
            print("\nStuck! No optimal solution found with greedy heuristic.") 
    else: 
        print("This puzzle is not solvable.") 

if __name__ == "__main__": 
    main()