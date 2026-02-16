
class TttTimeseries:
    def __init__(
        self,
        Id: str = "",
    ):
        self.Id = Id


class XyzTttScheduleMessage:
    def __init__(
        self,
        Id: str,
        TimeSeries: list[TttTimeseries] = [],
    ):
        self.Id = Id
        self.TimeSeries = TimeSeries
        