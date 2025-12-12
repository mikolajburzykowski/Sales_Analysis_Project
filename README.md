# Sales Analysis — sample project

This project demonstrates a simple end-to-end data analysis workflow: loading sales data, cleaning and merging datasets, calculating KPIs, generating visualizations, and exporting everything into a multi-sheet Excel report.
All data used in the project is synthetic and provided only for demonstration.

---

## Project structure

The repository is organized as follows:

```
sales_project/
│   ├── sales.csv
│   ├── categories.csv
│   ├── sales_report.xlsx        # sample output / notebook
│   ├── product_revenue.png      # sample output
│   ├── category_revenue.png     # sample output
│   └── orders_per_day.png       # sample output

sales_analysis.ipynb             # notebook version
sales_analysis.py                # runnable Python script
requirements.txt
README.md
LICENSE
```

---

## Highlights / Business insights

**Short takeaway:**  
Electronics generate the highest revenue but with fewer purchases; food has frequent purchases but low order value. Potential improvement areas include pricing strategy and targeted promotions.

**KPI summary:**
- **Total revenue:** `X`
- **Most profitable category:** `Electronics`
- **Best-selling product:** `Laptop`
- **Average order value:** `Y`

---

## Files & notebooks

- **sales_analysis.ipynb** — step-by-step analysis (loading data, cleaning, merging, KPIs, charts, export).  
- **sales_analysis.py** — script version executed from terminal.  
- **sales_project/*.csv** — input data.  
- **sales_project/sales_report.xlsx** — full Excel report with multiple sheets (included as a sample output).
- **sales_project/*.png** — generated visualizations (included as example outputs).

---

## How to run (local)

It is recommended to use a Python virtual environment.

### 1. Create and activate a virtual environment

#### macOS / Linux

```
python3 -m venv .venv
source .venv/bin/activate
```
#### Windows
```
python -m venv .venv
.\.venv\Scripts\activate
```
2. Install dependencies
```
pip install -r requirements.txt
```
3. Run the script
```
python sales_analysis.py
```
This will:

- print a KPI summary to the console
- generate sales_report.xlsx
- save charts into sales_project/*.png

4. (Optional) Run the notebook
```
jupyter notebook sales_analysis.ipynb
```
This is useful if you prefer to walk through the analysis step by step or explore the code interactively.

### Additional notes

All data in this project is synthetic and included only for demonstration.


The project is intentionally simple and aims to showcase basic data analysis skills in Python.

