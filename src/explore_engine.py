import pandas as pd

def broken_revenue(orders, lines, promos):
    # fanout join
    fanned = lines.merge(orders, on="order_id").merge(promos, on="order_id", how="left")
    return round(float(fanned["revenue"].sum()), 2), fanned

def correct_revenue(lines):
    return round(float(lines["revenue"].sum()), 2)

def fanout_factor(broken, correct):
    return round(broken / correct, 2) if correct else None
