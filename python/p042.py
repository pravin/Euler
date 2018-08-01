#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 162

# Generate Triangle numbers
triangle_numbers = [n * (n + 1) / 2 for n in range(1, 45)] # Generating a certain length of triangle numbers

# Read the file
fp = open('../data/words.txt')
names = fp.read().split('","')
names[0] = names[0][1:] # Clean beginning of input
names[-1] = names[-1][:-1] # Clean end of input
fp.close()

print len([term for term in [sum([ord(x) - 64 for x in n]) for n in names] if term in triangle_numbers])
