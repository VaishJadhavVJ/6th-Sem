import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_mst(self, parent):
        """ Print the Minimum Spanning Tree """
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")

    def min_key(self, key, mst_set):
        """ Find the vertex with the minimum key value from the set of vertices not yet included in MST """
        min_value = sys.maxsize
        min_index = None
        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v
        return min_index

    def prim_mst(self):
        """ Perform Prim's algorithm to find the Minimum Spanning Tree """
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)


# Get the number of vertices from the user
num_vertices = int(input("Enter the number of vertices: "))

# Create a graph instance with the specified number of vertices
g = Graph(num_vertices)

# Get the edge weights from the user and populate the graph matrix
print("Enter the edge weights (separated by space):")
for i in range(num_vertices):
    weights = list(map(int, input().split()))
    for j in range(num_vertices):
        g.graph[i][j] = weights[j]

# Find and print the Minimum Spanning Tree
g.prim_mst()
