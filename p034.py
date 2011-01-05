#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# The largest number to consider is 2,540,160 (9! * 7). 
# No number exceeding this value will satisfy the rules of the problem.  
# 
# Answer: 40730


# We don't need more than 9!
factorials = {'0': 1}
last = 1
for num in xrange(1, 10):
    last = last * num
    factorials[str(num)] = last

numbers = []
for num in xrange(11, 2540160):
    num_str = str(num)
    if sum([factorials[x] for x in num_str]) == num:
        numbers.append(num)

print sum(numbers)
