#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
# 
#
# Answer: 

num, num_str = 1, ' '

while len(num_str) < 1000001: # 1 million
    num_str += str(num)
    num += 1

print reduce(lambda x, y: x * y, [int(num_str[x]) for x in (1, 10, 100, 1000, 10000, 100000, 1000000)])
