#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# I have simply iterated over n^2 + a*n + b for a < |1000| and b < |1000|
#
# Answer: -59231

import math

class p27:
    last_num = 21
    primes = [2,3,5,7,11,13,17,19]

    def populate_primes(self, num):
        """ Returns all prime nums from 0 to num, including num """
        if self.last_num % 2 == 0:
            self.last_num -= 1

        if num > self.primes[-1]:
            limit = math.ceil(math.sqrt(num))
            for n in xrange(self.last_num, num+1, 2):
                is_prime = True
                for p in self.primes:
                    if n % p == 0 or p > limit:
                        is_prime = False
                        break
                if is_prime:
                    self.primes.append(n)
        self.last_num = num

    def find_primes(self, a, b):
        """ Returns number of primes found between a and b """
        n = 0
        while True:
            num = n ** 2 + a * n + b
            if num < 1: # Not considering negative numbers as prime
                return 0
            if num > self.last_num: # Do we need to generate more prime nums?
                self.populate_primes(num)
            #print n, num
            limit = math.ceil(math.sqrt(num))
            # Is this a prime num
            is_prime = True
            for p in self.primes:
                if p > limit:
                    break
                if num % p == 0:
                    is_prime = False
                    break
            if is_prime:
                if num not in self.primes and num > 1:
                    self.primes.append(num)
            else:
                break
            n += 1
        return n

if __name__ == '__main__':
    max_count = 0
    p = p27()
    
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            r = p.find_primes(a, b)
            if r > max_count:
                max_count = r
                print a, b, max_count, a * b#, len(p.primes), p.primes

    #print p.find_primes(-79, 1601)
