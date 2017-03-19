#!/usr/bin/env python

import optparse
import re
import bioFunctions

parser	= optparse.OptionParser()

parser.add_option(	'-f',
			'--fasta',
			dest='fasta',
			metavar='FASTA',
			help='Fasta input file.'	)
parser.add_option(	'-s',
			'--splitOnNs',
			action='store_true',
			dest='split',
			default=False,
			help='Split fasta on strings of "N" or "n".'	)
parser.add_option(	'-l',
			'--list',
			dest='contiglist',
			metavar='CONTIG LIST',
			help="List of contigs to retrieve or omit (add option -v) from file."	)
parser.add_option(	'-v',
			action='store_true',
			dest='negative',
			default=False,
			help='Negative contig matching.'	)
parser.add_option(	'-a',
			'--assembly-stats',
			action='store_true',
			dest='stats',
			default=False,
			help='Print tab-delimited assembly stats file.'	)
parser.add_option(	'-o',
			'--output',
			dest='output',
			metavar='OUTPUT',
			default='output',
			help="Output file prefix."	)
			
(options, args) 	= parser.parse_args()

if not options.fasta:
	parser.error('Please specify fasta input.\n')

if not options.split and not options.stats and not options.contiglist:
	parser.error('Please specify action for fasta file.\n')

fastafile	= bioFunctions.FastaManipulator(options.fasta)

if options.split == True:
	fastafile.splitOnNs()
else:
	fastafile.noSplit()

if options.stats == True:
	fastafile.contigLengths()
	fastafile.contigN50()
	outfile	= open(options.output + '.txt', 'w')
	string	= "Assembly size:\t" + str(fastafile.total) \
		+ "\nContig N50:\t" + \
		fastafile.nf + \
		"\nContig L50:\t" \
		+ fastafile.lf + \
		"\nMax contig length:\t" \
		+ fastafile.max \
		+ "\nNumber of Contigs:\t" \
		+ str(len(fastafile.lengths))
	outfile.write(string)

if options.split == True:
	outfile	= open(options.output + 'splitContigs.fasta', 'w')
	for key, value in fastafile.contigs.iteritems():
		string	= key + "\n" + ''.join(fastafile.contigs[key])
		outfile.write(string)

outfile	= open(options.output + '.listMatch.fasta', 'w')
if options.contiglist:
	contiglist	= bioFunctions.ListCompare(options.contiglist)
	if options.negative == True:
		for key, value in fastafile.contigs.iteritems():
			if key not in contiglist.contiglist and key[1:] not in contiglist.contiglist:
				string	= key  + ''.join(fastafile.contigs[key])
				outfile.write(string)
	else:
		if options.negative == False:
			for key, value in fastafile.contigs.iteritems():	
				if key in contiglist.contiglist or key[1:] in contiglist.contiglist:
					string	= key  + ''.join(fastafile.contigs[key])
					outfile.write(string)

