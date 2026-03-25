import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rcParams["figure.figsize"] = (14, 7)

if not os.path.exists("plots"):
    os.makedirs("plots")

# Load data
big_dataset = pd.read_csv("Trips_Full Data.csv", parse_dates=['Date'])

# Clean columns
big_dataset.columns = big_dataset.columns.str.strip()

# Filter national
national = big_dataset[big_dataset['Level'] == "National"]

# AUTO FIX
distance_cols = [col for col in national.columns if "Trips" in col and "Total" not in col]

print("Columns used:", distance_cols)

# Compute mean
distance_avg = national[distance_cols].mean()

# Plot 1
plt.figure()
distance_avg.plot(kind='bar')
plt.title("Q1(d): Travellers by Distance Category")
plt.xlabel("Distance Range")
plt.ylabel("Average Trips")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/Q1d_bar.png", dpi=300)
plt.show()

# Plot 2
plt.figure()
distance_avg.plot(marker='o')
plt.title("Q1(d): Distance vs Travel Frequency")
plt.xlabel("Distance Range")
plt.ylabel("Average Trips")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("plots/Q1d_line.png", dpi=300)
plt.show()