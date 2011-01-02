#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 104743 

import math

class p007:
    def run(self):
        num = 2 ** 32
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        last_num = 21

        for n in xrange(last_num, num, 2):
            is_prime = True
            limit = math.ceil(math.sqrt(n))
            for p in primes:
                if p > limit:
                    break
                if n % p == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
                if len(primes) == 10001:
                    print n
                    break
        last_num = num

if __name__ == '__main__':
    p = p007()
    p.run()
