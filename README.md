DNA sequence/reads simulator
================================
Reads simulation is often needed in bioformatics for tool performance benchmark or tool test. It generally takes long time 
and a lot of money to get the real data. For instance, if you want to do benchmark of several 
short read aligners. To test them out, you will need 1,000,000 high throuput sequencing reads, which should 
have a median length of 40 nt and 30% of A,T and 70% of C,G. This program can generate simulated reads, which exactly follows 
given nucleotide composition and length distribution for you. 

Features
=========
This program will generate any number of reads, which uses exact nucleotide frequency given 
by the user. Additionally, the length of the simulated reads is consistent with the input (training)
data

Requirements
=============
  1. Python version > 2.7
  
  2. package: [numpy] (http://www.numpy.org/)

  3. package: [scipy] (http://www.scipy.org/)

  4. package: [pandas] (http://pandas.pydata.org/)


Example Usage
=============
To display help

    python readsSimulator.py -h

 Below command will generate 10000 reads to STDOUT. By default, the frequency of 'A' and 'T' is 0.32 and that 
 of 'C' and 'G' is 0.18. The mean and stdev of the length of all generated simulation reads will be exactly 
 the same as input file -- test.fa.

    python readsSimulator.py test.fa

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

