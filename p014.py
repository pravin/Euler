#!/usr/bin/env python
# Pravin Paratey (http://pravin.insanitybegins.com)
#
# Answer: 837799

class p14:
    path_len = {1: 1}
    def next(self, n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1

    def run(self):
        max_count = 0
        answer = 0
        for n in xrange(1, 1000000):
            #print n
            num = n
            count = 1
            while True:
                num = self.next(num)
                #print num, len(self.path_len)
                if self.path_len.has_key(num):
                    count += self.path_len[num]
                    break
                else:
                    count += 1
            self.path_len[n] = count
            if count > max_count:
                answer = n
                max_count = count
        return (answer, max_count)

if __name__ == '__main__':
    p = p14()
    print p.run()
