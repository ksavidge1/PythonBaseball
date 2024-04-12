import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

fangraphs_player_data = pd.read_csv(Path(r'C:\Data\baseball\fangraphs_batting_2023.csv'))

# matplotlib example
WAR_per_player = fangraphs_player_data['WAR']
wrcPlus_per_player = fangraphs_player_data['wRC+']
m, b = np.polyfit(WAR_per_player, wrcPlus_per_player, 1)
plt.scatter(WAR_per_player, wrcPlus_per_player)
plt.plot(WAR_per_player, m*WAR_per_player + b)
plt.show()

# seaborn example
sns.displot(data=fangraphs_player_data, x="Age", kde=True)
plt.show()

# try adding a col argument, but restrict the range of Age for simpler display
fangraphs_player_data_age_restricted = fangraphs_player_data[np.logical_and(fangraphs_player_data["Age"] >= 25,
                                                                            fangraphs_player_data["Age"] <= 29)]
sns.displot(data=fangraphs_player_data_age_restricted, x="WAR", col="Age", kde=True)
plt.show()

# Max of KDE distribution for each age (eyeballed from above plot)
x = np.arange(25, 30)
y = [3, 3.5, 2.5, 2, 5]

plt.scatter(x=x, y=y)
plt.show()
