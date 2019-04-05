class Node():
  def __init__(self, links):
    self.color = None
    self.links = links
    self.options = len(links)

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
    return (colors_avaiable.pop(), colors)
  else:
    return (colors, colors + 1)

def solve(node_count, edge_count, edges):
  graph = create_graph(edges, node_count)
  colors = 0

  for _ in range(node_count):
    index, node = max(enumerate(graph), key= lambda x: x[1].options)
    color, colors = pick_color(graph, node, colors)

    # Update Graph
    node.color = color
    node.options = -1
    for link in node.links:
      graph[link].options -= 1

    #Debug output
    #print('-' * 80)
    #for i, a in enumerate(graph):
    #  print(i, a.color, a.links, a.options)

  return (list(map(lambda x: x.color, graph)), 0)
