# Scripts for working with fasta files that provide functionality not included in BioPython

*	bioFunctions.py contains class definitions that can be used by other scripts.
*	assemblyUtils.py uses the class definitions to carry out user-defined operations.

## Install:

This package requires no installation procedures. Just type the name of the script (assemblyUtils.py) followed
by commands you want it to carry out.

However, for convenience, you may wish to consider the following:

To install system-wide, open a bash shell and type

	sudo ./setup.py

from within this directory.

If you don't have a password for this system, you can use the package by typing the full path to the script
assemblyUtils.py followed by arguments to it as mentioned above.

Alternatively, add the lines

	export PATH=$PATH:/path/to/PyUtils
	alias assemblyUtils="assemblyUtils.py"

to the file ~/.bashrc.

You can do this with the command

	echo "export PATH=$PATH:/path/to/PyUtils/ >> ~/.bashrc"
	echo "alias assemblyUtils='assemblyUtils.py' >> ~/.bashrc"

## Examples:

If installed systemwide or added to '~/.bashrc' following the previous instructions, the package will be accessible
from the command line using the command 'assemblyUtils'.
Alternatively, you can use the full path to assemblyUtils.py as the command (e.g. '/path/to/assemblyUtils.py').
In these examples, we consider the package to be installed system wide.

There are several commands that can be used with assemblyUtils. These include:

	-s/--split		-	Splits a fasta file into separate contigs based on positions of missing bases specified as 'N' or 'n'.
	-a/--assembly-stats	-	Creates a file containing assembly statistics for the fasta given, including L50, N50, size, longest contig.
	-l/--list		-	Creates a fasta file containing contigs that either match or don't match the provided list.
	-v			-	Used in the same way as the shell command 'grep -v' with '-l' or '--list' (above). If -l and -v are specified, the contigs in the provided list will not be printed to file.
	-o/--output		-	Prefix for all output files.

To run the following examples, stay in the PyUtils directory and type the commands.
To split a fasta file into contigs based on where 'N' or 'n' characters occur:

	assemblyUtils -f test/test.fasta -s -o test/test

This will create a file called 'test.splitContigs.fasta' in the 'test' directory.

To get assembly stats without splitting:

	assemblyUtils -f test/test.fasta -a -o test/test

This will create a file called 'test.txt' in the 'test' directory, which contains assembly stats for the given fasta file, 
without first splitting it into separate contigs based on 'N's or 'n's.

To get assembly stats with splitting:

	assemblyUtils -f test/test.fasta -s -a -o test/test

This will create two output files, 'test.splitContigs.fasta' and 'test.txt', in the 'test' directory.
The file 'test.txt' contains stats based on 'test.splitContigs.fasta'.

To filter a fasta file based on a list of sequences in a file:

	assemblyUtils -f test/test.fasta -l test/list.txt -o test/test

This will create a file called 'test.listMatch.fasta' in the 'test' directory. This is a fasta file containing only contigs that match the list.

To negatively filter a fasta file based on a list of sequences in a file:

	assemblyUtils -f test/test.fasta -l test/list.txt -v -o test/test

This will do the same as the previous example, except the fasta file will contain only sequences that do not match the list.

