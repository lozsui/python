"""
No comment.
"""

import pytest
import ppl.stechuhr
from datetime import date
from datetime import time

@pytest.mark.parametrize("test_input,expected", [(date(year=2021, day=27, month=4), 8.4),])
def test_hours_worked(test_input, expected):
    # no working example yet
    su = ppl.stechuhr.Stechuhr()
    ts = ppl.stechuhr.TimeStamp(day=test_input, time_arg=time(hour=9, minute=0))
    su.add_timestamp(ts)
    su.hours_worked_at(test_input)
