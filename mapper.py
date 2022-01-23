#!/usr/bin/env python
import sys
import string

#stopwords = set([stop_words.ENGLISH_STOP_WORDS])

stopwords = set(['the', 'and'])

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    line = line.translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
 	       print '%s\t%s' % (word, "1")
