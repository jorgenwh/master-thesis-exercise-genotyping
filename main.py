from source.reads import Reads
from source.kmer_index import KmerIndex, hash_kmer

import time

def main():
  print(hash_kmer("atg"))
  return
  reads = Reads("reads.fa")
  reads_as_list = reads.get_all()
  print("There are %d reads in this file" % len(reads_as_list))

  t1 = time.time_ns()
  ki = KmerIndex(reads, k=3)
  t2 = time.time_ns()
  elapsed = t2 - t1
  print("Elapsed time to create index normally:", elapsed)

  ki.to_file("out_pickle.p")

  t1 = time.time_ns()
  loaded_ki = KmerIndex.from_file("out_pickle.p")
  t2 = time.time_ns()
  elapsed = t2 - t1
  print("Elapsed time to create index from file:", elapsed)

  print(ki.get_kmer_count("act"))
  print(loaded_ki.get_kmer_count("act"))

if __name__ == "__main__":
  main()
