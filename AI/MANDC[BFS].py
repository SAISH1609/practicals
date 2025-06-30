def missionaries_cannibals_bfs():
    def is_valid(state):
        m_left, c_left, boat = state # state is a tuple
        m_right, c_right = 3 - m_left, 3 - c_left
        if (m_left >= c_left or m_left == 0) and (m_right >= c_right or m_right == 0): # (Check Right and left side)
            return state not in visited
        return False # if state is unsafe 
       
    queue = []
    traversal = []
    solutions = []
    visited = set()
    parent = {}
    initial_state = (3, 3, 'l')
    goal_state = (0, 0, 'r')  
    queue.append(initial_state)
    parent[initial_state] = None  
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  
          
    while queue:
        current_node=queue.pop(0) #current_node=queue.pop() for DFS as it will pop from the left 
        if current_node not in visited:  
            traversal.append(current_node)  
            visited.add(current_node)
        
        # Generate possible next states 
        m_left, c_left, boat = current_node             
        for m, c in moves:
            if boat == 'l': 
                new_state = (m_left - m, c_left - c, 'r')
            else: 
                new_state = (m_left + m, c_left + c, 'l')            
            if min(new_state[:2]) >= 0 and max(new_state[:2]) <= 3 and new_state not in visited and is_valid(new_state):
                #new_state[:2] means m_left and c_left
                parent[new_state] = current_node
                queue.append(new_state)                
                if new_state == goal_state:
                    path = []
                    node = new_state
                    while node is not None:
                        path.append(node)
                        node = parent[node]
                    path.reverse()
                    solutions.append(path)
            # end of for
            # end of while
            
    if solutions: 
        return traversal, solutions
    else:
        return traversal, "No solution exists"


traversal, paths = missionaries_cannibals_bfs()

if paths == "No solution exists":
    print(paths)
else:
    print("All possible paths from initial to final state:")
    for i, path in enumerate(paths, 1):
        print(f"Solution {i}:")
        print(" -> ".join(map(str, path)))
