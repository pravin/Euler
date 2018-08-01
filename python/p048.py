#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# There must be a better way of doing this apart from brute force. Waay to early in the morning to bother
#
# Answer: 9110846700

sum = 0
for x in xrange(1, 1001):
    sum += x ** x

print str(sum)[-10:]
