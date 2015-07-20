#!/usr/bin/env python

# Creates a .fasta/q formatted file of nonsense reads with a specified
# number of reads and mean read length. Read lengths are randomly
# sampled from a normal distribution with a standard deviation of
# a fifth of the mean read length.

import getopt, sys
import random
import numpy as np

# Generator function to split a list or string up into chunks of a
# specified size.

def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

# This function creates the reads file with a specified mean read length
# and number of reads.

def write_reads(num_reads, mean_len, file_type):
    if file_type == 'fasta':
	       out = open('fakereads.fasta','w')
    elif file_type == 'fastq':
	       out = open('fakereads.fastq','w')
    bases = ['A','G','T','C']
    num_reads = num_reads
    mean_len = mean_len
    sd = mean_len/5  # The standard deviation is set to 1/5 of the mean read length.
    lengths = np.random.normal(mean_len, sd, num_reads)  # Randomly samples given number of reads from normal distribution.
    n = 1  # Keeps track of the read number.
    for l in lengths:
        seq = ''.join([random.choice(bases) for i in range(int(l))])
        if len(seq) == 0:
            seq = random.choice(bases)
        if file_type == 'fasta':
            out.write('>read_%i\n' % n)  # Write the header line for the sequence.
            for c in chunks(seq, 80):  # Splits the sequence up into lines of length 80, as per .fasta format.
                out.write(c + '\n')
        elif file_type == 'fastq':
            out.write('@read_%i\n' % n)  # Write the header line for the sequence.
            out.write(seq + '\n')
            out.write('+\n')
            out.write('5' * len(seq) + '\n')
        n += 1  # Increments read number.
    out.close()

# Tells you how to use the darned thing.

def usage():
	print """
\nfake_reads.py.\n
Creates a .fasta/q formatted file of nonsense reads with a specified
number of reads and mean read length. Read lengths are randomly
sampled from a normal distribution with a standard deviation of
a fifth of the mean read length.\n
Basic usage:
\tpython fake_reads.py -n <numberofreads> -l <meanlength> -t <fasta/fastq>\n
Arguments:
\t-h, --help\t\t\tPrint this information.
\t-n, --number <numberofreads>\t\tInteger value.
\t-l, --length <meanlength>\t\tInteger value.
\t-t, --type <fasta/fastq>\t\tFile type."""

# Runs the main program, and parses all of the command line arguments.

def main():
    try:  ## Parses the command line arguments.
        opts, args = getopt.getopt(sys.argv[1:], 'n:l:t:h', ['number=', 'length=', 'type=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

	## Creates variables from the arguments.

    for opt, arg in opts:
        if opt in ('-n', '--number'):
            num_reads = int(arg)
        elif opt in ('-l', '--length'):
            mean_len = int(arg)
        elif opt in ('-t', '--type'):
            file_type = str(arg)
        elif opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        else:
            usage()
            sys.exit(2)

    try:  ## Tries to make a fake reads file.
        write_reads(num_reads, mean_len, file_type)
    except KeyboardInterrupt:
        sys.exit(1)
    except:  ## Otherwise, shows usage.
        usage()
        sys.exit(1)

if __name__ == '__main__':
    main()
