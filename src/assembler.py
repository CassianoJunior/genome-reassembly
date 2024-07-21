from debruijn import DeBruijn
from generate_k_mers import export_k_mers, generate_k_mers

def read_genome_file(file_path):
  with open(file_path, 'r') as f:
    sequence = f.readline().strip()
  return sequence

def read_kmers_file(file_path):
  with open(file_path, 'r') as f:
    line = f.readline().strip()
    kmers = line.split(',')
  
  return kmers

def reassemble_genome(kmers):
  assembler = DeBruijn(kmers)
  genome = assembler.get_possible_genome()

  with open('files/joseJunior.txt', 'w') as f:
    f.write(genome)


def main():
  while True:
    print("Choose an option:")
    print("1. Read a file with a full genome and generate kmers")
    print("2. Reassemble kmers and return a genome")
    print("0. Exit")
    
    choice = input("Enter your choice (0/1/2): ")
      
    if choice == '1':
      file_path = input("Enter the path to the file with genome: ")
      k = int(input("Enter the value of k: "))
      genome = read_genome_file(file_path)
      kmers = generate_k_mers(genome, k)
      export_k_mers(kmers, 'files/input.txt')
      print("\033[92mKmers generated and saved in 'files/input.txt'\033[0m")
    
    elif choice == '2':
      file_path = input("Enter the path to the file with kmers: (default: files/input.txt) ")

      if file_path == '':
        file_path = 'files/input.txt'

      kmers = read_kmers_file(file_path)
      genome = reassemble_genome(kmers)
      print("\033[92mGenome reassembled, check file 'files/joseJunior.txt' for the result.\033[0m")
    
    elif choice == '0':
      print("Exiting.")
      break
    
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()