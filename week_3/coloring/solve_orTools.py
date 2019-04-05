
from ortools.sat.python import cp_model 

def solve(node_count, edge_count, edges):

  max_num_colors = node_count
  model = cp_model.CpModel()

  color = []
  for i in range(node_count):
    color.append(model.NewIntVar(0, max_num_colors, 'x%i' % i))

  for edge in edges:
    model.Add(color[edge[0]] != color[edge[1]])

  model.Minimize(len(color))

  solver = cp_model.CpSolver()

  status = solver.Solve(model)

  if status == cp_model.OPTIMAL:
    solution = [solver.Value(color[i]) for i in range(node_count)]
    return (solution, 1)
  else:
    print('Not FEASIBLE')


#node_count = 4
#edge_count = 4
#edges = [(0,1),(0,2),(0,3),(2,3)]

#solve(node_count, edge_count, edges)
