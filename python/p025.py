#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 4782

last_one, last_two = 2, 1
term, num = 3, 2
while len(str(num)) != 1000:
    num = last_one + last_two
    last_two, last_one = last_one, num
    term += 1
print term
