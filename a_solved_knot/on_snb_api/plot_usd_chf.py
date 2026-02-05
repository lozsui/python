import requests
import pandas as pd
import matplotlib.pyplot as plt
import requests_cache

requests_cache.install_cache(
    cache_name="snb_cache",
    backend="sqlite",
    expire_after=24 * 60 * 60 # seconds (24 hours)
)

url = (
    "https://data.snb.ch/api/cube/devkum/data/json/en"
    "?dimSel=D0(M0),D1(USD1)"
    "&fromDate=2020-01"
    "&toDate=2025-12"
)

response = requests.get(url)
response.raise_for_status()
data = response.json()

# Extract date labels
dates = [
    v["date"] for v in
    data["timeseries"][0]["values"]
]

"""
Ziel wäre eigentlich einen Plot zu erstellen.
"""

# Dummy df

df = pd.DataFrame({
    "date": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "value": [10, 12, 9, 14, 15, 13, 16, 18, 17, 10]
})

# So würde man den Plat erstllen

plt.figure(figsize=(10, 5))
plt.plot(df["date"], df["value"])
plt.title("SNB devkum – USD (M0)")
plt.xlabel("Date")
plt.ylabel("Value")
plt.grid(True)
plt.tight_layout()
# plt.show()
plt.savefig("usd_chf.png", dpi=150)
