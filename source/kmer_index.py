from collections import defaultdict

from source.reads import Reads

class KmerIndex():
  def __init__(self, reads: Reads, k: int = 10):
    self.counts = defaultdict(int)
    self.k = k

    #for r in reads.get_all():
    for r in reads.get_reads():
      for i in range(len(r) - k + 1):
        self.counts[r[i:i + k].lower()] += 1

  def get_kmer_count(self, kmer: str) -> int:
    assert len(kmer) == self.k, f"Kmer of length {len(kmer)} provided to KmerIndex configured for k={self.k}"
    return self.counts[kmer.lower()]
