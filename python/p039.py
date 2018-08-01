#!/usr/bin/env python
#
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 840

max, answer = 0, 0
for p in xrange(120, 1001):
    num_of_solutions = 0
    half = p / 2 # Used to optimize
    for ab in xrange(half + 1, p):
        ab_4, ab_2 = ab / 4, ab / 2
        for a in xrange(ab_4, ab_2):
            b, c = ab - a, p - ab
            if c < b: continue
            if c ** 2 == a ** 2 + b ** 2:
                num_of_solutions += 1
    if num_of_solutions > max:
        max = num_of_solutions
        answer = p

print answer, max
