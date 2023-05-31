import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, src, dest, weight):
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))

    def dijkstra(self, source):
        # Initialize distances array with infinity
        distances = [float('inf')] * self.V
        distances[source] = 0

        # Create a priority queue to store vertices and their distances
        pq = []
        heapq.heappush(pq, (0, source))

        while pq:
            # Extract the minimum distance vertex from the priority queue
            dist, u = heapq.heappop(pq)

            # Check if the extracted vertex is already processed
            if dist > distances[u]:
                continue

            # Traverse through all adjacent vertices of the current vertex
            for v, weight in self.graph[u]:
                # Update the distance if a shorter path is found
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))

        # Print the shortest distances from the source vertex to all other vertices
        self.print_distances(distances, source)

    def print_distances(self, distances, source):
        print("Vertex\tDistance from Source")
        for v in range(self.V):
            print(f"{v}\t{distances[v]}")


# Driver code
if __name__ == "__main__":
    # Create a graph with 6 vertices
    g = Graph(6)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 7)
    g.add_edge(2, 4, 3)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 5)

    # Find and print the shortest distances using Dijkstra's algorithm
    source_vertex = 0
    g.dijkstra(source_vertex)
