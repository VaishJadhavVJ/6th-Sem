# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight

    # Function to find the vertex with minimum key value
    def min_key(self, key, mst_set):
        min_value = float('inf')
        min_index = -1
        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v
        return min_index

    # Function to print the MST
    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")

    # Function to construct and print MST
    def prim_mst(self):
        # Initialize key values as infinite
        key = [float('inf')] * self.V
        # Initialize parent array as empty
        parent = [None] * self.V
        # Initialize the first vertex as the root
        key[0] = 0
        mst_set = [False] * self.V

        for _ in range(self.V):
            # Choose the vertex with the minimum key value
            u = self.min_key(key, mst_set)
            # Include the vertex in the MST
            mst_set[u] = True

            # Update the key values and parent for adjacent vertices
            for v in range(self.V):
                if (
                    self.graph[u][v] != 0
                    and not mst_set[v]
                    and self.graph[u][v] < key[v]
                ):
                    key[v] = self.graph[u][v]
                    parent[v] = u

        # Print the MST
        self.print_mst(parent)


# Driver code
if __name__ == "__main__":
    # Create a graph
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 3, 6)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 8)
    g.add_edge(1, 4, 5)
    g.add_edge(2, 4, 7)
    g.add_edge(3, 4, 9)

    # Find and print the MST using Prim's algorithm
    g.prim_mst()
