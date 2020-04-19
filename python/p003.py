#!/usr/bin/env python
# Pravin Paratey (https://cto.me.uk)
#
# Question:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
#
# Answer: 6857

import math
from Prime import Prime

NUMBER = 600851475143
# Only need to generate numbers uptil \sqrt(NUMBER)
primes_list = Prime.generate_primes(int(math.sqrt(NUMBER)))
primes_list.reverse()
for p in primes_list:
    if NUMBER % p == 0:
        print p
        break
