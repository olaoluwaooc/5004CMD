import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# load the dataset
df = pd.read_csv('Trips_by_Distance.csv')

# create the average distance
dist_cols = [
    ('Number of Trips <1', 0.5),
    ('Number of Trips 1-3', 2),
    ('Number of Trips 3-5', 4),
    ('Number of Trips 5-10', 7.5),
    ('Number of Trips 10-25', 17.5),
    ('Number of Trips 25-50', 37.5),
    ('Number of Trips 50-100', 75),
    ('Number of Trips 100-250', 175),
    ('Number of Trips 250-500', 375),
    ('Number of Trips >=500', 600)
]

def avg_distance(row):
    total = 0
    trips = 0
    for col, mid in dist_cols:
        total += row[col] * mid
        trips += row[col]
    return total / trips if trips != 0 else 0

df['Avg_Distance'] = df.apply(avg_distance, axis=1)

# prepare the data 
df_model = df[['Avg_Distance', 'Number of Trips']].dropna()

X = df_model[['Avg_Distance']]
y = df_model['Number of Trips']

# train the model 
model = LinearRegression()
model.fit(X, y)

# predictions
y_pred = model.predict(X)

# metrics 
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("RMSE:", rmse)
print("R²:", r2)

# scatterplot
plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.xlabel('Average Distance (miles)')
plt.ylabel('Number of Trips')
plt.title('Distance vs Travel Frequency')
plt.tight_layout()
plt.show()

