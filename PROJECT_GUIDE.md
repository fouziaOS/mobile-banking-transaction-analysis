# PROJECT GUIDE — Mobile Banking Transaction Analysis

A complete explanation of this project for beginners: what it is, what every file
and column means, how the code works step by step, and how to explain it in a viva.

## 1. What is this project?
Analyzing 700 mobile banking transactions (bKash-style) — types, amounts, fees and peak hours. It is a full data-analysis workflow: create data → clean and explore it →
group and summarize → draw charts → write honest insights. Dataset size: 700 transactions.

## 2. Files in this project
- `README.md` — project summary with the key results and chart images.
- `PROJECT_GUIDE.md` — this guide.
- `requirements.txt` — the Python libraries needed (pandas, numpy, matplotlib).
- `src/generate_dataset.py` — builds the dataset with NumPy random numbers (fixed seed = same data every run).
- `src/analysis.py` — the main analysis code.
- `data/mobile_transactions.csv` — the dataset (created by generate_dataset.py).
- `mobile-banking-transaction-analysis.ipynb` — the same analysis as a Jupyter notebook.
- `outputs/charts/` — chart images:
- `amount_by_district.png`
- `amount_distribution.png`
- `transactions_by_hour.png`
- `transactions_by_type.png`
- `outputs/tables/` — summary tables (CSV):
- `fee_by_type.csv`
- `transactions_by_hour.csv`
- `volume_by_district.csv`
- `volume_by_type.csv`
- `outputs/insights.md` — the key findings in plain words.

## 3. Dataset columns explained
| Column | Meaning |
|---|---|
| date | Transaction date |
| hour | Hour of day (0–23) |
| type | Send Money / Cash Out / Payment / Remittance / Salary / Cash In |
| district | District |
| amount_bdt | Amount in BDT |
| fee_bdt | Fee charged in BDT |

## 4. How to run it (step by step)
1. Open a terminal inside this project folder.
2. Install the libraries: `pip install -r requirements.txt`
3. Create the data: `python src/generate_dataset.py`
4. Run the analysis: `python src/analysis.py`
5. Look inside `outputs/` — charts, tables and insights are created there.
6. Or open `mobile-banking-transaction-analysis.ipynb` in Jupyter and run the cells one by one.

## 5. How the code works
**generate_dataset.py** — sets a fixed NumPy seed, chooses categories with realistic
probabilities, builds numeric columns from related formulas (so the data behaves like
real life), assembles a Pandas DataFrame and saves it as CSV.

**analysis.py** — loads the CSV with Pandas, then:
1. `groupby(...)` summaries → saved as tables in `outputs/tables/`.
2. A correlation matrix for the numeric columns.
3. Four Matplotlib charts → saved in `outputs/charts/`.
4. The most important numbers are written into `outputs/insights.md`.

## 6. Key results
# Key Insights — Mobile Banking Transaction Analysis

- Dataset: 700 transactions, total volume **3,861,740 BDT**.
- Most frequent transaction type: **Send Money**.
- Highest-volume district: **Dhaka**.
- Most fee income comes from: **Cash Out** (16,009 BDT in fees).
- Peak transaction hour: **18:00**.

## 7. How to read the charts
- **Bar charts** compare groups (which group is biggest / most expensive / slowest).
- **Line charts** show change over time or hour — look for peaks.
- **Histograms** show how values are spread (most common range, rare extremes).
- **Scatter plots** show relationships between two numbers — an upward or downward
  cloud means the two move together (check the correlation value in the tables).

## 8. Viva / interview questions
**Q: Which transaction type earns the most fees?**
A: Cash Out — it has the highest fee rate (1.85%) and large average amounts.

**Q: Why does the peak hour matter?**
A: The provider must keep servers and agent liquidity ready at peak times.

**Q: What does the amount distribution show?**
A: Most transactions are small; a few large remittance/salary payments pull the average up.

## 9. Honest note
The data is synthetic (computer-generated with realistic patterns), made for learning
and portfolio demonstration. The workflow, code and analysis method are exactly what
would be used with real data.
