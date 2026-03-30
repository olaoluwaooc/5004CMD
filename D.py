import pandas as pd
import matplotlib.pyplot as plt

# load the dataset
df = pd.read_csv('Trips_by_Distance.csv')

# sum of the total trips for each distance category
distance_totals = {
    '<1 mile': df['Number of Trips <1'].sum(),
    '1–3 miles': df['Number of Trips 1-3'].sum(),
    '3–5 miles': df['Number of Trips 3-5'].sum(),
    '5–10 miles': df['Number of Trips 5-10'].sum(),
    '10–25 miles': df['Number of Trips 10-25'].sum(),
    '25–50 miles': df['Number of Trips 25-50'].sum(),
    '50–100 miles': df['Number of Trips 50-100'].sum(),
    '100–250 miles': df['Number of Trips 100-250'].sum(),
    '250–500 miles': df['Number of Trips 250-500'].sum(),
    '500+ miles': df['Number of Trips >=500'].sum()
}


dist_df = pd.DataFrame(list(distance_totals.items()), columns=['Distance', 'Trips'])

# plot the graph
plt.figure()
plt.bar(dist_df['Distance'], dist_df['Trips'])

plt.xlabel('Distance Category')
plt.ylabel('Total Number of Trips')
plt.title('Total Travellers by Distance Category')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
