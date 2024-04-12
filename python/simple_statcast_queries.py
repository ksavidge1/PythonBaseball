import pybaseball as pyb
from pathlib import Path


# This gets pitch-level data, not aggregated by player. Returns 8000 rows for 2 days
statcast_data = pyb.statcast("2023-04-01", "2023-04-02")
print(statcast_data.head())

statcast_data.to_csv(Path(r"C:\Data\baseball\statcast_2023_04_01.csv"))




