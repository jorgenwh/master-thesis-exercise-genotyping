import numpy as np
import time
import random

base_values = {"a": 0, "c": 1, "t": 2, "g": 3}

def hash(kmer):
  value = 0
  k = len(kmer)
  for i, b in enumerate(kmer):
    value += base_values[b] * 4 ** (k - i - 1)
  return value

def np_hash(kmer):
  k = len(kmer)
  kmer_arr = np.array(list(kmer.lower()))

  numeric_arr = np.zeros_like(kmer_arr, dtype=np.int64)
  numeric_arr[np.where(kmer_arr == "a")] = 0
  numeric_arr[np.where(kmer_arr == "c")] = 1 
  numeric_arr[np.where(kmer_arr == "t")] = 2 
  numeric_arr[np.where(kmer_arr == "g")] = 3 

  power_arr = np.power(4, np.arange(0, k))
  h = np.convolve(numeric_arr, power_arr, mode="valid")
  return h

def main():
  kmer_short = "atg"
  kmer_long = ""
  for _ in range(15):
    kmer_long += random.choice(["a", "c", "t", "g"])

  print("SHORT KMER")
  t1 = time.time_ns()
  h = hash(kmer_short)
  t2 = time.time_ns()
  elapsed = t2 - t1
  print(f"Elapsed ns for hash: {elapsed}")

  t1 = time.time_ns()
  np_h = np_hash(kmer_short)
  t2 = time.time_ns()
  elapsed = t2 - t1
  print(f"Elapsed ns for np_hash: {elapsed}")
  assert h == np_h, "hash and np_hash hashed same kmer to different values"

  print("\nLONG KMER")
  t1 = time.time_ns()
  h = hash(kmer_long)
  t2 = time.time_ns()
  elapsed = t2 - t1
  print(f"Elapsed ns for hash: {elapsed}")

  t1 = time.time_ns()
  np_h = np_hash(kmer_long)
  t2 = time.time_ns()
  elapsed = t2 - t1
  print(f"Elapsed ns for np_hash: {elapsed}")
  assert h == np_h, f"hash and np_hash hashed same kmer to different values.\n{h} != {np_h}"

if __name__ == "__main__":
  main()
