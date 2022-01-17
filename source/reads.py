from typing import List

class Reads():
  def __init__(self, file_name):
    self.file_name = file_name

  def get_all(self) -> List[str]:
    return [line.strip() for line in open(self.file_name) if line[0] != ">"]

  def get_reads(self):
    f = open(self.file_name)
    for line in f:
      if line[0] == ">":
        continue
      yield line.strip()
    f.close()
      
