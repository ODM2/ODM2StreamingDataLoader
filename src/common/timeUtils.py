from datetime import datetime

__author__ = 'Jacob'


class TimeUtils:
    def __init__(self):
        pass

    def canIRun(self, m_datetime, delta):
        """Checks if the last time it ran is outside of the timedelta permitted.
        If the elapsed time is greater than the delta cause the event to execute

        :param m_datetime:
            :type datetime:
        :param delta:
            :type datetime.timedelta:

        :return boolean:
        """

        if (datetime.now() - m_datetime) > delta:
            return True
        return False

    def dateconverter(self, m_datetime, offset):
        """Need to confirm that this is still needed...

        :param m_datetime:
        :param offset:
        :return:
        """

        pass

