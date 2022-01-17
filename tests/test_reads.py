from source.reads import Reads

def test_num_reads():
  reads = Reads("test_reads.fa")
  reads_list = reads.get_all()
  assert len(reads_list) == 5
  assert reads_list[0] == "acgtcgt"
