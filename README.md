# 🎰 Powerball Rolling Window Overlap Analysis

A data science study analyzing white ball number overlap patterns across consecutive Powerball lottery drawings.

## Project Overview

This project examines how white ball numbers repeat when looking at rolling windows of 2-10 consecutive drawings. Rather than focusing on a single phenomenon, we construct an empirical probability matrix showing the distribution of overlaps across different time horizons.

**Research Question**: How do white ball numbers repeat across consecutive drawing windows of different sizes?

## Dataset

- **Source**: Official New York State Powerball Lottery Records
- **Time Period**: January 2010 - July 2026
- **Total Drawings**: 1,967
- **Data Quality**: No duplicates found, fully cleaned and validated

## Current Study: Rolling Window Overlap Analysis

We analyze rolling windows of sizes 2 through 10 consecutive drawings to determine:

- **Average overlaps** - Mean number of repeated white balls per window
- **Distribution** - Probability of 0, 1, 2, 3... repeated numbers
- **Statistics** - Median, min, max, and standard deviation for each window size

### Key Findings

| Window Size | Mean Overlaps | Median | Min | Max |
|-------------|---------------|--------|-----|-----|
| 2 | 0.38 | 0 | 0 | 3 |
| 5 | 3.30 | 3 | 0 | 8 |
| 10 | 11.39 | 12 | 5 | 18 |

**Observation**: As window size increases, expected overlap increases. This is consistent with probability theory – longer windows have higher likelihood of repeated numbers.

## Repository Structure

```
powerball-study/
├── README.md                                  # This file
├── PROJECT_SUMMARY.md                        # Chinese summary
├── PROJECT_SUMMARY_EN.md                     # English summary
│
├── src/                                       # Python scripts
│   ├── rolling_window_analysis.py            # Main analysis
│   ├── rolling_window_visualizations.py      # Charts and graphs
│   └── generate_report_and_infographic.py    # Report generation
│
├── data/
│   └── powerball_clean.csv                   # Cleaned dataset
│
└── results/                                   # Analysis outputs
    ├── Powerball_Rolling_Overlap_Report.pdf   # Full technical report
    ├── Powerball_Rolling_Overlap_Summary.png  # Infographic
    ├── rolling_window_heatmap.png            # Probability heatmap
    ├── rolling_window_statistics.png         # Statistics chart
    ├── rolling_window_summary_table.png      # Summary table
    ├── rolling_window_matrix.csv             # Empirical probabilities
    └── rolling_window_results.json           # Raw results
```

## Main Outputs

- **PDF Report** (`Powerball_Rolling_Overlap_Report.pdf`) - Comprehensive technical report with all visualizations
- **Infographic** (`Powerball_Rolling_Overlap_Summary.png`) - Single-page visual summary
- **Probability Matrix** (`rolling_window_matrix.csv`) - Empirical probability data
- **Visualizations** - Heatmap, statistics chart, and summary table (high-resolution PNG)

## Running the Analysis

```bash
# Clone repository
git clone https://github.com/siren7075/powerball-study.git
cd powerball-study

# Set up environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run analysis
python3 src/rolling_window_analysis.py          # Compute statistics
python3 src/rolling_window_visualizations.py    # Generate charts
python3 src/generate_report_and_infographic.py  # Create report & infographic
```

## Important Notes

⚠️ **This is a descriptive statistical analysis**
- **No predictive claims** - Historical patterns do not predict future outcomes
- **No strategy recommendations** - Study cannot be used to improve lottery odds
- **Empirical only** - Results describe observed historical distributions
- **Lottery is random** - Outcomes remain inherently unpredictable

This study is for educational and analytical purposes only.

## Future Work

Potential extensions:
- Analysis of Powerball (red ball) patterns
- Time-series analysis of drawing patterns
- Comparison with theoretical random distributions
- Geographic analysis if state-level data becomes available

## Tools & Technologies

- **Python 3.14** - Core language
- **Pandas** - Data processing
- **Matplotlib & Seaborn** - Visualization
- **ReportLab** - PDF generation

## Author & Repository

**GitHub**: https://github.com/siren7075/powerball-study (Private)  
**Analysis Date**: July 2026  
**Data Source**: Official NY State Powerball Records

---

*A focused statistical study of historical Powerball lottery data.*
