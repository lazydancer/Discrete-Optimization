import itertools

def brute_force(node_count, edge_count, edges):
    isOptimal = False

    print(edges)

    color_count = 1

    for color_count in range(node_count):
        combinations = itertools.combinations_with_replacement(range(color_count), node_count)
        count = 0
        for comb in combinations:
            count += 1
            if valid(edges, comb):
                print("Found optimal at {} in {} moves".format(color_count, count))
                return (comb, True)

        print("Nothing found in {} in {} moves".format(color_count, count))


def networkx_solve(node_count, edge_count, edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    d = nx.coloring.greedy_color(G)

    print(d)


def valid(edges, solution):

    for edge in edges:
        if solution[edge[0]] == solution[edge[1]]:
            return False

    return True
