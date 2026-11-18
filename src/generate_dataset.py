"""Generate the dataset for this project (synthetic data, NumPy seed-based)."""
import numpy as np, pandas as pd, os
rng = np.random.default_rng(11)
os.makedirs("data", exist_ok=True)
n = 700
types = ["Send Money", "Cash Out", "Payment", "Remittance", "Salary", "Cash In"]
tp = [0.30, 0.22, 0.18, 0.08, 0.07, 0.15]
districts = ["Dhaka", "Chattogram", "Khulna", "Rajshahi", "Sylhet", "Barishal", "Rangpur", "Mymensingh"]
ttype = rng.choice(types, n, p=tp)
district = rng.choice(districts, n, p=[0.34, 0.14, 0.10, 0.11, 0.08, 0.06, 0.09, 0.08])
dates = pd.date_range("2025-01-01", periods=120, freq="D")
date = rng.choice(dates, n)
hour = rng.choice(range(24), n, p=[0.01,0.01,0.01,0.01,0.01,0.02,0.04,0.06,0.07,0.07,0.06,0.06,0.06,0.06,0.05,0.05,0.05,0.06,0.07,0.06,0.05,0.03,0.02,0.01])
amount_map = {"Send Money": (2400, 1800), "Cash Out": (5200, 3800), "Payment": (1500, 1200),
              "Remittance": (14500, 7000), "Salary": (21000, 6000), "Cash In": (4600, 3200)}
amount = np.array([max(50, rng.normal(*amount_map[t])) for t in ttype]).round(2)
fee_rate = {"Send Money": 0.005, "Cash Out": 0.0185, "Payment": 0.0, "Remittance": 0.0, "Salary": 0.0, "Cash In": 0.0}
fee = np.round(amount * np.array([fee_rate[t] for t in ttype]), 2)
df = pd.DataFrame({"date": pd.Series(date).dt.date, "hour": hour, "type": ttype, "district": district,
                   "amount_bdt": amount, "fee_bdt": fee})
df.to_csv("data/mobile_transactions.csv", index=False)
print("Saved", len(df), "transactions")
