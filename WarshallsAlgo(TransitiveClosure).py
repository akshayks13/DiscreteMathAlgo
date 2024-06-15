def transitive_closure(graph):
    """
    Warshall's algorithm to find the transitive closure of a directed graph.
    
    Parameters:
    graph (list of lists): The adjacency matrix representation of the directed graph.
    
    Returns:
    list of lists: The transitive closure matrix.
    """
    n = len(graph)
    closure = [row for row in graph]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    
    return closure

# Example usage:
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

print("Original Graph:")
for row in graph:
    print(row)

print("\nTransitive Closure:")
closure = transitive_closure(graph)
for row in closure:
    print(row)
