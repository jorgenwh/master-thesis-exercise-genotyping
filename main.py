from source.reads import Reads
from source.kmer_index import KmerIndex

def main():
  reads = Reads("reads.fa")
  reads_as_list = reads.get_all()
  print("There are %d reads in this file" % len(reads_as_list))

  ki = KmerIndex(reads, k=3)
  v = ki.get_kmer_count("act")
  print(v)

if __name__ == "__main__":
  main()
