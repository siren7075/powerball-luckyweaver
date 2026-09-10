# 🎰 Powerball Study & Interactive Number Generator

A comprehensive Powerball lottery analysis project with an **interactive web-based number generator** featuring probability weighting, period-based decay, and multilingual support.

**⭐ New!** Try the interactive web app: Bilingual UI, batch generation (1-20 sets), intelligent probability decay based on recent draws.

---

## 🚀 Quick Start - Interactive Generator

### Try the Web App

```bash
cd powerball-study
python3 -m venv app_venv
source app_venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Then open: **http://localhost:5001**

### Features
✨ **Bilingual** - English / 中文 toggle  
🎲 **Batch Generation** - Generate 1-20 number sets at once  
📊 **Decay Weighting** - Recent draws have higher weight reduction  
📅 **Period Analysis** - View weight decay by drawing period  
🎯 **Adjustable Strength** - 0% (no decay) to 100% (complete avoidance)  
🎨 **Beautiful UI** - Responsive gradient design with smooth animations  

### How It Works

The generator reduces probability of recently drawn numbers while maintaining variance:

- **Period 5** (most recent) → 100% decay weight
- **Period 4** → 80% decay weight
- **Period 3** → 60% decay weight
- **Period 2** → 40% decay weight
- **Period 1** (oldest) → 20% decay weight

Example: With 60% strength, the most recent draw has numbers with ~60% reduced probability.

---

## 📊 Data Science Study

### Project Overview

Comprehensive analysis of Powerball white ball number patterns across rolling windows of consecutive drawings.

**Research Question**: How do white ball numbers repeat across consecutive drawing windows?

### Dataset

- **Source**: Official New York State Powerball Lottery Records
- **Time Period**: January 2010 - July 2026
- **Total Drawings**: 1,967
- **Data Quality**: Cleaned, validated, no duplicates

### Key Findings

| Window Size | Mean Overlaps | Median | Min | Max |
|-------------|---------------|--------|-----|-----|
| 2 | 0.38 | 0 | 0 | 3 |
| 5 | 3.30 | 3 | 0 | 8 |
| 10 | 11.39 | 12 | 5 | 18 |

**Observation**: Overlap increases with window size, consistent with probability theory.

### Repository Structure

```
powerball-study/
├── app.py                                     # Flask web server
├── powerball_generator.py                     # Number generation logic
├── templates/
│   └── index.html                             # Interactive UI (bilingual)
│
├── data/
│   └── powerball_clean.csv                    # Dataset (1,967 drawings)
│
├── src/                                       # Analysis scripts
│   ├── rolling_window_analysis.py
│   ├── rolling_window_visualizations.py
│   └── generate_report_and_infographic.py
│
└── results/                                   # Analysis outputs
    ├── Powerball_Rolling_Overlap_Report.pdf
    ├── rolling_window_matrix.csv
    └── [visualizations]
```

### Running the Data Analysis

```bash
# Set up
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run analysis
python3 src/rolling_window_analysis.py          # Compute statistics
python3 src/rolling_window_visualizations.py    # Generate charts
python3 src/generate_report_and_infographic.py  # Create report
```

### Outputs

- **PDF Report** - Technical analysis with all visualizations
- **Infographic** - Single-page summary
- **Probability Matrix** - Empirical data (CSV)
- **Charts** - Heatmaps, distributions, statistics

---

## ⚖️ Important Disclaimer

⚠️ **Educational Purpose Only**

- ❌ **No predictive claims** - Patterns do not predict future outcomes
- ❌ **No strategy** - Cannot improve actual lottery odds
- ❌ **Entertainment only** - The web generator is for fun, not gambling advice
- ✅ **Random outcome** - Lottery drawings remain inherently unpredictable

Each Powerball drawing is independent. Historical analysis is descriptive, not predictive.

---

## 🛠️ Technology Stack

**Web App:**
- Flask (Python web framework)
- NumPy (probability calculations)
- Vanilla JavaScript/HTML5/CSS3 (frontend)

**Analysis:**
- Python 3.14
- Pandas (data processing)
- Matplotlib & Seaborn (visualization)
- ReportLab (PDF generation)

---

## 📚 Documentation

- `PROJECT_SUMMARY.md` - Chinese project overview
- `PROJECT_SUMMARY_EN.md` - English project overview
- `LOTTERY_ODDS_EXPLAINED.md` - Lottery odds explanation

---

## 🔗 Links

**GitHub:** https://github.com/siren7075/powerball-study  
**Data Source:** Official NY State Powerball Records  
**Analysis Date:** July 2026

---

## 📝 License & Attribution

Data science study and web application for educational purposes.

*A data-driven exploration of Powerball lottery patterns with an interactive number generation tool.*
