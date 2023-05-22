from heapq import heappop, heappush

def prim_mst(graph):
    start_node = list(graph.keys())[0]  # Choose any starting node
    visited = set([start_node])
    mst = []
    heap = []

    # Add edges of the starting node to the heap
    for neighbor, weight in graph[start_node].items():
        heappush(heap, (weight, start_node, neighbor))

    while heap:
        weight, src, dest = heappop(heap)

        if dest not in visited:
            visited.add(dest)
            mst.append((src, dest, weight))

            for neighbor, weight in graph[dest].items():
                if neighbor not in visited:
                    heappush(heap, (weight, dest, neighbor))

    return mst

# Example usage:
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 3},
    'D': {'B': 1, 'C': 3}
}

mst = prim_mst(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")
