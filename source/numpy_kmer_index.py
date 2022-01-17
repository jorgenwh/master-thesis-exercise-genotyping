from source.reads import Reads

import numpy as np
import pickle

base_values = {"a": 0, "c": 1, "t": 2, "g": 3}

def hash_kmer(kmer: str) -> int:
  value = 0
  k = len(kmer)
  for i, b in enumerate(kmer):
    value += base_values[b] * 4 ** (k - i - 1)
  return value

class NumpyKmerIndex():
  def __init__(self, reads: Reads = None, k: int = 10):
    self.counts = np.zeros(4 ** k) 
    self.k = k

    if reads != None:
      #for r in reads.get_all():
      for r in reads.get_reads():
        for i in range(len(r) - k + 1):
          kmer = r[i:i + k]
          hash = hash_kmer(kmer.lower())
          self.counts[hash] += 1

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
    return self.counts[hash_kmer(kmer.lower())]

  def set_internal_dict_and_k(self, counts, k):
    self.counts = counts
    self.k = k

