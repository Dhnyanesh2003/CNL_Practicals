def distance_vector_routing(graph, start):
    # Initialize distance vector with inf (infinity) and set start node distance to 0
    dist = [float('inf')] * len(graph)
    dist[start] = 0

    # Relax the edges for each node
    for _ in range(len(graph) - 1):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if graph[u][v] != 0 and dist[u] + graph[u][v] < dist[v]:
                    dist[v] = dist[u] + graph[u][v]

    # Print shortest paths
    for i in range(len(graph)):
        print(f"Node {i}: {dist[i] if dist[i] != float('inf') else 'No path'}")


# Adjacency matrix for a 4-node graph
graph = [
    [0, 1, 4, 0],
    [1, 0, 4, 2],
    [4, 4, 0, 3],
    [0, 2, 3, 0]
]

# Input: Start node
start_node = int(input("Enter the start node (0 to 3): "))
distance_vector_routing(graph, start_node)
