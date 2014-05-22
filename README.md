DNA sequence/reads simulator
================================
Significant amount of reads are often needed in bioformatics for tool benchmark 
or tool test. Though the cost of sequencing has greatly reduced due to recent 
advancement in sequencing technology, it still costs several thousands of dollars 
per sequencer run, without mentioning the time cost, which usually is a few days, 
to generate real sequencing reads. Here the sequencers are including all current 
dominant NGS sequencers (Illumina, SOLiD and 454). That is expensive and it's a 
overkill for purpose like benchmarking tools. With the application of statistics 
and computer science, we can generate simulated reads, which have the same 
quality as real data. That's the motivation of this project -- generate simulated 
reads with features customizable through arguments.

For instance, to benchmark several SNP callers, you may need 1,000,000 high throughput 
sequencing reads, which should have a median length of 72 nt (or any median length you 
would expect from your 
sequencer) and the reads should possess 30% of A,T and 70% of C,G to reflect the 
actual AT and GC content in a your favorate specie (such as rice). That is what 
this program can do.

Features
=========
This program will generate any number of reads with the exact nucleotide frequency 
given by the user. Additionally, the length of the simulated reads is consistent with the input (training) data if given. 

Requirements
=============
  * Python version > 2.7                         
  * package: [numpy] (http://www.numpy.org/)     
  * package: [scipy] (http://www.scipy.org/)     
  * package: [pandas] (http://pandas.pydata.org/)


Example Usage
=============
To display help
```python
python readsSimulator.py -h
```
 Below command will generate 10000 reads to STDOUT. By default, the frequency of 'A' and 'T' is 0.32 and that 
 of 'C' and 'G' is 0.18. The mean and stdev of the length of all generated simulation reads will be exactly 
 the same as input file -- test.fa.
```python
python readsSimulator.py test.fa
```
Send Bugs/Commnents to
======================
Zhigang Wu (zhigang.wu@email.ucr.edu)



LICENSE
=========
Copyright (c) <2013>, <Zhigang Wu>
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, 
       this list of conditions and the following disclaimer.
    
    2. Redistributions in binary form must reproduce the above copyright 
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.

    3. Neither the name of Django nor the names of its contributors may be used
       to endorse or promote products derived from this software without
       specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

