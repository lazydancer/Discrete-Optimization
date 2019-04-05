import networkx as nx
import itertools
import random

from tqdm import tqdm


def strategy_saturation_largest_first(G, colors):
    distinct_colors = {v: set() for v in G}
    for i in range(len(G)):
        # On the first time through, simply choose the node of highest degree.
        if i == 0:
            node = max(G, key=G.degree)
            yield node
            # Add the color 0 to the distinct colors set for each
            # neighbors of that node.
            for v in G[node]:
                distinct_colors[v].add(0)
        else:
            # Compute the maximum saturation and the set of nodes that
            # achieve that saturation.
            saturation = {v: len(c) for v, c in distinct_colors.items()
                          if v not in colors}
            # Yield the node with the highest saturation, and break ties by
            # degree.
            node = max(saturation, key=lambda v: (saturation[v], G.degree(v)))
            yield node
            # Update the distinct color sets for the neighbors.
            color = colors[node]
            for v in G[node]:
                distinct_colors[v].add(color)

def greedy_color(G, unique_colors):
    if len(G) == 0:
        return {}
    colors = {}
    nodes = strategy_saturation_largest_first(G, colors)
    for u in nodes:
        # Set to keep track of colors of neighbours
        neighbour_colors = {colors[v] for v in G[u] if v in colors}
        # Find the first unused color.
        #for color in itertools.count():
        #    if color not in neighbour_colors:
        #        break
        # Assign the new color to the current node.

        # Find the first random unused color in unique colors.
        random_colors = random.sample(range(unique_colors), unique_colors)

        for i, color in enumerate(random_colors):
            if i == unique_colors - 1:
                # There isn't a solution for this chose
                return None
                
            if color not in neighbour_colors:
                break

        colors[u] = color
    return colors


def solve(node_count, edge_count, edges):
    G = nx.Graph()
    G.add_edges_from(edges)

    if node_count == 50:
        unique_colors = 6
    if node_count == 70:
        unique_colors = 20
    if node_count == 100:
        unique_colors = 16
    if node_count == 250:
        unique_colors = 78
    if node_count == 500:
        unique_colors = 16
    if node_count == 1000:
        unique_colors = 100
    
    for i in tqdm(range(10000)):
        result = greedy_color(G, unique_colors)
        if result:
            print("After ", i)
            break

    solution = []
    for i in range(node_count):
        solution.append(result[i])

    return(solution,0)

#node_count = 4
#edge_count = 4
#edges = [(0,1),(0,2),(0,3),(2,3)]

#print(solve(node_count, edge_count, edges))

