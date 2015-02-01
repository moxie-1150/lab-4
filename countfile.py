__author__ = 'eric'

""" countfile.py:

    Reads the name of a text file (same folder as this code),
    then computes and prints number of characters, words, and
    lines in the file.

"""

filename = input ("Enter name of file to analyze: ")

infile = open (filename,"r")

linecount=0
charcount=0
wordcount=0
for eachline in infile: # here's a new kind of for statement!

    if '\n' in eachline: # and an example of an if-statement - more later
        linecount += 1

    charcount += len(eachline)
    linewords = eachline.split()
    wordcount += len(linewords)

print ("number of lines: ",linecount)
print ("number of words: ",wordcount)
print ("number of chars: ",charcount)

infile.close()