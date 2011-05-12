#!/usr/bin/env python

import math

class Prime:
    @staticmethod
    def generate_primes(n):
        """ Uses the Sieve of Eratosthenes """
        # Create a candidate list within which non-primes will be
        # marked as None; only candidates below sqrt(n) need be checked. 
        candidates = range(n+1)
        fin = int(n**0.5)
     
        # Loop over the candidates, marking out each multiple.
        for i in xrange(2, fin+1):
            if candidates[i]:
                candidates[2*i::i] = [None] * (n//i - 1)
     
        # Filter out non-primes and return the list.
        return [i for i in candidates[2:] if i]
