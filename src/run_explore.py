import json, sys
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from explore_engine import broken_revenue, correct_revenue, fanout_factor
DATA, OUT = ROOT / "data", ROOT / "output"
OUT.mkdir(parents=True, exist_ok=True)

def main():
    orders = pd.read_csv(DATA / "orders.csv")
    lines = pd.read_csv(DATA / "order_line.csv")
    promos = pd.read_csv(DATA / "promotions.csv")
    broken, fanned = broken_revenue(orders, lines, promos)
    correct = correct_revenue(lines)
    summary = {
        "broken_explore_revenue": broken,
        "correct_revenue": correct,
        "fanout_factor": fanout_factor(broken, correct),
    }
    fanned.to_csv(OUT / "fanned_rows_sample.csv", index=False)
    pd.DataFrame([summary]).to_csv(OUT / "explore_metrics.csv", index=False)
    print(json.dumps(summary, indent=2))
if __name__ == "__main__":
    main()
