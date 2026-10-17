
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD AND PREPARE THE DATA
# ==========================================

df = pd.read_csv("data.csv", skipinitialspace=True)

# Clean column names
df.columns = df.columns.str.strip()

# Remove extra spaces from column values
for column in df.select_dtypes(include="object").columns:
    df[column] = df[column].str.strip()

# Convert temperature from text to number
# Parentheses around 0.3 are interpreted as -0.3
df["temperature"] = (
    df["temperature"]
    .astype(str)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
)

df["temperature"] = pd.to_numeric(df["temperature"])

# Convert other measurements to numbers
df["humidity"] = pd.to_numeric(df["humidity"])
df["atmospheric pressure"] = pd.to_numeric(
    df["atmospheric pressure"]
)

# Create a complete date from year and month/day
df["date"] = pd.to_datetime(
    df["year"].astype(str) + "/" + df["day"],
    format="%Y/%m/%d"
)

# Sort data chronologically
df = df.sort_values("date").reset_index(drop=True)

# ==========================================
# 2. TEMPERATURE OVERVIEW
# ==========================================

average_temperature = df["temperature"].mean()

print("\n1. TEMPERATURE OVERVIEW")
print("Overall average temperature:",
      round(average_temperature, 2), "°C")

# ==========================================
# 3. MONTHLY AVERAGE TEMPERATURE
# ==========================================

df["month"] = df["date"].dt.month

monthly_average = df.groupby("month")["temperature"].mean()

# Display month names instead of numbers
monthly_average.index = monthly_average.index.map(
    lambda month: pd.Timestamp(
        month=month, day=1, year=2023
    ).strftime("%B")
)

print("\n2. MONTHLY AVERAGE TEMPERATURE")
print(monthly_average.round(2))

# Bar plot of monthly average temperatures
monthly_average.plot(
    kind="bar",
    color="skyblue",
    edgecolor="black"
)

plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# 4. HOTTEST AND COLDEST DAYS
# ==========================================

hottest_day = df.loc[df["temperature"].idxmax()]
coldest_day = df.loc[df["temperature"].idxmin()]

print("\n3. HOTTEST DAY")
print(hottest_day)

print("\nCOLDEST DAY")
print(coldest_day)

# ==========================================
# 5. TEMPERATURE TRENDS OVER TIME
# ==========================================

plt.figure(figsize=(12, 5))

plt.plot(
    df["date"],
    df["temperature"],
    color="red",
    linewidth=1
)

plt.title("Daily Temperature Changes Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ==========================================
# 6. SEASONAL AVERAGE TEMPERATURE
# ==========================================

def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"


df["season"] = df["date"].dt.month.map(get_season)

seasonal_average = df.groupby("season")["temperature"].mean()

# Display seasons in chronological order
season_order = ["Winter", "Spring", "Summer", "Autumn"]
seasonal_average = seasonal_average.reindex(season_order)

print("\n4. SEASONAL AVERAGE TEMPERATURE")
print(seasonal_average.round(2))

# Plot seasonal averages
seasonal_average.plot(
    kind="bar",
    color="orange",
    edgecolor="black"
)

plt.title("Average Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Average Temperature (°C)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
