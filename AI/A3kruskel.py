# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []    # List to store the edges

    # Function to add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find set of an element i (uses path compression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union of two sets of x and y (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # The main function to construct MST using Kruskal's algorithm
    def kruskal_mst(self):
        result = []          # Stores the MST edges
        i = 0                # An index variable, used for sorted edges
        e = 0                # An index variable, used for result[]

        # Step 1: Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        # Number of edges to be taken is equal to V-1
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print the MST
        print("Edge   Weight")
        for u, v, weight in result:
            print(f"{u} - {v}   {weight}")


# Driver code
if __name__ == "__main__":
    # Get the number of vertices from the user
    num_vertices = int(input("Enter the number of vertices: "))

    # Create a graph instance
    graph = Graph(num_vertices)

    # Get the edge weights from the user
    print("Enter the edge weights (separated by space):")
    for i in range(num_vertices):
        weights = list(map(int, input().split()))
        for j in range(num_vertices):
            if weights[j] != 0:
                graph.add_edge(i, j, weights[j])

    # Find and print the Minimum Spanning Tree using Kruskal's algorithm
    print("Minimum Spanning Tree:")
    graph.kruskal_mst()
