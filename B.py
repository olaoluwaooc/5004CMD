import pandas as pd
import matplotlib.pyplot as plt
import os


# GLOBAL SETTINGS
plt.rcParams["figure.figsize"] = (14, 7)


# CREATE PLOTS FOLDER
if not os.path.exists("plots"):
    os.makedirs("plots")


# LOAD DATASET
big_dataset = pd.read_csv("Trips_Full Data.csv", parse_dates=['Date'])


# FILTER NATIONAL DATA
national = big_dataset[big_dataset['Level'] == "National"]


# FILTER CONDITIONS 
set1 = national[national['Trips 10-25 Miles'] > 10000000]
set2 = national[national['Trips 50-100 Miles'] > 10000000]


# PLOT 1: 10–25 MILES
plt.figure()
plt.scatter(set1['Date'], set1['Trips 10-25 Miles'])

plt.title("Q1(b): Trips 10–25 Miles (>10M)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.grid(alpha=0.4)
plt.tight_layout()

plt.savefig("plots/Q1b_trips_10_25.png", dpi=300, bbox_inches="tight")
plt.show()


# PLOT 2: 50–100 MILES
plt.figure()
plt.scatter(set2['Date'], set2['Trips 50-100 Miles'])

plt.title("Q1(b): Trips 50–100 Miles (>10M)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.grid(alpha=0.4)
plt.tight_layout()

plt.savefig("plots/Q1b_trips_50_100.png", dpi=300, bbox_inches="tight")
plt.show()


# PLOT 3: COMPARISON
plt.figure()

plt.scatter(set1['Date'], set1['Trips 10-25 Miles'], label='10-25 Miles')
plt.scatter(set2['Date'], set2['Trips 50-100 Miles'], label='50-100 Miles')

plt.title("Q1(b): Comparison of High Volume Trips", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()

plt.savefig("plots/Q1b_comparison.png", dpi=300, bbox_inches="tight")
plt.show()