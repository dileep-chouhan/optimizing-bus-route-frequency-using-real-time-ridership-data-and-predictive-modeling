import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit
# --- 1. Synthetic Data Generation ---
np.random.seed(42) # for reproducibility
# Simulate bus route data
num_routes = 5
num_days = 30
routes = [f'Route {i+1}' for i in range(num_routes)]
dates = pd.date_range(start='2024-01-01', periods=num_days)
data = {
    'Date': [],
    'Route': [],
    'Passengers': []
}
for date in dates:
    for route in routes:
        passengers = np.random.poisson(lam=np.random.randint(10, 100)) # Poisson distribution for passenger counts
        data['Date'].append(date)
        data['Route'].append(route)
        data['Passengers'].append(passengers)
df = pd.DataFrame(data)
# --- 2. Data Analysis ---
# Calculate daily average ridership per route
daily_ridership = df.groupby(['Date', 'Route'])['Passengers'].sum().unstack()
# Simple predictive model (linear regression - example, can be improved)
def linear_model(x, a, b):
    return a*x + b
params, covariance = curve_fit(linear_model, range(len(daily_ridership)), daily_ridership['Route 1'])
predicted_route1 = [linear_model(i, *params) for i in range(len(daily_ridership))]
# --- 3. Visualization ---
plt.figure(figsize=(12,6))
for route in routes:
    plt.plot(daily_ridership.index, daily_ridership[route], label=route)
plt.plot(daily_ridership.index, predicted_route1, label='Route 1 Prediction', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.title('Daily Ridership per Route')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('daily_ridership.png')
print("Plot saved to daily_ridership.png")
# --- 4. Optimization (Conceptual - requires more advanced techniques) ---
# This section is a placeholder.  Real optimization would involve:
# - More sophisticated predictive modeling (e.g., time series analysis, ARIMA)
# - Consideration of operational costs (fuel, driver salaries, etc.)
# - Optimization algorithms (e.g., linear programming) to find optimal frequencies.
print("\nNote: Optimization section requires more advanced techniques and is not fully implemented in this example.")
#Example of how to access and use the data for further analysis
average_passengers_route1 = daily_ridership['Route 1'].mean()
print(f"\nAverage passengers on Route 1: {average_passengers_route1:.2f}")