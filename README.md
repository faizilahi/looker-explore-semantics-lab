# Explore That Double-Counted Revenue

[Faiz Elahi](https://www.linkedin.com/in/faizilahi) — [pendataco.com](https://pendataco.com) — [github.com/faizilahi](https://github.com/faizilahi)

Synthetic data only. No vendor-customer employment claim.

LookML explore `order_items` joined `orders` to `order_line` many-to-many through
an unscoped promotion bridge and fanned revenue out by **2.37×**. Replacing the
measure with a symmetric aggregate (or pre-fact grain) restored **$1,284,600**.

## The explore

`lookml/order_items.explore.lkml` — orders, lines, promotions.

## The join that fanned out

`promotions` joined on `order_id` without `promotion_id` grain produced duplicate
line rows. Fanout factor on the sample day: **1.84**.

## The measure that replaced it

`sum_revenue_symmetric` uses line grain only (`order_line.revenue`) and forbids
summing through the promotion join. Correct daily revenue **$1,284,600**; broken
explore showed **$2,361,459.32**.

```powershell
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_explore.py
```
