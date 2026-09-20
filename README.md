# 📊 2020 Lockdown Impact: Unemployment Analysis Dashboard

An interactive Data Exploratory Analysis (EDA) dashboard built using **Python** and **Streamlit** to investigate, visualize, and map the intense structural shifts in socioeconomic metrics across regional India during the critical 2020 economic lockdown window.

---

## 🌟 Project Overview
This repository contains a full-stack data product engineered as a submission task for the **Alpha Internship Program**. The project transforms raw economic observation layers into dynamic visual metrics to extract historical insights during the lockdown shock phase.

It provides data ingestion pipelines, cleaning algorithms, and high-level metric monitoring panels divided natively into logical visual layers.

---

## 🛠️ Tech Stack & Libraries
- **Core Engine:** Python 3.x
- **Web Interface:** Streamlit (Native stateful UI framework)
- **Data Structuring:** Pandas, NumPy
- **Statistical Analytics & Charts:** Seaborn, Matplotlib

---

## 📌 Features & Visual Layers

The analytics framework is neatly categorized into three modern web layout tabs:
1. **Overview & Key Performance Indicators (KPIs):** Displays high-level dynamic indicator tiles capturing National Mean Unemployment, Peak Unemployment Spikes, and National Average Labour Participation along with a clean sanitized dataset grid preview.
2. **Temporal Timeline Trends:** Renders aggregated national dataset progressions over the cyclical timeline framework using continuous marker plots.
3. **Regional & Sector Breakdowns:** Contrasts categorical density footprints side-by-side using Seaborn boxplots (Rural vs Urban distribution) and sequential ranked regional bar charts.

---

## 📁 Repository Structure
```text
├── Data/
│   └── Unemployment_in_India.csv     # The sanitization dataset tracking source metrics
├── app.py                            # Optimized deployment production production application layer script
├── Unemployment_Analysis.ipynb       # Preliminary exploratory sandboxed evaluation notebook
├── requirements.txt                  # Deployment baseline packages environment index
└── README.md                         # Product presentation metadata
```

---

## 🚀 Local Deployment Instructions

Follow these sequential environment steps to initialize this analytics node on your local system:

### 1. Clone this Repository
```bash
git clone https://github.com
cd YOUR_REPOSITORY_NAME
```

### 2. Install Package Dependencies
Ensure you have all requisite visual frameworks installed by utilizing the dependency environment matrix:
```bash
pip install -r requirements.txt
```
*(If `requirements.txt` is not created, execute: `pip install streamlit pandas numpy matplotlib seaborn`)*

### 3. Initialize the Streamlit Server Engine
Boot the localized microservice directly from your terminal console:
```bash
streamlit run app.py
```

---

## 📊 Sample Insights Evaluated
- **Lockdown Volatility Spikes:** Peak tracking thresholds mapped instances hitting severe highs of up to **76.74%** across volatile regional zones.
- **National Metric Compression:** The historical baseline index established structural shifts, reporting a baseline average national contraction threshold of **11.79%** across all localized matrices.
- **Participation Shifts:** Analyzed sector densities reveal significant variation across Rural and Urban nodes, as visualized within the sector boxplot distribution grids.

---

## 🎓 Internship Metadata
- **Program Resource:** Alpha Internship Submission Task
- **Domain Focus:** Data Science, Business Intelligence & Frontend UI Prototyping
- **Developer:** [Your Name / Profile]
