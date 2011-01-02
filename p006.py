#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 25164150

class p006:
    def run(self):
        sum_of_squares = sum([x ** 2 for x in xrange(1, 101)])
        square_of_sum = sum(range(1, 101)) ** 2
        return square_of_sum - sum_of_squares

if __name__ == '__main__':
    p = p006()
    print p.run()
