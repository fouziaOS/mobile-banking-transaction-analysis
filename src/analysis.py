"""Main analysis: tables, charts and insights. Run from the project root: python src/analysis.py"""
import pandas as pd, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, os
os.makedirs("outputs/charts", exist_ok=True); os.makedirs("outputs/tables", exist_ok=True)
df = pd.read_csv("data/mobile_transactions.csv")
df.groupby("type")["amount_bdt"].agg(["count", "mean", "sum"]).round(2).to_csv("outputs/tables/volume_by_type.csv")
df.groupby("district")["amount_bdt"].agg(["count", "mean", "sum"]).round(2).to_csv("outputs/tables/volume_by_district.csv")
df.groupby("type")["fee_bdt"].sum().round(2).rename("total_fee_bdt").to_csv("outputs/tables/fee_by_type.csv")
df.groupby("hour").size().rename("transactions").to_csv("outputs/tables/transactions_by_hour.csv")
plt.figure(figsize=(8, 4.5)); df.groupby("type").size().sort_values().plot(kind="barh", color="#2e75b6")
plt.title("Transactions by Type"); plt.xlabel("Count"); plt.tight_layout(); plt.savefig("outputs/charts/transactions_by_type.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("district")["amount_bdt"].sum().sort_values().plot(kind="barh", color="#548235")
plt.title("Total Amount by District"); plt.xlabel("BDT"); plt.tight_layout(); plt.savefig("outputs/charts/amount_by_district.png"); plt.close()
plt.figure(figsize=(8, 4.5)); df.groupby("hour").size().plot(kind="line", marker="o", color="#c55a11")
plt.title("Transactions by Hour"); plt.xlabel("Hour"); plt.ylabel("Count"); plt.tight_layout(); plt.savefig("outputs/charts/transactions_by_hour.png"); plt.close()
plt.figure(figsize=(8, 4.5)); plt.hist(df[df["amount_bdt"] < 30000]["amount_bdt"], bins=20, color="#7030a0")
plt.title("Distribution of Transaction Amounts (under 30,000 BDT)"); plt.xlabel("BDT"); plt.tight_layout(); plt.savefig("outputs/charts/amount_distribution.png"); plt.close()
top_type = df.groupby("type").size().idxmax()
top_dist = df.groupby("district")["amount_bdt"].sum().idxmax()
fee_type = df.groupby("type")["fee_bdt"].sum().idxmax()
peak_hour = int(df.groupby("hour").size().idxmax())
ins = f"""# Key Insights — Mobile Banking Transaction Analysis

- Dataset: {len(df)} transactions, total volume **{df['amount_bdt'].sum():,.0f} BDT**.
- Most frequent transaction type: **{top_type}**.
- Highest-volume district: **{top_dist}**.
- Most fee income comes from: **{fee_type}** ({df.groupby('type')['fee_bdt'].sum().max():,.0f} BDT in fees).
- Peak transaction hour: **{peak_hour}:00**.
"""
open("outputs/insights.md", "w").write(ins)
print(ins)
