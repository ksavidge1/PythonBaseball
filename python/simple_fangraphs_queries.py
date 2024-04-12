import pybaseball as pyb
from pathlib import Path

fg_data = pyb.batting_stats(2023)
print(f'Number rows in df = {len(fg_data.index)}')

# fg_data.to_csv(Path(r"C:\Data\baseball\fangraphs_batting_2023.csv"))




