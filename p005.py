#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# I worked this out by hand. I listed the factors of the numbers from 1 to 20.
#
# Answer: 232792560

class p5:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def run(self):
        result = {}
        for num in range(1, 20):
            factors = {}
            for p in self.primes:
                while p <= num and num % p == 0:
                    num = num / p
                    if not factors.has_key(p):
                        factors[p] = 0
                    factors[p] += 1
            for k, v in factors.items():
                if not result.has_key(k):
                    result[k] = v
                else:
                    result[k] = max(result[k], v)
        print reduce(lambda x, y: x * y, map(lambda x, y: x ** y, result.keys(), result.values()))

if __name__ == '__main__':
    p = p5()
    p.run()
