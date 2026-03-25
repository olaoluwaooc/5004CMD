# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import os


# GLOBAL PLOT SETTINGS
plt.rcParams["figure.figsize"] = (14, 7)
plt.rcParams["figure.dpi"] = 120


# CREATE PLOTS FOLDER
if not os.path.exists("plots"):
    os.makedirs("plots")


# LOAD DATASETS
small_dataset = pd.read_csv(
    "/Users/roti/Desktop/5004CMD/Trips_by_Distance.csv",
    parse_dates=['Date']
)

big_dataset = pd.read_csv(
    "/Users/roti/Desktop/5004CMD/Trips_Full Data.csv",
    parse_dates=['Date']
)


# FILTER NATIONAL DATA
national = big_dataset[big_dataset['Level'] == "National"]


# 1. PEOPLE STAYING HOME
weekly_home = small_dataset.groupby(
    small_dataset['Date'].dt.isocalendar().week
)['Population Staying at Home'].mean()

plt.figure()
weekly_home.plot(kind='bar')
plt.title("Average People Staying at Home per Week", fontsize=14)
plt.xlabel("Week")
plt.ylabel("Population")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("plots/weekly_home.png", dpi=300, bbox_inches="tight")
plt.show()


# 2. PEOPLE NOT STAYING HOME
weekly_not_home = small_dataset.groupby(
    small_dataset['Date'].dt.isocalendar().week
)['People Not Staying at Home'].mean()

plt.figure()
weekly_not_home.plot(kind='bar')
plt.title("Average People Not Staying at Home per Week", fontsize=14)
plt.xlabel("Week")
plt.ylabel("Population")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("plots/weekly_not_home.png", dpi=300, bbox_inches="tight")
plt.show()


# 3. TRIPS BY DISTANCE
distance_cols = [
    'Trips 1-25 Miles',
    'Trips 25-50 Miles',
    'Trips 50-100 Miles',
    'Trips 100+ Miles'
]

distance_mean = small_dataset[distance_cols].mean()

plt.figure()
distance_mean.plot(kind='bar')
plt.title("Mean Trips by Distance Range", fontsize=14)
plt.xlabel("Distance Range")
plt.ylabel("Average Trips")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("plots/distance_trips.png", dpi=300, bbox_inches="tight")
plt.show()


# 4. HIGH VOLUME TRIPS (10–25)
set1 = national[national['Number of Trips 10-25'] > 10000000]

plt.figure()
plt.scatter(set1['Date'], set1['Number of Trips 10-25'])
plt.title("Trips 10–25 Miles (>10M)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("plots/trips_10_25.png", dpi=300, bbox_inches="tight")
plt.show()


# 5. HIGH VOLUME TRIPS (50–100)
set2 = national[national['Number of Trips 50-100'] > 10000000]

plt.figure()
plt.scatter(set2['Date'], set2['Number of Trips 50-100'])
plt.title("Trips 50–100 Miles (>10M)", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("plots/trips_50_100.png", dpi=300, bbox_inches="tight")
plt.show()


# 6. COMPARISON SCATTER
plt.figure()
plt.scatter(set1['Date'], set1['Number of Trips 10-25'], label='10-25 Miles')
plt.scatter(set2['Date'], set2['Number of Trips 50-100'], label='50-100 Miles')

plt.title("Comparison of High Volume Trips", fontsize=14)
plt.xlabel("Date")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()
plt.savefig("plots/comparison_trips.png", dpi=300, bbox_inches="tight")
plt.show()


# 7. DISTANCE DISTRIBUTION
distance_full = [
    'Number of Trips 1-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100+'
]

distance_avg = national[distance_full].mean()

plt.figure()
distance_avg.plot(kind='bar')
plt.title("Travellers by Distance Category", fontsize=14)
plt.xlabel("Distance Range")
plt.ylabel("Average Trips")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("plots/distance_distribution.png", dpi=300, bbox_inches="tight")
plt.show()