from source.reads import Reads

from collections import defaultdict
import pickle

class KmerIndex():
  def __init__(self, reads: Reads = None, k: int = 10):
    self.counts = defaultdict(int)
    self.k = k

    if reads != None:
      #for r in reads.get_all():
      for r in reads.get_reads():
        for i in range(len(r) - k + 1):
          self.counts[r[i:i + k].lower()] += 1

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
    return self.counts[kmer.lower()]

  def set_internal_dict_and_k(self, counts, k):
    self.counts = counts
    self.k = k
  
