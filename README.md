# Looker Explore Semantics Lab

**Author:** [Faiz Elahi](https://github.com/faizilahi) (`faizilahi`) · **Type:** EDUCATIONAL LAB · **Synthetic data only**

---

## Educational disclaimer

This is an **educational portfolio lab**. Datasets are **synthetic**. It does **not** claim employment at a customer, hospital, bank, SAP shop, or Oracle estate. No real PHI/PII. No live cloud spend. No API keys required.

---

## Problem statement

Looker explores must point at certified grains so ALOS/revenue definitions match Power BI/Sigma/dbt exposures.

**Domain focus:** Self-serve BI semantics

---

## Why this tool (Looker-style explores / LookML habits)

| Explore sprawl | One explore per certified grain |
|---|---|
| Dashboard math | Measures from YAML only |

---

## Architecture

```mermaid
flowchart LR
  GEN[generate_synthetic_data.py]
  DATA[data/*.csv]
  RUN[run_lab.py]
  OUT[output/*.csv]
  CHART[generate_charts.py]
  IMG[docs/images/*.png]
  GEN --> DATA --> RUN --> OUT
  OUT --> CHART --> IMG
```

See [`docs/architecture.md`](docs/architecture.md).

---

## Dataset dictionary

| File | Notes |
|------|-------|
| `lookml/explore_orders.yml` | Explore |
| `output/summary.csv` | Explore query result |

---

## Prerequisites

- Python 3.10+
- Packages in `requirements.txt`

---

## How to run

```powershell
cd "looker-explore-semantics-lab"
python -m venv .venv
.\\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/generate_synthetic_data.py
python src/run_lab.py
python scripts/generate_charts.py
```

Inspect `output/summary.csv` and `docs/images/primary_metric.png`.

---

## Local vs cloud (honest)

YAML LookML-inspired explores + DuckDB. No Looker instance.

---

## Results interpretation

Open `output/` CSVs and the PNGs under `docs/images/`. Numbers are synthetic teaching fixtures — use them to explain grain, filters, and control totals, not as real business KPIs.

---

## Limitations

- Stand-in engines (DuckDB/SQLite/pandas) replace paid MPP/warehouses where noted.
- Simplified schemas vs production SAP/Oracle/Hive estates.
- Charts are matplotlib teaching visuals, not vendor BI embeds.

---

## Exercises

1. Add a symmetric aggregate caution note.
2. Join a users view safely.
3. Point explore at dbt exposure names.

---

## License / attribution

Educational portfolio content by Faiz Elahi. Synthetic data for teaching only.

