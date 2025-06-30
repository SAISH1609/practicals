import heapq
def best_first_search(graph, heuristics, start, goal):
    priority_queue = [] # each element = heristic, node
    heapq.heappush(priority_queue, (heuristics[start], start)) 
    visited = set()
    parent = {}
    parent[start]=None
    traversal = []
    while priority_queue:
        cost, current_node = heapq.heappop(priority_queue)            
        if current_node in visited:
            continue
        print(f"{current_node},{parent[current_node]},Cost: {cost}")
        visited.add(current_node)
        traversal.append(current_node)
        total_cost = 0        
        if current_node == goal:
            path = []
            while current_node is not None:
                total_cost += heuristics[current_node]
                path.append(current_node)
                current_node = parent[current_node]
            print("Total cost:", total_cost)
            print("Traversal:", " -> ".join(traversal))
            path.reverse()
            return path
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristics[neighbor], neighbor))
                parent[neighbor] = current_node  
    
    print("Traversal:", " -> ".join(traversal))
    return None 
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
start = input("Enter the start node: ")
goal = input("Enter the goal node: ")
path = best_first_search(graph, heuristics, start, goal)
if path:
    print("Best First Search Path:", " -> ".join(path))
else:
    print("No path found.")
