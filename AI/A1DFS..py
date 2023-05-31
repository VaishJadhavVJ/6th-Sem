# Implementing Depth-First Search (DFS) algorithm recursively

# Define the undirected graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

# Recursive function to perform DFS traversal
def dfs_recursive(vertex, visited):
    # Mark the current vertex as visited
    visited.add(vertex)
    print(vertex, end=' ')  # Print the visited vertex

    # Recursive call for all unvisited neighbors of the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(neighbor, visited)


# Function to initiate DFS traversal
def dfs_traversal(start):
    visited = set()  # Set to keep track of visited vertices
    dfs_recursive(start, visited)


# Perform DFS traversal starting from vertex 'A'
print("DFS Traversal:")
dfs_traversal('A')
