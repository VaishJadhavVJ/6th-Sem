# Implementing Breadth-First Search (BFS) algorithm recursively

from collections import deque

# Define the undirected graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}

# Recursive function to perform BFS traversal
def bfs_recursive(queue, visited):
    if not queue:
        return  # Base case: If the queue is empty, return

    vertex = queue.popleft()  # Dequeue a vertex from the left of the queue
    visited.add(vertex)
    print(vertex, end=' ')  # Print the visited vertex

    # Add unvisited neighbors of the current vertex to the right of the queue
    for neighbor in graph[vertex]:
        if neighbor not in visited and neighbor not in queue:
            queue.append(neighbor)

    bfs_recursive(queue, visited)  # Recursive call with the updated queue and visited set


# Function to initiate BFS traversal
def bfs_traversal(start):
    queue = deque()  # Queue to keep track of vertices to visit
    visited = set()  # Set to keep track of visited vertices

    queue.append(start)  # Enqueue the starting vertex
    visited.add(start)

    bfs_recursive(queue, visited)


# Perform BFS traversal starting from vertex 'A'
print("BFS Traversal:")
bfs_traversal('A')
