#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# The number, 197, is called a circular prime because all rotations of 
# the digits: 197, 971, and 719, are themselves prime. There are 
# thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 
# 73, 79, and 97. How many circular primes are there below one million?
#
# Answer: 55

from Prime import Prime

# Generate prime numbers under 1 million
primes_list = Prime.generate_primes(1000000)
primes_dict = {}
for p in primes_list:
    primes_dict[p] = None

# Just brute force 
# 13 primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97
count = 13 
for p in primes_list:
    if p < 100: 
        continue
    is_circular = True

    str_p = str(p)
    for i in xrange(len(str_p)):
        int_p = int(str_p)
        if not primes_dict.has_key(int_p):
            is_circular = False
            break
        str_p = str_p[-1] + str_p[:-1] 
    if is_circular:
        count += 1

print count
