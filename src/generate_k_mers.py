def generate_k_mers(sequence: str, k: int) -> list[str]:
  k_mers = []
  for i in range(len(sequence) - k + 1):
    k_mers.append(sequence[i:i + k])

  k_mers.sort()

  return k_mers

def export_k_mers(k_mers: list[str], output_file: str) -> None:
  with open(output_file, 'w') as f:
    for i in range(len(k_mers)):
      if i == len(k_mers) - 1:
        f.write(f'{k_mers[i]}')
        continue

      f.write(f'{k_mers[i]},')
    