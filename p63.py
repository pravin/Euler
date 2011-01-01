#!/usr/bin/env python

count = 0
for i in xrange(1, 1000):
    for j in xrange(1, i):
        print i, j
        num = i ** j
        length = len(str(num))
        if length == j:
            count += 1
            print num, i, j
        elif length > i:
            break

print count
