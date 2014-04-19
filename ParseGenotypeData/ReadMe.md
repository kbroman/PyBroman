## ParseGenotypeData

Python version of the [long example perl script](http://www.biostat.wisc.edu/~kbroman/perlintro/index.html#ex2) in my
[Intro to perl](http://www.biostat.wisc.edu/~kbroman/perlintro/).

The goal is to take three files obtained from a collaborator (genotype
data, family info, and order of markers) and combine them into a
single file in the format used byt the CRI-MAP program.

- [`genotypes.txt`](genotypes.txt) &mdash; genotype data
- [`families.txt`](families.txt) &mdash; family information
- [`markers.txt`](markers.txt) &mdash; ordered markers
- [`data_save.gen`](data_save.gen) &mdash; desired output file
- [`convert.pl`](convert.pl) &mdash; original perl script
- [`convert.py`](convert.py) &mdash; python script

Also see the [Ruby version](https://github.com/kbroman/RubyBroman/blob/master/ParseGenotypeData/convert.rb).
