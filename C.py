import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

plt.rcParams["figure.figsize"] = (14, 7)

if not os.path.exists("plots"):
    os.makedirs("plots")

# Load data
big_dataset = pd.read_csv("Trips_Full Data.csv", parse_dates=['Date'])

# Clean column names
big_dataset.columns = big_dataset.columns.str.strip()

# Filter national data
national = big_dataset[big_dataset['Level'] == "National"]

# AUTO-DETECT COLUMNS
print(national.columns.tolist())

col_10_25 = [col for col in national.columns if "10-25" in col][0]
col_50_100 = [col for col in national.columns if "50-100" in col][0]

print("Using:", col_10_25, "and", col_50_100)

# Model data
X = np.array(national[col_10_25]).reshape(-1, 1)
y = np.array(national[col_50_100]).reshape(-1, 1)

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Evaluate
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)

print("RMSE:", rmse)
print("R²:", r2)

# Plot
plt.figure()
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")

plt.title("Q1(c): Regression – Trip Distance vs Frequency")
plt.xlabel(col_10_25)
plt.ylabel(col_50_100)
plt.legend()
plt.grid(alpha=0.4)
plt.tight_layout()

plt.savefig("plots/Q1c_regression.png", dpi=300, bbox_inches="tight")
plt.show()