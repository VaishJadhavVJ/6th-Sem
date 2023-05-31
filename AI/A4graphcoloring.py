class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def is_safe(self, v, color, coloring):
        for i in range(self.vertices):
            if self.adj_matrix[v][i] and coloring[i] == color:
                return False
        return True

    def graph_coloring_util(self, num_colors, coloring, v):
        if v == self.vertices:  # All vertices have been assigned a color
            return True
        for color in range(1, num_colors + 1):
            if self.is_safe(v, color, coloring):
                coloring[v] = color
                if self.graph_coloring_util(num_colors, coloring, v + 1):
                    return True
                coloring[v] = 0
        return False

    def graph_coloring(self, num_colors):
        coloring = [0] * self.vertices
        if self.graph_coloring_util(num_colors, coloring, 0):
            return coloring
        return None


# Example usage:
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))

graph = Graph(vertices)

print("Enter the edges (vertex u, vertex v):")
for _ in range(edges):
    u, v = map(int, input().split())
    graph.add_edge(u, v)

num_colors = int(input("Enter the number of colors: "))

coloring = graph.graph_coloring(num_colors)

if coloring is None:
    print("No solution exists.")
else:
    print("Graph coloring:")
    for vertex, color in enumerate(coloring):
        print("Vertex", vertex, "- Color", color)
