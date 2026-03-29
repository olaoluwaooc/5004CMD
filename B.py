import pandas as pd
import matplotlib.pyplot as plt

# load the dataset
df = pd.read_csv('Trips_by_Distance.csv')

# convert the ate column
df['Date'] = pd.to_datetime(df['Date'])

# filter conditions for >10,000,000 trips
trips_10_25 = df[df['Number of Trips 10-25'] > 10_000_000]
trips_50_100 = df[df['Number of Trips 50-100'] > 10_000_000]

# plot the Scatter plot
plt.figure()

plt.scatter(trips_10_25['Date'], trips_10_25['Number of Trips 10-25'], label='10-25 miles')
plt.scatter(trips_50_100['Date'], trips_50_100['Number of Trips 50-100'], label='50-100 miles')

# create the labels and title
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.title('Trips >10M: 10–25 miles vs 50–100 miles')
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
