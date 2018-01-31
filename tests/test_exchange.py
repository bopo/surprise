# encoding: utf-8
import datetime
import unittest

holiday = [
    u'2016-04-30',
    u'2016-05-01',
    u'2016-05-02',
    u'2016-06-09',
    u'2016-06-10',
    u'2016-06-11',
    u'2016-06-12',
    u'2016-09-15',
    u'2016-09-16',
    u'2016-09-17',
    u'2016-09-18',
    u'2016-10-01',
    u'2016-10-02',
    u'2016-10-03',
    u'2016-10-04',
    u'2016-10-05',
    u'2016-10-06',
    u'2016-10-07',
    u'2016-10-08',
    u'2016-10-09']


def get_exchange(today=None):
    total = 1

    # 周六日休市
    weeks = today.isoweekday()
    total = weeks - 5 if weeks > 5 else total
    total = weeks + 2 if weeks == 1 else total
    print 'weeks=>', weeks
    print 'total=>', total
    print 'today=>', today

    # 判断是否节假日
    while True:
        if not holiday:
            break

        forward = today + datetime.timedelta(days=-total)
        forward = forward.date()
        print 'forward=>', forward

        # 判断不是休市
        if str(forward) not in holiday:
            # 判断周末
            print '2total=>', total
            weeks = forward.isoweekday()
            total = weeks - 5 if weeks > 5 else total
            # total = weeks + 2 if weeks == 1 else total
            print '3total=>', total
            print 'weeks=>', weeks
            break

        total += 1
        print 'holiday=>', str(forward) in holiday

    print today + datetime.timedelta(days=-total)
    return today + datetime.timedelta(days=-total)


def has_exchange(today=None):
    # holiday = Holiday.objects.filter(year=now().year)
    today = datetime.datetime.now().date() if not today else today
    weeks = today.isoweekday()

    if holiday:
        if str(today) in holiday:
            return False

    # 周六日休市
    return False if weeks > 5 else True


def set_exchange(today=None):
    # instance = Prompt.objects.first()
    # switch__ = instance.switchs if instance else False

    # holiday = Holiday.objects.filter(year=now().year)

    total = 1

    # if switch__:
    #     total = Trade.objects.filter(owner=user, created__exact=now()).count()
    #     total = int(total) + 1

    # 周六日休市
    # weeks = today.isoweekday()
    # total += weeks - 5 if weeks > 5 else 0
    weeks = today.isoweekday()
    total = 8 - weeks if weeks >= 5 else total

    while True:
        if not holiday:
            break

        forward = today + datetime.timedelta(days=+total)
        print str(forward), '=>'

        # 判断非休市
        if str(forward) not in holiday:
            print str(forward)
            # 判断周末
            weeks = forward.isoweekday()
            total = 8 - weeks if weeks >= 5 else total
            break

        total += 1

    return today + datetime.timedelta(days=+total)


def checked(td):
    weeks = td.isoweekday()

    if weeks > 5:
        print "checked=>>", td, "weeks=>", weeks
        return False

    if str(td.date()) in holiday:
        print "checked=>>", td, "holiday"
        return False

    return True


class exchange_test(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        self.today = datetime.datetime.now()
        pass

    # 退出清理工作
    def tearDown(self):
        pass
        # 具体的测试用例，一定要以test开头

    def test_get_exchange(self):
        today = datetime.datetime.strptime("2016-01-01", "%Y-%m-%d")
        # today = today.date()

        for x in range(0, 365):
            self.assertTrue(checked(get_exchange(today=today + datetime.timedelta(days=+x))))


if __name__ == '__main__':
    unittest.main()
