#!/usr/bin/env python

import os
import sys
import subprocess

error = 0
path=os.path.dirname(__file__)
path=os.path.abspath(path)
try:
	command	= subprocess.check_call("ln -s " + path + "/assemblyUtils.py /usr/local/bin/assemblyUtils", shell=True)
except Exception:
	if os.path.exists("/usr/local/bin/assemblyUtils"):
		print "Already installed system wide."
	else:
		print "Try sudo ./setup.py to install system wide. Otherwise \"echo 'export PATH=$PATH:/path/to/PyUtils' >> ~/.bashrc\"."
	error	= 1
if error == 0:
	print "Success. assemblyUtils.py in current directory " + path + " symlinked to system bin directory."
