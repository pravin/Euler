#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 4613732

last_one, last_two = 2, 1
sum, num = 2, 3
while num < 4000000: # 4 million
    num = last_one + last_two
    if num % 2 == 0:
        sum += num
    last_two, last_one = last_one, num
print sum
