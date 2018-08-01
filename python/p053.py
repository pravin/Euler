#!/usr/bin/env python
#
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 4075

factorial = [1]
for i in xrange(1, 101):
    factorial.append(factorial[i - 1] * i)

count = 0
for n in xrange(1, 101):
    for r in xrange(1, n):
        if factorial[n] / (factorial[n - r] * factorial[r]) > 1000000:
            count += 1

print count
