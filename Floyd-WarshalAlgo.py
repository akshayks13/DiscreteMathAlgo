def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices in a weighted graph.
    
    Parameters:
    graph (list of lists): The adjacency matrix representation of the weighted graph.
    
    Returns:
    list of lists: The matrix of shortest path distances between all pairs of vertices.
    """
    n = len(graph)
    dist = [row[:] for row in graph] #Or [row for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# Example usage:
graph = [
    [0, float('inf'), -2, float('inf')],
    [4, 0, 3, float('inf')],
    [float('inf'), float('inf'), 0, 2],
    [float('inf'), -1, float('inf'), 0]
]

print("Original Graph (Adjacency Matrix):")
for row in graph:
    print(row)

print("\nShortest Path Distances (Floyd-Warshall Algorithm):")
shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)
