from source.reads import Reads
from source.numpy_kmer_index import NumpyKmerIndex

def test_numpy_np_kmer_index():
  reads = Reads("test_reads.fa") 
  np_kmer_index = NumpyKmerIndex(reads, 3)

  assert np_kmer_index.get_kmer_count("TcA") == 1
  assert np_kmer_index.get_kmer_count("TGA") == 2 
  assert np_kmer_index.get_kmer_count("acg") == 3
  assert np_kmer_index.get_kmer_count("TgT") == 0 
  assert np_kmer_index.get_kmer_count("CAG") == 1 

def test_np_kmer_index_file_loading():
  reads = Reads("test_reads.fa")
  np_kmer_index = NumpyKmerIndex(reads, 3)

  assert np_kmer_index.get_kmer_count("TcA") == 1

  np_kmer_index.to_file("test_kmer.p")
  loaded_np_kmer_index = NumpyKmerIndex.from_file("test_kmer.p")

  assert loaded_np_kmer_index.k == np_kmer_index.k

  assert loaded_np_kmer_index.get_kmer_count("TcA") == 1
  assert loaded_np_kmer_index.get_kmer_count("TGA") == 2 
  assert loaded_np_kmer_index.get_kmer_count("acg") == 3
  assert loaded_np_kmer_index.get_kmer_count("TgT") == 0 
  assert loaded_np_kmer_index.get_kmer_count("CAG") == 1 

