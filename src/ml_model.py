"""Machine Learning: classify high-value transactions (amount >= 10,000 BDT).

Features: hour + one-hot transaction type and district.
Models compared: Logistic Regression and Random Forest Classifier.
Run from the project root:  python src/ml_model.py
"""
import pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/mobile_transactions.csv")
df["is_high_value"] = (df["amount_bdt"] >= 10000).astype(int)
X = pd.get_dummies(df[["hour", "type", "district"]], columns=["type", "district"])
y = df["is_high_value"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

rows = []
for name, model in [("Logistic Regression", LogisticRegression(max_iter=1000)),
                    ("Random Forest", RandomForestClassifier(n_estimators=200, random_state=42))]:
    model.fit(X_train, y_train)
    p = model.predict(X_test)
    acc = round(accuracy_score(y_test, p), 3)
    rows.append({"model": name, "accuracy": acc})
    print(name, "-> accuracy:", acc)
    if name == "Random Forest":
        print(classification_report(y_test, p, target_names=["Normal", "High-value"]))

pd.DataFrame(rows).to_csv("outputs/tables/model_results.csv", index=False)
imp = pd.Series(model.feature_importances_, index=X.columns).sort_values()
plt.figure(figsize=(8, 4.5)); imp.plot(kind="barh", color="#2e75b6")
plt.title("What predicts a high-value transaction? (feature importance)")
plt.tight_layout(); plt.savefig("outputs/charts/feature_importance.png"); plt.close()
print("Saved outputs/tables/model_results.csv and outputs/charts/feature_importance.png")
