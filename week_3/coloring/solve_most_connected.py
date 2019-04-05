class Node():
  def __init__(self, links):
    self.color = None
    self.links = links

def create_graph(edges, node_count):
  graph = [None] * node_count
  for id in range(node_count):
    node_links = list(filter(lambda x: id in x, edges))
    
    linked_to = []
    for link in node_links:
      if link[0] == id:
        linked_to.append(link[1])
      if link[1] == id:
        linked_to.append(link[0])

    graph[id] = Node(linked_to)

  return graph

def pick_color(graph, node, colors):
  colors_around = set()
  for link in node.links:
    colors_around.add(graph[link].color)
  colors_around = set(filter(None.__ne__, colors_around))

  colors_avaiable = set(range(colors)) - colors_around 

  if colors_avaiable:
    return colors_avaiable.pop()
  else:
    return colors

def solve(node_count, edge_count, edges):
  graph = create_graph(edges, node_count)
  colors = 0
  for node in sorted(graph, key= lambda x: len(x.links), reverse=True):
    color = pick_color(graph, node, colors)

    if color == colors:
      colors += 1

    node.color = color

  return (list(map(lambda x: x.color, graph)), 0)