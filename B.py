import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(14,7))


# Load the dataset
df = pd.read_csv("Trips_by_Distance.csv", parse_dates=['Date'])
df.columns = df.columns.str.strip()

# Filter National 
national = df[df['Level'] == "National"]

# Get correct columns
col_10_25 = [c for c in national.columns if "10-25" in c][0]
col_50_100 = [c for c in national.columns if "50-100" in c][0]

# Filter the dates to >10M
high_10_25 = national[national[col_10_25] > 10000000]
high_50_100 = national[national[col_50_100] > 10000000]

# Sort
high_10_25 = high_10_25.sort_values("Date")
high_50_100 = high_50_100.sort_values("Date")

# Plot 
plt.scatter(high_10_25['Date'], high_10_25[col_10_25], label="10–25 Trips")
plt.scatter(high_50_100['Date'], high_50_100[col_50_100], label="50–100 Trips")

plt.title("Dates where >10M people travelled (10–25 vs 50–100 miles)")
plt.xlabel("Date")
plt.ylabel("Number of Trips")

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

