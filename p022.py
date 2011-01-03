#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 871198282

fp = open('names.txt')
names = fp.read().strip().upper().split('","')
# Clean names
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
fp.close()

names.sort()

total = 0
for i in xrange(len(names)):
    total += (i + 1) * sum([ord(x) - 64 for x in names[i]])
print total
