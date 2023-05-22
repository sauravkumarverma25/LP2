class DisjointSet:
    def __init__(self, vertices):
        self.parent = {}
        self.rank = {}
        for v in vertices:
            self.parent[v] = v
            self.rank[v] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append((src, dest, weight))

    def kruskal_mst(self):
        mst = []
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Sort edges by weight
        disjoint_set = DisjointSet(self.vertices)

        for edge in self.graph:
            src, dest, weight = edge
            root_src = disjoint_set.find(src)
            root_dest = disjoint_set.find(dest)

            if root_src != root_dest:
                mst.append(edge)
                disjoint_set.union(root_src, root_dest)

        return mst


# Example usage
g = Graph(['A', 'B', 'C', 'D', 'E', 'F'])
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 3)
g.add_edge('C', 'D', 5)
g.add_edge('C', 'E', 1)
g.add_edge('D', 'E', 4)
g.add_edge('D', 'F', 2)
g.add_edge('E', 'F', 6)

mst = g.kruskal_mst()
for edge in mst:
    src, dest, weight = edge
    print(f"{src} -- {dest}: {weight}")
