def water_jug_bfs(m, n, d):
    def is_valid(state):
        return state not in visited
    
    visited = set()
    initial_state = (0, 0)
    queue = []
    queue.append(initial_state)
    parent = {}
    parent[initial_state] = None
    traversal = []
    solutions = []
    
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
            solutions.append(path)
        
        next_states = [
            (m, jug2),  # Fill jug1 completely
            (jug1, n),  # Fill jug2 completely
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, n - jug2), jug2 + min(jug1, n - jug2)),  # Pour jug1 -> jug2
            (jug1 + min(m - jug1, jug2), jug2 - min(m - jug1, jug2))   # Pour jug2 -> jug1
        ]
        
        for state in (next_states): # reversed not required for BFS
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

traversal, paths = water_jug_bfs(m, n, d)

#print("DFS Traversal:", traversal)
if paths == "No solution exists":
    print(paths)
else:
    print("All possible paths from initial to final state:")
    for i, path in enumerate(paths, 1):
        print(f"Solution {i}:")
        print(" -> ".join(map(str, path)))
