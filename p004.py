#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 906609

max = 0
for x in xrange(100, 1000):
    for y in xrange(100, 1000):
        num = x * y
        num_str = str(num)
        if num_str == num_str[::-1] and num > max:
            max = num
print max
