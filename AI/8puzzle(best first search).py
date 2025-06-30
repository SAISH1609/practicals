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
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            next_states.append(new_state)
    return next_states

def greedy_best_first(start, goal):
    open_list = [start]
    visited = set()
    parent = {tuple(map(tuple, start)): None}

    while open_list:
        open_list.sort(key=lambda s: misplaced_tiles(s, goal))
        current = open_list.pop(0)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[tuple(map(tuple, current))]
            return path[::-1] 
        
        visited.add(tuple(map(tuple, current)))

        for neighbor in generate_next_states(current):
            if tuple(map(tuple, neighbor)) not in visited:
                parent[tuple(map(tuple, neighbor))] = current
                open_list.append(neighbor)

    return None 

def get_input(prompt):
    print(prompt)
    return [list(map(int, input().split())) for _ in range(3)]

start_state = get_input("\nEnter the start state (blank tile as 0):")
goal_state = get_input("\nEnter the goal state (blank tile as 0):")

solution = greedy_best_first(start_state, goal_state)
if solution:
    print("\nSolution Path:")
    for step in solution:
        heuristic_value = misplaced_tiles(step, goal_state)
        print(f"Heuristic Value: {heuristic_value}")
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")
