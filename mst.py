from collections import defaultdict
import heapq

def minimum_spanning_tree(graph):
    # Create a defaultdict to store the adjacency list representation of the graph
    adj_list = defaultdict(list)
    
    # Convert the graph into adjacency list format
    for u, v, weight in graph:
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))
    
    # Starting vertex for MST (can be any vertex)
    start_vertex = list(adj_list.keys())[0]
    
    # Set to store the visited vertices
    visited = set([start_vertex])
    
    # Priority queue to store the edges based on their weights
    edges = [(weight, start_vertex, v) for v, weight in adj_list[start_vertex]]
    heapq.heapify(edges)
    
    # Minimum spanning tree
    mst = []
    
    # Iterate until all vertices are visited or all edges are explored
    while edges:
        weight, u, v = heapq.heappop(edges)
        
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            
            for next_v, next_weight in adj_list[v]:
                if next_v not in visited:
                    heapq.heappush(edges, (next_weight, v, next_v))
    
    return mst

# Example usage
graph = [
    ('A', 'B', 4),
    ('A', 'C', 3),
    ('B', 'C', 6),
    ('B', 'D', 1),
    ('C', 'D', 3),
    ('D', 'E', 4)
]

mst = minimum_spanning_tree(graph)

# Print the minimum spanning tree
for u, v, weight in mst:
    print(f"{u} -- {v} : {weight}")
