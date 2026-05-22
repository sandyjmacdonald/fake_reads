> [!IMPORTANT]
> **This repository has moved to Codeberg.**
>
> Active development now happens at **[https://codeberg.org/sandyjmacdonald/fake_reads](https://codeberg.org/sandyjmacdonald/fake_reads)**.
>
> This GitHub copy is archived and read-only. Please file issues, open pull requests, and follow the project on Codeberg.

---

fake_reads.py
==========

Creates a .fasta formatted file of nonsense reads with a specified number of reads and 
mean read length. Read lengths are randomly sampled from a normal distribution with a 
standard deviation of a fifth of the mean read length. The output is a file named
fakereads.fasta containing your fake reads.

### Dependencies

Requires [Numpy](http://www.numpy.org) to sample from a normal distribution.

### Usage

    python fake_reads.py -n <numberofreads> -l <meanlength>

> ##### Arguments

> `-n` The number of reads that you want in your fasta file.

> `-l` The mean read length that you want.

> `-h` Displays help.
