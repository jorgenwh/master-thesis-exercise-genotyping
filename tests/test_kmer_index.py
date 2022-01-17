from source.reads import Reads
from source.kmer_index import KmerIndex

def test_kmer_index():
  reads = Reads("test_reads.fa") 
  kmer_index = KmerIndex(reads, 3)

  assert kmer_index.get_kmer_count("TcA") == 1
  assert kmer_index.get_kmer_count("TGA") == 2 
  assert kmer_index.get_kmer_count("acg") == 3
  assert kmer_index.get_kmer_count("TgT") == 0 
  assert kmer_index.get_kmer_count("CAG") == 1 
