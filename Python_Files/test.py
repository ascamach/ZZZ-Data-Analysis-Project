import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["team"] = df["teammate_1"] + "_" + df["teammate_2"]

plot = df.groupby("team").plot(title="Scores", x='run_number',y='damage_score',kind='line')

plt.show()