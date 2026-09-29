from pathlib import Path
import yaml, pandas as pd
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"output"; OUT.mkdir(parents=True, exist_ok=True)
explore=yaml.safe_load((ROOT/"lookml"/"explore_orders.yml").read_text(encoding="utf-8"))
df=pd.read_csv(ROOT/"data"/"orders.csv")
# Only measures declared in explore may be computed
measures={m["name"]:m for m in explore["measures"]}
filt=df[df["status"].isin(explore.get("default_filters",{}).get("status",df["status"].unique()))]
summary=filt.groupby("status",as_index=False).agg(orders=("order_id","count"),revenue=("revenue","sum"))
summary["revenue"]=summary["revenue"].round(2)
assert "revenue" in measures and "orders" in measures
summary.to_csv(OUT/"summary.csv",index=False)
print(summary)

