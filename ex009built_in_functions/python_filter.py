from dataclasses import dataclass


# Step 1: Mock the SreAggregationTimeseries class
@dataclass
class SreAggregationTimeseries:
    SendersTimeSeriesIdentification: str


# Step 2: Define example inputs
aggr_bids = {"BID001", "BID002"}
interval = type("Interval", (), {"value": 1})  # Change to -1 to test negative case


# Step 3: Define the matching function
def match_schedule(timeseries: SreAggregationTimeseries) -> bool:
    timeseries_bid_id = timeseries.SendersTimeSeriesIdentification.split("_")[0]
    if timeseries_bid_id not in aggr_bids:
        return False

    if interval.value > 0 and "pos" in timeseries.SendersTimeSeriesIdentification:
        return True
    if interval.value < 0 and "neg" in timeseries.SendersTimeSeriesIdentification:
        return True
    return False


# Step 4: Create a mock list of timeseries
schedule_timeseries = [
    SreAggregationTimeseries("BID001_pos"),
    SreAggregationTimeseries("BID001_neg"),
    SreAggregationTimeseries("BID003_pos"),
    SreAggregationTimeseries("BID002_pos"),
    SreAggregationTimeseries("BID002_neg"),
]

# Step 5: Apply the filter and convert to a list
aggr_timeseries = list(filter(match_schedule, schedule_timeseries))

# Step 6: Print the results
print("Matched Time Series:")
for ts in aggr_timeseries:
    print(ts.SendersTimeSeriesIdentification)
    print(ts.SendersTimeSeriesIdentification)

# learn about class filter
filtered = filter(match_schedule, schedule_timeseries)
for f in filtered:
    print(f)
