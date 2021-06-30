# -*- coding: utf-8 -*-

"""
An employee reports to the Stechuhr when he enters or leaves the government building. With this data
the Stechuhr calculates how long the employee worked on a specific day.

Do not use this code as an implementation for the above mentioned, :-(. It is work in progress.
"""

from datetime import time
from datetime import date
from datetime import datetime
from datetime import timedelta


class TimeStamp:

    def __init__(self, day=None, time_arg=None):
        self.day = day
        self.time = time_arg

    def __str__(self):
        return str(self.day) + " " + str(self.time)


class Stechuhr():

    def __init__(self):
        self.timestamps = []
        self.timedeltas = []

    def hours_worked_at(self, d):
        previous_ts = None
        td = timedelta(seconds=0)
        for ts in self.timestamps:
            if date(year=ts.year, month=ts.month, day=ts.day) == d:
                if previous_ts is None:
                    previous_ts = ts
                else:
                    td += ts - previous_ts
                    previous_ts = None
        return td

    def sum_timedeltas(self):
        td_sum = timedelta(seconds=0)
        for td in self.timedeltas:
            td_sum += td
        return td_sum
