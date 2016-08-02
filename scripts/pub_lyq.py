#  -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'verdors'))

from .pub_base import *

CHANNEL = 'nzjh'


def main(channel, pages, cats, syncdb):
    pages = pages
    cats = cats
    iids = []

    for page in xrange(1, int(pages) + 1):
        req = requests.get(build_query(page, catIds='19250', channel=channel))
        rep = json.loads(req.content)
        ids = [str(x['auctionId']) for x in rep['data']['pageList']]
        ids = {}.fromkeys(ids).keys()
        ids = ",".join(ids)

        print ' -- page=%d' % page

        iids.append(convert(ids, cats))

        print iids


def run():
    main(channel=CHANNEL, pages=1, cats=105, syncdb=True)
