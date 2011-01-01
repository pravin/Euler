#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 232792560

class p009:
    def run(self):
        for a in xrange(1, 998):
            for b in xrange(a, 999):
                for c in xrange(b, 1000):
                    if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                        print (a, b, c), a * b * c
                        return

if __name__ == '__main__':
    p = p009()
    p.run()
