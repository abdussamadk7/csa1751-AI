def dfs_iterative(graph, start_node):
    # Create a stack for DFS
    stack = [start_node] 
    # Set to keep track of visited nodes
    visited = set() 
    while stack:
        # Pop a node from the top of the stack
        node = stack.pop() 
        if node not in visited:
            print(node, end=" ")  # Process the node (e.g., print it)
            visited.add(node) 
            # Push all unvisited neighbors onto the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor) 
# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_iterative(graph, 'A')
