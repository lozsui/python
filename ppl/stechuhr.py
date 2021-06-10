# -*- coding: utf-8 -*-

"""
An employee reports to the Stechuhr when he enters or leaves the government building. With this data
the Stechuhr calculates how long the employee worked on a specific day.
"""

from datetime import time

class TimeStamp():

    def __init__(self, day=None, time_arg=None):
        self.day = day
        self.time = time_arg

    def __str__(self):
        return str(self.day) + " " + str(self.time)


class Stechuhr():

    def __init__(self):
        self.timestamps = []

    def add_timestamp(self, timestamp):
        self.timestamps.append(timestamp)

    def hours_worked_at(self, date):
        time_worked = time(hour=0, minute=0)
        for ts in self.timestamps:
            if ts.day == date:
                time_worked += ts.time
