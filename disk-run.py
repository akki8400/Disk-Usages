#!/usr/bin/python
#####################################################
# Usages pyhton disk-run.py Diretory-path           #
# This Script simply calls a shell script diskuse.sh#
# Show all stats in json format                     #
# file diskuse.sh should be in same directory       #
# By Akash Verma                                    #
#####################################################

import sys
import subprocess
import shlex
dir=sys.argv[1]
#subprocess.call(['sh', 'diskuse.sh', dir])
subprocess.call(shlex.split('sh diskuse.sh ' + dir))
