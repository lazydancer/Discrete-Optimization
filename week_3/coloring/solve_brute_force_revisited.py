import numpy as np


def solve(node_count, edge_count, edges):
    adjacency_matrix = np.zeros((node_count, node_count), dtype='bool')
    for edge in edges:
        adjacency_matrix[edge[0]][edge[1]] = True
        adjacency_matrix[edge[1]][edge[0]] = True

    color = np.full(node_count, -1, dtype='int8')
    print(adjacency_matrix, color)

    return


node_count = 4
edge_count = 4
edges = [(0,1),(0,2),(0,3),(2,3)]
print(solve(node_count, edge_count, edges))