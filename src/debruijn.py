import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class DeBruijn:
  def __init__(self, kmers: list[str]):
    self.k = len(kmers[0])
    self.kmers = kmers
    self.graph = {}
    self.build_graph()

  def build_graph(self):
    for kmer in self.kmers:
      prefix = kmer[:-1]
      suffix = kmer[1:]

      if prefix not in self.graph:
        self.graph[prefix] = []
      
      self.graph[prefix].append(suffix)

  def eulerian_walk(self):
    in_degrees = defaultdict(int)
    out_degrees = defaultdict(int)
    
    for node in self.graph:
      out_degrees[node] += len(self.graph[node])
      for neighbor in self.graph[node]:
        in_degrees[neighbor] += 1
    
    # Find starting point: start at a node with (out-degree - in-degree) == 1 if it exists
    start = None
    for node in out_degrees:
      if out_degrees[node] - in_degrees[node] == 1:
        start = node
        break
    if start is None:
      # Otherwise, start at any node with an outgoing edge
      start = next((node for node in out_degrees if out_degrees[node] > 0), None)
    
    if start is None:
      # No starting point found (no edges in the graph)
      return []
    
    # Hierholzer's algorithm to find Eulerian walk
    stack = [start]
    path = []
    while stack:
      current = stack[-1]
      if out_degrees[current] > 0:
        next_node = self.graph[current].pop()
        out_degrees[current] -= 1
        stack.append(next_node)
      else:
        path.append(stack.pop())
    
    return path[::-1]
  
  def get_possible_genome(self):
    path = self.eulerian_walk()
    genome = path[0]
    for node in path[1:]:
      genome += node[-1]
    return genome

  def __str__(self):
    res = []
    for kmer in self.graph:
      res.append(f'{kmer} -> {",".join(self.graph[kmer])}')
    return "\n".join(res)
  
  def draw(self):
    G = nx.DiGraph()
    
    for node, edges in self.graph.items():
      for edge in edges:
        G.add_edge(node, edge)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=15, font_color="black", font_weight="bold", arrows=True)
    plt.show()