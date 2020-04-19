#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
In the United Kingdom the currency is made up of pound (£) and pence (p). 
There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

coins = (1, 2, 5, 10, 20, 50, 100, 200)
memo = {}

def count_ways(num, coins_arr):
    """ Counts the ways in which one can arrive at num using coins """
    if (num, coins_arr) in memo:
        return memo[(num, coins_arr)]
    if num == 0:
        return 1
    if len(coins_arr) == 0:
        return 0

    total = 0
    for i in range(len(coins_arr)):
        if num < coins_arr[i]:
            break
        total += count_ways(num - coins_arr[i], coins_arr[i:])

    memo[(num, coins_arr)] = total
    return total

print(count_ways(200, coins))
