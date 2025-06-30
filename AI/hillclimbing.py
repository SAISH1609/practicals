import heapq
def hill_climbing(graph, heuristics, start, goal):
    node = start  
    parent = {node: None}  
    path = []     
    while True:
        neighbors = graph.get(node, []) 
        min_heap = []
        for neighbor in neighbors:
            heapq.heappush(min_heap, (heuristics[neighbor], neighbor))         
        if not min_heap:
            break        
        new_cost, new_node = heapq.heappop(min_heap)        
        if heuristics[new_node] >= heuristics[node]:
            break  
        parent[new_node] = node  
        node = new_node 
        if node == goal:
          break
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path
graph = {}
heuristics = {}
num_edges = int(input("Enter the number of edges: "))
print("Enter edges in the format: node1 node2")
for _ in range(num_edges):
    node1, node2 = input().split()
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)
num_nodes = int(input("Enter the number of nodes: "))
print("Enter heuristic cost for each node (node cost):")
for _ in range(num_nodes):
    node, cost = input().split()
    heuristics[node] = int(cost)
start = input("Enter the Start Node: ")
goal = input("Enter the Goal Node: ")
path = hill_climbing(graph, heuristics, start, goal)
if path and path[-1] == goal:
    print("Hill Climbing Path:", " -> ".join(path))
else:
    print("Goal not reached")
    print("Hill Climbing Path:", " -> ".join(path))