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

def test_kmer_index_file_loading():
  reads = Reads("test_reads.fa")
  kmer_index = KmerIndex(reads, 3)

  assert kmer_index.get_kmer_count("TcA") == 1

  kmer_index.to_file("test_kmer.p")
  loaded_kmer_index = KmerIndex.from_file("test_kmer.p")

  assert loaded_kmer_index.k == kmer_index.k

  assert loaded_kmer_index.get_kmer_count("TcA") == 1
  assert loaded_kmer_index.get_kmer_count("TGA") == 2 
  assert loaded_kmer_index.get_kmer_count("acg") == 3
  assert loaded_kmer_index.get_kmer_count("TgT") == 0 
  assert loaded_kmer_index.get_kmer_count("CAG") == 1 

