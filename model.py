import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# =========================
# LOAD DATA
# =========================
df = pd.read_csv('Trips_by_Distance.csv')
df.columns = df.columns.str.strip()

# =========================
# SELECT FEATURES (SHORT + MEDIUM DISTANCE)
# =========================
features = [
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25'
]

# TARGET (LONG DISTANCE)
target = 'Number of Trips 50-100'

X = df[features]
y = df[target]

# =========================
# CLEAN DATA
# =========================
data = pd.concat([X, y], axis=1).dropna()

X = data[features]
y = data[target]

# =========================
# TRAIN TEST SPLIT
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# MODEL TRAINING
# =========================
model = LinearRegression()
model.fit(X_train, y_train)

# =========================
# PREDICTION
# =========================
y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("RMSE:", rmse)
print("R²:", r2)

# =========================
# COEFFICIENTS (IMPORTANT)
# =========================
coefficients = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_
})

print("\nModel Coefficients:")
print(coefficients)

# =========================
# VISUALISATION
# =========================
plt.figure(figsize=(10,6))

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Trips (50–100 miles)")
plt.ylabel("Predicted Trips")
plt.title("Actual vs Predicted Long-Distance Travel")

# Line of best fit
plt.plot(y_test, y_test)

plt.tight_layout()
plt.show()