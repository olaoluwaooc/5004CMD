import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Trips_by_Distance.csv')
df['Date'] = pd.to_datetime(df['Date'])

weekly_home = df.groupby('Week')['Population Staying at Home'].sum()

weekly_home.plot(kind='bar')
plt.xlabel('Week')
plt.ylabel('People Staying at Home')
plt.title('Weekly Population Staying at Home')

plt.show()
