def water_jug_dfs(m, n, d):
    def is_valid(state):
        return state not in visited # returns the state only if it isnt in visited
    queue = []
    traversal = []
    solutions = []
    visited = set()
    parent = {}
    initial_state = (0, 0)
    queue.append(initial_state)
    parent[initial_state] = None
        
    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:     
            traversal.append(current_node)
            visited.add(current_node) 
            jug1, jug2 = current_node
        
        if (jug1 == d and jug2==0) or (jug1==0 and jug2 == d):
            path = []
            node = current_node
            while node != None:
                path.append(node)
                node = parent[node]
            path.reverse()
            solutions.append(path) # Keep track of all solutions
        
        next_states = [
            (m, jug2),  # Fill jug1 completely
            (jug1, n),  # Fill jug2 completely
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, n - jug2), jug2 + min(jug1, n - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(m - jug1, jug2), jug2 - min(m - jug1, jug2))   # Pour jug2 -> jug1
        ]
        
        for state in reversed(next_states): # reversed is required for DFS
            if is_valid(state):
                queue.append(state)
                parent[state] = current_node
    
    if solutions:
        return traversal, solutions
    else:
        return traversal, "No solution exists"

# Taking input from user
m = int(input("Enter capacity of jug1: "))
n = int(input("Enter capacity of jug2: "))
d = int(input("Enter the target amount: "))

traversal, solutions = water_jug_dfs(m, n, d)

#print("DFS Traversal:", traversal)
if solutions == "No solution exists":
    print(solutions)
else:
    print("All possible paths from initial to final state:")
    for i, path in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print(" -> ".join(map(str, path)))
