#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 1366

class p016:
    def run(self):
        print sum([int(c) for c in str(2 ** 1000)])

if __name__ == '__main__':
    p = p016()
    p.run()
