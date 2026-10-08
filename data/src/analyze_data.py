import pandas as pd
import matplotlib.pyplot as plt


# Load the synthetic flight pricing dataset
data = pd.read_csv("data/flight_data.csv")

# Display basic information
print("First five observations:")
print(data.head())

print("\nSummary statistics:")
print(data.describe())

# Analyze correlation between variables
print("\nCorrelation matrix:")
print(data.corr(numeric_only=True))

# Visualize ticket price vs. days to departure
plt.figure(figsize=(8, 5))

plt.plot(
    data["days_to_departure"],
    data["ticket_price"],
    marker="o"
)

plt.xlabel("Days to Departure")
plt.ylabel("Ticket Price ($)")
plt.title("Ticket Price vs. Days to Departure")

# Reverse x-axis so departure date approaches from left to right
plt.gca().invert_xaxis()

plt.grid(True)
plt.tight_layout()

plt.savefig("price_vs_departure.png")

print("\nChart saved as price_vs_departure.png")
