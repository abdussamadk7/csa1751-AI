import heapq# A* search function
def a_star(graph, start, goal, heuristic):
    # Priority queue to store (cost, node) pairs
    open_list = []
    heapq.heappush(open_list, (0, start)) 
    # To store the cost of the shortest path from start to each node
    g_costs = {start: 0} 
    # To store the parent of each node (for path reconstruction)
    came_from = {start: None} 
    while open_list:
        # Get the node with the lowest f(n) = g(n) + h(n)
        current_cost, current_node = heapq.heappop(open_list) 
        # If we have reached the goal, reconstruct the path
        if current_node == goal:
            return reconstruct_path(came_from, goal) 
        # Explore neighbors of the current node
        for neighbor, move_cost in graph[current_node]:
            # Calculate the tentative g_cost
            tentative_g_cost = g_costs[current_node] + move_cost 
            # If the new path is better, update and push it into the queue
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node 
    # If the goal is unreachable
    return None
# Reconstruct the path from start to goal
def reconstruct_path(came_from, current_node):
    path = []
    while current_node:
        path.append(current_node)
        current_node = came_from[current_node]
    return path[::-1]  # Reverse the path to get from start to goal
# Example heuristic (Euclidean distance or other appropriate heuristic)
def heuristic(node, goal):
    # For example, Manhattan distance if nodes are coordinates (tuples)
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
# Example graph (a dictionary of adjacency lists with costs)
graph = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1), ((0, 2), 1)],
    (0, 2): [((0, 1), 1), ((1, 2), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1), ((2, 0), 1)],
    (1, 1): [((1, 0), 1), ((0, 1), 1), ((2, 1), 1), ((1, 2), 1)],
    (1, 2): [((0, 2), 1), ((1, 1), 1), ((2, 2), 1)],
    (2, 0): [((1, 0), 1), ((2, 1), 1)],
    (2, 1): [((2, 0), 1), ((1, 1), 1), ((2, 2), 1)],
    (2, 2): [((2, 1), 1), ((1, 2), 1)]
}
# Example usage
start = (0, 0)
goal = (2, 2)
path = a_star(graph, start, goal, heuristic) 
if path:
    print(f"Path found: {path}")
else:
 print("No path found.")