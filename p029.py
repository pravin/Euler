#!/usr/bin/env python
#
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 9183


terms = []
for a in xrange(2, 101):
    for b in xrange(2, 101):
        terms.append(a ** b)

print len(set(terms))
