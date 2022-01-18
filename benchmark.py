from source.reads import Reads
from source.kmer_index import KmerIndex
from source.numpy_kmer_index import NumpyKmerIndex

import time

def benchmark():
  reads = Reads("reads.fa")
  k = 3

  # Normal dict KmerIndex
  kmer_index = KmerIndex(reads, k)

  # Numpy KmerIndex
  np_kmer_index = NumpyKmerIndex(reads, k)

  n = 0
  for r in reads.get_reads():
    for i in range(len(r) - k + 1):
      counts_dict = kmer_index.get_kmer_count(r[i:i + k])
      counts_np = np_kmer_index.get_kmer_count(r[i:i + k])
      assert counts_dict == counts_np

    n += 1
    if n == 1000:
      break

  elapsed_dict = kmer_index.get_elapsed_lookup_time()
  elapsed_np_lookup, elapsed_np_hashing = np_kmer_index.get_elapsed_lookup_time()

  print(f"total lookup time dict_index: \33[1m{elapsed_dict / 1e6} sec\33[0m")
  print(f"total lookup time numpy_index: \33[1m{(elapsed_np_lookup + elapsed_np_hashing) / 1e6} sec\33[0m - ({elapsed_np_lookup / 1e6} sec lookup, {elapsed_np_hashing / 1e6} sec hashing)")


if __name__ == "__main__":
  benchmark()

