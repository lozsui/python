from message import XyzTttScheduleMessage, TttTimeseries

def test_list_and_filer():
    ts1 = TttTimeseries(Id="ts1")
    message = XyzTttScheduleMessage(Id="msg1", TimeSeries=[ts1])
    no_starts_with_ts = len(list(filter(lambda x: x.Id.startswith("ts"), message.TimeSeries)))
    assert no_starts_with_ts

