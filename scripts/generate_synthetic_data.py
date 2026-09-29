from pathlib import Path
import numpy as np, pandas as pd
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"; DATA.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(1284)
orders = pd.DataFrame({"order_id": [f"O{i:05d}" for i in range(1, 401)], "order_date": "2024-04-02"})
lines = []
for oid in orders.order_id:
    for j in range(int(RNG.integers(1, 4))):
        lines.append({"order_id": oid, "line_id": f"{oid}-L{j}", "revenue": round(float(RNG.uniform(20, 200)), 2)})
lines = pd.DataFrame(lines)
# scale to exact 1284600
factor = 1284600 / lines.revenue.sum()
lines["revenue"] = (lines["revenue"] * factor).round(2)
drift = round(1284600 - lines.revenue.sum(), 2)
lines.iloc[-1, lines.columns.get_loc("revenue")] += drift
# promotions: ~2.37 avg per order for subset
promos = []
for i, oid in enumerate(orders.order_id):
    n = 3 if i % 5 == 0 else (2 if i % 2 == 0 else 1)
    for p in range(n):
        promos.append({"order_id": oid, "promotion_id": f"P{p}", "promo_name": f"Promo{p}"})
orders.to_csv(DATA / "orders.csv", index=False)
lines.to_csv(DATA / "order_line.csv", index=False)
pd.DataFrame(promos).to_csv(DATA / "promotions.csv", index=False)
print("revenue", lines.revenue.sum(), "promo rows", len(promos))
