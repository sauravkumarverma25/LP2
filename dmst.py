from collections import defaultdict
import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity except the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Priority queue to store nodes with their distances
    pq = [(0, start)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        # Ignore outdated entries in the priority queue
        if current_dist > distances[current_node]:
            continue

        # Explore neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight

            # Update distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def minimum_spanning_tree(graph):
    start_node = next(iter(graph))
    mst = defaultdict(dict)

    distances = dijkstra(graph, start_node)

    for node, distance in distances.items():
        if node != start_node:
            for previous_node in graph[node]:
                if previous_node in distances and distances[previous_node] + graph[node][previous_node] == distance:
                    mst[previous_node][node] = graph[node][previous_node]

    return dict(mst)

# Example usage:
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

mst = minimum_spanning_tree(graph)
print(mst)