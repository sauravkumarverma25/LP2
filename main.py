from collections import deque

# Undirected Graph Class
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Take user input for graph and starting vertex
graph = Graph()

# Get the number of edges
num_edges = int(input("Enter the number of edges: "))

# Add edges to the graph
for _ in range(num_edges):
    edge = input("Enter an edge (format: u v): ")
    u, v = map(int, edge.split())
    graph.add_edge(u, v)

start_vertex = int(input("Enter the starting vertex: "))

print("DFS Traversal:")
graph.dfs(start_vertex)
print("\n")

print("BFS Traversal:")
graph.bfs(start_vertex)
print("\n")
