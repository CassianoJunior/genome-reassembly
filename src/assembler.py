from debruijn import DeBruijn
from generate_k_mers import export_k_mers, generate_k_mers

with open('samples/sample1.txt', 'r') as f:
  sequence = f.readline().strip()

export_k_mers(generate_k_mers(sequence, 12), 'files/input.txt')

with open('files/input.txt', 'r') as f:
  line = f.readline().strip()
  kmers = line.split(',')

graph = DeBruijn(kmers)

sequence = graph.get_possible_genome()

with open('files/output.txt', 'w') as f:
  f.write(sequence)
  f.write('\n')