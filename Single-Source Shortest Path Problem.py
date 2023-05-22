import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 4},
    'C': {'A': 3, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Shortest distances from vertex", start_vertex)
for vertex, distance in distances.items():
    print(vertex, ":", distance)
