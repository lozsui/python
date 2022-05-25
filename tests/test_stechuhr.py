"""
This code is work in progress...
"""

import pytest
import ppl.stechuhr
from datetime import date
from datetime import datetime
from datetime import timedelta

"""
How can I declare test_input as array that I can do

    for dt in test_input:
        su.add_timestamp(dt)

@pytest.mark.parametrize("test_input,expected", [
    [datetime(year=2021, day=27, month=4, hour=9, minute=0),
     datetime(year=2021, day=27, month=4, hour=10, minute=0), ],
    [date(year=2021, day=27, month=4), 1]])
"""


def test_hours_worked():
    su = ppl.stechuhr.Stechuhr()
    timestamps = [
        datetime(year=2021, day=27, month=4, hour=9, minute=0),
        datetime(year=2021, day=27, month=4, hour=12, minute=0),
        datetime(year=2021, day=27, month=4, hour=13, minute=0),
        datetime(year=2021, day=27, month=4, hour=16, minute=0),
    ]
    su.timestamps = timestamps
    hours_worked = su.hours_worked_at(date(year=2021, day=27, month=4))
    print()
    print(hours_worked)
    assert hours_worked == timedelta(hours=6)


def test_hours_worked_two():
    su = ppl.stechuhr.Stechuhr()
    tds = [
        timedelta(hours=10, minutes=31),
        timedelta(hours=8, minutes=51),
        timedelta(hours=6, minutes=3),
        timedelta(hours=8, minutes=40),
        timedelta(hours=7, minutes=00),
        timedelta(hours=8, minutes=56),
        timedelta(hours=5, minutes=00),
        timedelta(hours=7, minutes=44),
        timedelta(hours=7, minutes=30),
        timedelta(hours=6, minutes=39),
        timedelta(hours=9, minutes=14),
        timedelta(hours=7, minutes=50),
        timedelta(hours=8, minutes=55),
        timedelta(hours=6, minutes=49),
    ]
    su.timedeltas = tds
    actual_hours_worked = su.sum_timedeltas()
    expected_hours_worked = timedelta(hours=109, minutes=42)
    print()
    print("13 days à 8h 24': ", 13 * timedelta(hours=8, minutes=24))
    print("Actually Worked: ", actual_hours_worked)
    assert actual_hours_worked == expected_hours_worked

def test_hours_worked_july():
    su = ppl.stechuhr.Stechuhr()
    tds = [
        # Aktuelles Saldo
        #
        # Wochensoll: 25h 12'
        #
        # Für Oktober siehe Notiz in todos_et_al.org vom
        # 2. November.
        # KW 44
        # Dienstag
        timedelta(hours=7, minutes=17),
        # Mittwoch
        timedelta(hours=8, minutes=12),
        # Donnerstag
        timedelta(hours=8, minutes=3),
        # Freitag
        timedelta(hours=9, minutes=4),
        # KW 45
        # Dienstag
        timedelta(hours=0, minutes=0),
        # Mittwoch
        timedelta(hours=9, minutes=0),
        # Donnerstag
        timedelta(hours=8, minutes=24),
        # Freitag
        timedelta(hours=0, minutes=24),
    ]
    su.timedeltas = tds
    actual_hours_worked = su.sum_timedeltas()
    expected_hours_worked = 2 * timedelta(hours=25, minutes=12)
    print()
    print("x days à 8h 24': ", expected_hours_worked)
    print("Actually Worked: ", actual_hours_worked)
    print("Delta: ", actual_hours_worked - expected_hours_worked)
    assert actual_hours_worked == expected_hours_worked

