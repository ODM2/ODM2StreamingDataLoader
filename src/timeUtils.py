from datetime import datetime

__author__ = 'Jacob'


class TimeUtils:
    def __init__(self):
        pass

    def canIRun(self, m_datetime, delta):
        """

        :param m_datetime:
        :param delta:
        :return boolean:
        """

        if (datetime.now() - m_datetime) > delta:
            return True
        return False

