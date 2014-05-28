from __future__ import print_function

from datetime import datetime, timedelta

from src.timeUtils import TimeUtils as tu


__author__ = 'Jacob'


class TestTimeUtils():
    def setup(self):
        self.tu = tu()

    def test_canirun(self):

        delta = timedelta(minutes=15)
        value = datetime(2014, 5, 27, 0, 0, 0),

        dates = [
            datetime(2014, 5, 27, 0, 7, 0),
            datetime(2014, 5, 27, 0, 15, 0),
            datetime(2014, 5, 27, 0, 17, 0),
            datetime(2014, 5, 27, 0, 20, 0),
            datetime(2014, 5, 27, 0, 23, 0),
            datetime(2014, 5, 27, 0, 28, 0),
            datetime(2014, 5, 27, 0, 30, 0),
            datetime(2014, 5, 27, 0, 35, 0),
            datetime(2014, 5, 27, 0, 40, 0),
            datetime(2014, 5, 27, 0, 45, 0),
        ]

        self.tu.canIRun()
        pass