from typing import List

class Reads():
  def __init__(self, filename):
    self.filename = filename

  def get_all(self) -> List[str]:
    return [line.strip() for line in open(self.filename) if line[0] != ">"]

  def get_reads(self):
    f = open(self.filename)
    for line in f:
      if line[0] == ">":
        continue
      yield line.strip()
    f.close()
      
