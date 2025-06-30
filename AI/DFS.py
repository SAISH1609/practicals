def dfs(adj_list, start_node, target_node):
    visited = set()  
    queue = []  
    queue.append(start_node)
    traversal = []  
    parent={}
    parent[start_node]=None
    path=[]
    while queue: # Exexute till the queue is not empty
        current_node=queue.pop() #current_node=queue.pop() for DFS as it will pop from the left 
        if current_node not in visited:  
            traversal.append(current_node)  
            visited.add(current_node)
            for neighbor in adj_list[current_node]:
                if neighbor not in visited:
                        queue.append((neighbor))
                        parent[neighbor]=current_node
    node=target_node
    while node!=None:
        path.append(node)
        node=parent[node]
    path.reverse()
    return traversal, path  # Return traversal after finishing the entire DFS
# Input adjacency list representation of the graph
adj_list = {}
print("Enter the adjacency list (format: node neighbor1 neighbor2 ...; empty line to end):")
while True:
    line = input()
    if not line.strip():  # Stop input on empty line
        break     # Checks if the input line is empty (contains only spaces or is blank). If true, the loop breaks.
    parts = list(map(int, line.split()))
    node, neighbors = parts[0], parts[1:]
    adj_list[node] = neighbors
start_node = int(input("Enter the start node: "))
target_node = int(input("Enter the target node: "))

# Perform DFS
traversal, path = dfs(adj_list, start_node, target_node)

# Output results
print("DFS Traversal:", traversal)
print("Path from {} to {}:".format(start_node, target_node), path)
