import heapq

def a_star_search(graph, heuristics, start, goal, edge_costs):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristics[start], 0, start))  #h(start),g(start)=0,node
    visited = set()
    parent = {start: None}
    g_costs = {start: 0} 
    traversal = []
    
    while priority_queue:
        f_cost, g_cost, current_node = heapq.heappop(priority_queue)
        
        if current_node in visited:
            continue
        
        #print(f"{current_node},{parent[current_node]}, Cost: {g_cost}")
        visited.add(current_node)
        traversal.append(current_node)
        
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            print("Total cost:", g_costs[goal])
            print("Traversal:", " -> ".join(traversal))
            return path
        
        for neighbor in graph.get(current_node, []):
            if neighbor in visited:
                continue
            
            new_g_cost = g_costs[current_node] + edge_costs[(current_node, neighbor)]
            new_f_cost = new_g_cost + heuristics[neighbor]
            
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                heapq.heappush(priority_queue, (new_f_cost, new_g_cost, neighbor))
                parent[neighbor] = current_node
    
    print("Traversal:", " -> ".join(traversal))
    return None 

graph = {}
heuristics = {}
edge_costs = {}

num_edges = int(input("Enter the number of edges: "))
print("Enter edges in the format: node1 node2 cost")
for _ in range(num_edges):
    node1, node2, cost = input().split()
    cost = int(cost)
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    graph[node1].append(node2)
    graph[node2].append(node1)
    edge_costs[(node1, node2)] = cost
    edge_costs[(node2, node1)] = cost

num_nodes = int(input("Enter the number of nodes: "))
print("Enter heuristic cost for each node (node cost):")
for _ in range(num_nodes):
    node, cost = input().split()
    heuristics[node] = int(cost)

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

path = a_star_search(graph, heuristics, start, goal, edge_costs)
if path:
    print("A* Search Path:", " -> ".join(path))
else:
    print("No path found.")
