# -*- coding: utf-8 -*-
"""Usage:
  prize.py rands [--batch=100] [--count=10000]
  prize.py -h | --help | --version
"""
import random

import numpy as np
from docopt import docopt


def benchmark(count=10000, batch=100, rands=True):
    nums = str(random.randint(100, 999))
    total = []
    goods = []

    for b in xrange(int(batch)):

        prize = [0, 0, 0, 0]

        for _ in xrange(int(count)):
            nums = str(random.randint(100, 999)) if rands is True else nums
            rand = str(random.randint(100, 999))
            item = random.randint(10, 500)

            if rand == nums:
                prize[3] += 1
                price = item
            elif rand[0:2] in nums:
                prize[2] += 1
                price = item * 0.5
            elif rand[0:1] in nums:
                prize[1] += 1
                price = item * 0.1
            else:
                prize[0] += 1
                price = 0.00

            price = np.round(price, 2)
            income = np.round(item * 0.1 - price, 2)
            goods.append({'total': item, 'income': income, 'price': price})

        # print prize, (prize[1] / float(count)), (prize[2] / float(count)), (prize[3] / float(count))
        total.append(prize)

    return total, goods


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.1rc')
    count = args['--count']
    batch = args['--batch']
    rands = args['rands']
    # print args


def run(*args):
    batch = args[0]
    count = args[1]
    rands = args[2]
    total, goods = benchmark(batch=batch, count=count, rands=rands)

    a = 0
    b = 0
    c = 0

    aa = []
    bb = []
    cc = []

    for x in total:
        if x[1] > a:
            a = x[1]

        if x[2] > b:
            b = x[2]

        if x[3] > c:
            c = x[3]

        aa.append(x[1])
        bb.append(x[2])
        cc.append(x[3])

    # print a, b, c

    ap = np.array(aa)
    bp = np.array(bb)
    cp = np.array(cc)

    # print "10 min: %s, max: %s, ave: %s" % (str(ap.min()), str(ap.max()), str(ap.mean()))
    # print "50 min: %s, max: %s, ave: %s" % (str(bp.min()), str(bp.max()), str(bp.mean()))
    # print "100 min: %s, max: %s, ave: %s" % (str(cp.min()), str(cp.max()), str(cp.mean()))
    t = 0.00
    p = 0.00
    i = 0.00

    for x in goods:
        print x
        t += x['total']
        p += x['price']
        i += x['income']
        # print total
        # print cp.min(), cp.max(), cp.mean()

    print t, p, i, i - p
