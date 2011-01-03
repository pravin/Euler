#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 443839


five_digit = [x ** 5 + y ** 5 + z ** 5 + w ** 5 + v ** 5 + u ** 5\
              for x in range(10) for y in range(10) for z in range(10) for w in range(10) for v in range(10) for u in range(10)\
              if x * 100000 + y * 10000 + z * 1000 + w * 100 + v * 10 + u == x ** 5 + y ** 5 + z ** 5 + w ** 5 + v ** 5 + u ** 5]

print sum([x for x in five_digit if x != 0 and x != 1])
