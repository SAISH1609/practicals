MOVES = {
    "UP": (-1, 0), "DOWN": (1, 0),
    "LEFT": (0, -1), "RIGHT": (0, 1)
}

def misplaced_tiles(state, goal):
    return sum(state[i][j] != goal[i][j] and state[i][j] != 0 for i in range(3) for j in range(3))

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def generate_next_states(state):
    x, y = find_blank(state)
    next_states = []
    
    for dx, dy in MOVES.values():
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]  
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]  # Swap blank with adjacent tile
            next_states.append(new_state)
    
    return next_states

def hill_climbing_8_puzzle(start, goal):
    current = start
    path = [(current, misplaced_tiles(current, goal))]  

    while True:
        next_states = generate_next_states(current)
        next_states.sort(key=lambda s: misplaced_tiles(s, goal)) 
        best_state = next_states[0] if next_states else None

        if best_state and misplaced_tiles(best_state, goal) <= misplaced_tiles(current, goal):
            current = best_state
            path.append((current, misplaced_tiles(current, goal)))  
        else:
            break  

    return path

def get_input(prompt):
    print(prompt)
    return [list(map(int, input().split())) for _ in range(3)]

start_state = get_input("\nEnter the start state (blank tile as 0):")
goal_state = get_input("\nEnter the goal state (blank tile as 0):")
solution_path = hill_climbing_8_puzzle(start_state, goal_state)

print("\nSolution Path:")
for step_num, (step, heuristic) in enumerate(solution_path):
    print(f"Step {step_num}: Heuristic Value = {heuristic}")
    for row in step:
        print(row)
    print()

# Check if goal state was reached
if solution_path[-1][0] == goal_state:
    print("\nGoal Reached!")
else:
    print("\nStuck in Local Optimum, goal not reached.")
