import pandas as pd, numpy as np
from pathlib import Path
RNG=np.random.default_rng(14)
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data"; DATA.mkdir(parents=True, exist_ok=True)
pd.DataFrame({"order_id":range(1,201),"user_id":RNG.integers(1,60,200),
  "revenue":RNG.uniform(10,300,200).round(2),"status":RNG.choice(["complete","returned"],200)}).to_csv(DATA/"orders.csv",index=False)
print("Wrote Looker lab data")

