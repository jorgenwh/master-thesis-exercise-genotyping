from source.reads import Reads

import numpy as np
import pickle
import time

base_values = {"a": 0, "c": 1, "t": 2, "g": 3}

def hash_kmer(kmer: str) -> int:
  value = 0
  k = len(kmer)
  for i, b in enumerate(kmer):
    value += base_values[b] * 4 ** (k - i - 1)
  return value

def np_hash_kmer(kmer: str):
  k = len(kmer)
  power_arr = np.array([4 ** (k - i - 1) for i in range(k)])
  kmer_arr = np.array([b for b in kmer])
  kmer_arr[np.where(kmer_arr == "a")] = 0
  kmer_arr[np.where(kmer_arr == "c")] = 1 
  kmer_arr[np.where(kmer_arr == "t")] = 2 
  kmer_arr[np.where(kmer_arr == "g")] = 3 
  numeric_arr = kmer_arr.astype(np.uint64)
  return int(np.convolve(numeric_arr, power_arr, mode="valid")[0])

class NumpyKmerIndex():
  def __init__(self, reads: Reads = None, k: int = 10):
    self.counts = np.zeros(4 ** k) 
    self.k = k

    if reads != None:
      #for r in reads.get_all():
      for r in reads.get_reads():
        for i in range(len(r) - k + 1):
          kmer = r[i:i + k]
          hash = np_hash_kmer(kmer.lower())
          self.counts[hash] += 1

    self.lookup_elapsed_ns_lookup = 0
    self.lookup_elapsed_ns_hash = 0

  @classmethod
  def from_file(cls, file_name: str):
    counts, k = pickle.load(open(file_name, "rb"))
    object = cls()
    object.set_internal_dict_and_k(counts, k)
    return object

  def to_file(self, file_name: str):
    pickle.dump((self.counts, self.k), open(file_name, "wb"))

  def get_kmer_count(self, kmer: str) -> int:
    assert len(kmer) == self.k, f"Kmer of length {len(kmer)} provided to KmerIndex configured for k={self.k}"
    t1 = time.time_ns()
    hash = np_hash_kmer(kmer.lower())
    t2 = time.time_ns()
    self.lookup_elapsed_ns_hash += t2 - t1

    t1 = time.time_ns()
    count = self.counts[hash]
    t2 = time.time_ns()
    self.lookup_elapsed_ns_lookup += t2 - t1

    return count 

  def set_internal_dict_and_k(self, counts, k):
    self.counts = counts
    self.k = k

  def get_elapsed_lookup_time(self):
    return self.lookup_elapsed_ns_lookup, self.lookup_elapsed_ns_hash


