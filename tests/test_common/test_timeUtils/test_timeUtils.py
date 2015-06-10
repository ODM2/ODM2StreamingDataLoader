from __future__ import print_function

from datetime import datetime, timedelta

from src.src.common.timeUtils import TimeUtils as tu


__author__ = 'Jacob'


class TestTimeUtils():
    def setup(self):
        self.tu = tu()

    def test_canirun(self):
        delta = timedelta(hours=24, minutes=20, seconds=12, milliseconds=5444)

        dates = [
            datetime(2014, 5, 27, 0, 7, 0),
            datetime(2014, 5, 27, 0, 15, 0),
            datetime(2014, 5, 27, 5, 17, 0),
            datetime(2014, 5, 27, 0, 20, 3),
            datetime(2014, 5, 28, 0, 23, 0),
            datetime(2014, 5, 26, 0, 28, 4),
            datetime(2014, 5, 17, 1, 30, 0),
            datetime(2014, 5, 7, 0, 35, 0),
            datetime(2014, 5, 27, 5, 40, 4),
            datetime(2014, 5, 27, 12, 45, 12),
            datetime.now()
        ]

        for x in dates:
            result = self.tu.canIRun(x, delta=delta)
            if not result:
                if not x == dates[-1]:
                    assert False
            #print("delta: %s -- %s result: %s" % (delta, x, result))
