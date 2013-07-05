#!/usr/bin/env python2.7
import sys
import pdb
import argparse
import random 
from pandas import *
from scipy import stats
import re
import time

# readfq function is gitted from heng li's repository https://github.com/lh3/readfq/blob/master/readfq.py
def readfq(fp): # this is a generator function
  e.write("start parsing file ...\n")
  t = time.time()
  last = None # this is a buffer keeping the last unprocessed line
  while True: # mimic closure; is it a bad idea?
      if not last: # the first record or a record following a fastq
          for l in fp: # search for the start of the next record
              if l[0] in '>@': # fasta/q header line
                  last = l[:-1] # save this line
                  break
      if not last: break
      name, seqs, last = last[1:].partition(" ")[0], [], None
      for l in fp: # read the sequence
          if l[0] in '@+>':
              last = l[:-1]
              break
          seqs.append(l[:-1])
      if not last or last[0] != '+': # this is a fasta record
          yield name, ''.join(seqs), None # yield a fasta record
          if not last: break
      else: # this is a fastq record
          seq, leng, seqs = ''.join(seqs), 0, []
          for l in fp: # read the quality
              seqs.append(l[:-1])
              leng += len(l) - 1
              if leng >= len(seq): # have read enough quality
                  last = None
                  yield name, seq, ''.join(seqs); # yield a fastq record
                  break
          if last: # reach EOF before reading enough quality
              yield name, seq, None # yield a fasta record instead
              break
  e.write("parsing file done ... Cost: %fs\n" % (time.time() - t))

def getHandle(file):
  if hasattr(file, "read"):
    return file
  else:
    return open(file)

def lengthGenerator(file, number):
  n, slen, qlen = 0, 0, 0
  lengthArray = []
  for name, seq, qual in readfq(getHandle(file)):
    n += 1
    lengthArray.append(len(seq))
  aa = Series(lengthArray)
  ee = DataFrame(aa.value_counts())
  ee.columns = ["counts"] 
  ee['percentage'] = aa.value_counts()/float(sum(aa.value_counts()))
  ee = np.around(ee, decimals=2)
  e.write("Here is length DataFrame\n")
  e.write(ee.to_string())

  custm = stats.rv_discrete(name="custm", values=(ee.index.tolist(), ee.ix[:, 'percentage']))
  return custm.rvs(size=number)

def read_generator(A=None, C=None, G=None, T= None, length=None):
  custm = stats.rv_discrete(name="custm", values=([0, 1, 2, 3], [A, C, G, T]))
  random_string = "".join(map(str, custm.rvs(size=length)))
  for i, c in enumerate(['A', 'C', 'G', 'T']): # trick is not going to work
    random_string = re.sub(str(i), c, random_string)
  return random_string

def reads_generator(args):
  seqid = 0
  for length in lengthGenerator(args.file, args.num):
    seqid += 1
    o.write(">%d\n%s\n" % (seqid, read_generator(args.A, args.C, args.G, args.T, length)))



if __name__ == '__main__':
  o = sys.stdout
  e = sys.stderr
  parser= argparse.ArgumentParser(
      description="Given frequency of each nucleotide (A, T, C, G), " +
      "generate specific number (customizable via --num) of simulatation DNA reads. " +
      " The length distribution of the simulated reads "
      + "will be consistent with that of the specified (training) input file. " +
      "By default frequency for each nucleotide is set to that of model plant -- Arabidopsis.")
  parser.add_argument("--A", help="frequency of A [.32]", 
      default = 0.32, type=float)
  parser.add_argument("--C", help="frequency of C [.18]", 
      default = 0.18, type=float)
  parser.add_argument("--G", help="frequency of G [.18]", 
      default = 0.18, type=float)
  parser.add_argument("--T", help="frequency of T [.32]", 
      default = 0.32, type=float)
  parser.add_argument('file', help="the reads file, from which we get the length distribution, " +
      "which will be used in our simulation")
  parser.add_argument('--num', default = 10000, type=int, help="number of simulation reads you " +
      "want to generate")
  args = parser.parse_args()
  reads_generator(args)


