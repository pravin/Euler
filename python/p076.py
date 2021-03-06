#!/usr/bin/env python
"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

from p031 import CountWays

if __name__ == '__main__':
    coins = tuple(range(1, 100))
    print(coins)

    c = CountWays()
    print(c.count_ways(100, coins))
