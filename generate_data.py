import pandas as pd
import numpy as np

np.random.seed(42)
N = 1000  # Number of samples

data = {
    "energy_usage": np.random.uniform(50, 200, N),         # MWh/year
    "renewable_pct": np.random.uniform(0, 100, N),         # %
    "recycling_pct": np.random.uniform(0, 100, N),         # %
    "green_investments": np.random.uniform(1000, 500000, N), # $
}

# Simulate a green_score based on a simple formula + noise
data["green_score"] = (
    0.2 * (200 - data["energy_usage"]) +
    0.3 * data["renewable_pct"] +
    0.3 * data["recycling_pct"] +
    0.00005 * data["green_investments"]
)

# Clip green_score to 0-100
data["green_score"] = np.clip(data["green_score"], 0, 100)

df = pd.DataFrame(data)

# ---- Add this block to explicitly include edge cases ----
edge_cases = pd.DataFrame([
    {
        "energy_usage": 200,
        "renewable_pct": 0,
        "recycling_pct": 0,
        "green_investments": 0,
        "green_score": 0  # worst case: should be 0
    },
    {
        "energy_usage": 50,
        "renewable_pct": 100,
        "recycling_pct": 100,
        "green_investments": 500000,
        "green_score": 100  # best case: should be 100
    }
])
df = pd.concat([df, edge_cases], ignore_index=True)
# ---- End edge case block ----

# Clip again after edge cases, to ensure all scores remain in [0, 100]
df["green_score"] = np.clip(df["green_score"], 0, 100)

df.to_csv("app/data.csv", index=False)
print("Generated app/data.csv with", len(df), "rows.")