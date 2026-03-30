import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Load the dataset
df = pd.read_csv('Trips_by_Distance.csv')

# Choose the distance category
X = df[['Number of Trips 10-25']]   
y = df['Number of Trips']           

# Remove the missing values
data = pd.concat([X, y], axis=1).dropna()
X = data[['Number of Trips 10-25']]
y = data['Number of Trips']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Metrics
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("RMSE:", rmse)
print("R²:", r2)

# Scatterplot
plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)

plt.xlabel('Trips (10–25 miles)')
plt.ylabel('Total Number of Trips')
plt.title('Travel Frequency vs Trip Length (10–25 miles)')

plt.tight_layout()
plt.show()
