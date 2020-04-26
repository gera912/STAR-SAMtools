#!/usr/bin/env python

# Program Header
# Course: Bi621
# Name:   Gerardo Perez
# Description: Python script that that counts up the number
#of reads that are properly mapped to the reference genome and
#the number of reads that are not mapped to the genome.
#
# ps8: Part 2 – Python and SAM
#
# Development Environment: Atom 1.38.2
# Version: Python 3.7.3
# Date:  06/19/2019
#################################################

# Imports modules
import re
import argparse

# Creates an arguement passer
parser = argparse.ArgumentParser(description="Program parses the contents of your BAM file. \
count up the number of reads that are properly mapped to the reference genome and the number \
of reads that are not mapped to the genome")

# Adds arguemets by calling the arguement passer
parser.add_argument("-f", "--filename", help="specify the filename", required=True)


# Parses arguemets through using the parse args method.
args = parser.parse_args()

# Creates a variable
mapped=0
unmapped=0

#Opens a text file to read. stores the file as a variable.
with open(args.filename, 'r') as fh:

    # A for loop that goes through each line in the file.
    for line in fh:

        # If statement that uses regex to find the first the line with a specific first charcter.
        if re.match(r'^K', line):

            # splits the line into an array everytime it encounters a tab.
            parts = line.split('\t')

            # converts the index one in the array  into to an int and stores it as a variable.
            flags=int(parts[1])

            # if statement that checks if check the current read is mapped and counts for mapped and unmapped.
            if ((flags & 4)!=4):
                if((flags & 256) != 256):
                    mapped=mapped+1
            else: unmapped=unmapped+1

# opens a text file to read and stores the text file as a variable.
f1 = open("mapped_vs_unmapped.tsv", "w")

# writes the formatted output to the tsv file
f1.write("mapped:{0}\tunmapped:{1}\n".format(mapped,unmapped))

# Prints a statement in a specific format.
print("mapped:", mapped)
print("unmapped:", unmapped)
