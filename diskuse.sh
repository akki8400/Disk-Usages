#!/bin/bash
#############################################################
# This scripts is to see the file size of each file in bytes#
# in a particular directory, Directory path is beeing passed#
# argument from disk-run.py pyhtin file.		    #
# By Akash Verma					    #
#############################################################
 
DIR=$1

du -sb $DIR/* | awk ' BEGIN {print "{\n \"files\": \n [";} {print "  {\""$2"\","$1"},";} END {print " ],\n}";}'


