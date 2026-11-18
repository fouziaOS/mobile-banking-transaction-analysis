# Key Insights — Mobile Banking Transaction Analysis

- Dataset: 700 transactions, total volume **3,861,740 BDT**.
- Most frequent transaction type: **Send Money**.
- Highest-volume district: **Dhaka**.
- Most fee income comes from: **Cash Out** (16,009 BDT in fees).
- Peak transaction hour: **18:00**.

## Machine Learning — prediction model
Classify whether a transaction is high-value (`amount_bdt` ≥ 10,000 BDT) from hour, type and district. This is a classification problem, so the metric is accuracy.

| Model | R² / Accuracy | RMSE |
|---|---|---|
| Logistic Regression | 0.957 accuracy | — |
| Random Forest | 0.886 accuracy | — |

**Best model: Logistic Regression.** Logistic Regression correctly flags **95.7%** of transactions. Transaction type (Remittance/Salary) is the strongest signal, as the feature-importance chart shows.

Run it yourself: `python src/ml_model.py` (needs scikit-learn, already in `requirements.txt`).
Results are saved in `outputs/tables/model_results.csv`.
