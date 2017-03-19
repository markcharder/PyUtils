#!/usr/bin/env python

import optparse
import re

class FastaManipulator(object):
	def __init__(self, object):
		self.file	= open(object, 'r')
		self.previous	= ""
		self.pline	= ""
		self.count	= 0
		self.contigs	= dict()
		self.lengths	= dict()
		self.total	= 0
		self.nf		= 0
	def noSplit(self):
		print "Reading in fasta."
		lines	= self.file.readlines()
		for line in lines:
			if re.match(">", line):
				self.contigs[line]	= []
				header			= line
			else:
				self.contigs[header].append(line)
	def splitOnNs(self):
		lines	= self.file.readlines()
		print "Reading in fasta."
		for line in lines:
			header	= re.compile(">")
			missing	= re.compile("N|n")
			if header.match(line):
				self.count += 1 
			else:
				if missing.match(line):
					if not missing.match(self.pline):
						self.count += 1
				else:
					if missing.search(line):
						bases	= list(line)
						self.previous=""
						for i in range(0, len(bases)):
							if missing.match(bases[i]):
								if not missing.match(self.previous):
									self.contigs[">contig_"+str(self.count)].append(str(bases[0:i-1]))
									self.count	+= 1
							self.previous	= bases[i]
					else:
						if  ">contig_"+str(self.count) in self.contigs:
							self.contigs[">contig_"+str(self.count)].append(line[:-1])
						else:
							self.contigs[">contig_"+str(self.count)]	= [line[:-1]]
			self.pline	= line[-2]
	def contigLengths(self):
		print "\nGetting contig lengths."
		for key, value in self.contigs.iteritems():
			self.lengths[key]	= len("".join(self.contigs[key]))
		self.lengths		= sorted(self.lengths.items(), key=lambda x: x[1])
	def contigN50(self):
		print "\nGetting N50."
		for i in range(0, len(self.lengths)):
			self.total	+= int(self.lengths[i][1])
		half	= int(self.total / 2)
		tracker	= 0
		count	= 0
		for i in reversed(range(0,len(self.lengths))):
			tracker += self.lengths[i][1]
			count 	+= 1
			if tracker >= half and self.nf == 0:
				self.nf	= str(self.lengths[i][1])
				self.lf	= str(count)
		self.max	= str(self.lengths[-1][1])

class ListCompare(object):
	def __init__(self, object):
		self.list	= open(object, 'r')
		self.contiglist	= self.list.readlines()

