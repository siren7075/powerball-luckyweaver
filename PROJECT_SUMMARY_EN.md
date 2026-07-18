# 🎰 Powerball Rolling Window Overlap Analysis - Project Summary

## Project Overview

This project is a comprehensive statistical analysis study of official New York State Powerball lottery data. By analyzing 1,967 lottery drawings from 2010 to 2026, we explore the overlap patterns of white ball numbers across consecutive draws.

The core research method uses **rolling window analysis**. Rather than examining only adjacent pairs of drawings, we extend the analysis to 2-10 consecutive drawing windows, constructing a complete empirical probability matrix.

## Dataset

- **Source**: Official New York State Powerball Lottery Records
- **Time Period**: January 2010 - July 2026
- **Sample Size**: 1,967 drawings
- **Data Quality**: Verified duplicate-free, fully cleaned and standardized

### Data Validation

✅ **Data Cleaning Completed**
- Total Drawings: 1,967
- Duplicate Drawings: 0
- Duplicate Rate: 0.0%
- Data Quality: Verified

## Primary Study: Rolling Window Overlap Analysis

### Research Methodology

For each window size (2 to 10 consecutive drawings), we calculate:

- **Average Overlaps** - Mean number of repeated white balls per window
- **Max/Min Overlaps** - Maximum and minimum overlap numbers
- **Median** - Median of overlap distribution
- **Standard Deviation** - Measure of data dispersion
- **Probability Distribution** - Probabilities of observing 0, 1, 2, 3... overlaps

### Key Findings

#### Summary Statistics Table

| Window Size | Mean Overlaps | Median | Min | Max | Std Dev |
|-------------|---------------|--------|-----|-----|---------|
| 2 | 0.38 | 0 | 0 | 3 | 0.54 |
| 3 | 1.08 | 1 | 0 | 5 | 1.06 |
| 4 | 2.08 | 2 | 0 | 6 | 1.47 |
| 5 | 3.30 | 3 | 0 | 8 | 1.80 |
| 6 | 4.70 | 5 | 0 | 9 | 2.00 |
| 7 | 6.24 | 6 | 2 | 12 | 2.09 |
| 8 | 7.88 | 8 | 2 | 14 | 2.14 |
| 9 | 9.61 | 10 | 4 | 16 | 2.13 |
| 10 | 11.39 | 12 | 5 | 18 | 2.14 |

#### Critical Observations

**Larger Windows Show More Overlaps**

- Window Size 2: Average 0.38 overlapping numbers
- Window Size 10: Average 11.39 overlapping numbers

This aligns with probability theory expectations – larger windows have more opportunities for number repetition.

**Distribution Shifts with Window Size**

- Small Windows (2-3): Distribution concentrated on low overlap counts
- Medium Windows (5-7): Distribution centered in the middle
- Large Windows (8-10): Broader distribution, skewed toward high overlaps

### Probability Matrix

A complete empirical probability matrix is generated in CSV format:

```
Window Size | Overlap 0 | Overlap 1 | Overlap 2 | Overlap 3 | ... | Overlap 18
------------|-----------|-----------|-----------|-----------|-----|----------
2           | 65.82%    | 30.32%    | 3.71%     | 0.15%     |     |
3           | 28.35%    | 42.19%    | 23.16%    | 5.75%     |     |
...         | ...       | ...       | ...       | ...       | ... |
10          | 0.00%     | 0.00%     | 0.00%     | 0.00%     |     | 0.20%
```

## Visualization Analysis

### 1. Probability Heatmap
Displays the probability distribution across all window sizes and overlap counts.
- X-axis: Number of overlapping white balls
- Y-axis: Window size
- Color intensity: Probability percentage

### 2. Statistics Comparison Chart
Compares mean, median, and standard deviation across window sizes.
- Clear trend visualization
- Shows increasing statistics with window size

### 3. Summary Table
A comprehensive table of key statistics for all window sizes.
- Easy reference and comparison
- Precise numerical values

### 4. Infographic
Single-page vertical infographic including:
- Project title and dataset information
- Heatmap and key charts
- Important findings and conclusions
- Modern, minimal design suitable for GitHub/Medium/LinkedIn

## Reports and Outputs

### PDF Report
Complete technical report: `Powerball_Rolling_Overlap_Report.pdf` includes:
- Project overview and background
- Dataset description
- Detailed methodology
- Complete probability matrix
- All visualizations
- In-depth analysis and interpretation
- Limitations and disclaimers

### Data Files
- `rolling_window_matrix.csv` - Complete probability matrix
- `rolling_window_results.json` - Raw statistical results

## Project Structure

```
powerball-study/
├── README.md                          # Project documentation
├── PROJECT_SUMMARY.md                 # Chinese summary
├── PROJECT_SUMMARY_EN.md              # English summary (this file)
│
├── src/                               # Python analysis scripts
│   ├── rolling_window_analysis.py     # Main analysis
│   ├── rolling_window_visualizations.py  # Chart generation
│   └── generate_report_and_infographic.py # Report generation
│
├── data/
│   └── powerball_clean.csv            # Cleaned dataset
│
└── results/                           # Analysis outputs
    ├── Powerball_Rolling_Overlap_Report.pdf  # PDF report
    ├── Powerball_Rolling_Overlap_Summary.png # Infographic
    ├── rolling_window_heatmap.png    # Probability heatmap
    ├── rolling_window_statistics.png # Statistics chart
    ├── rolling_window_summary_table.png # Summary table
    ├── rolling_window_matrix.csv     # Probability matrix (CSV)
    └── rolling_window_results.json   # Raw results (JSON)
```

## Usage Instructions

### Reproduce the Analysis

```bash
# Clone repository
git clone https://github.com/siren7075/powerball-study.git
cd powerball-study

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run analysis pipeline
python3 src/rolling_window_analysis.py          # Compute statistics
python3 src/rolling_window_visualizations.py    # Generate charts
python3 src/generate_report_and_infographic.py  # Generate reports
```

## Methodology

### Rolling Window Analysis

For each window size (2 to 10):

1. Extract all possible consecutive N-drawing windows from the dataset
2. For each window, count how many white ball numbers appear 2+ times
3. Collect all overlap counts
4. Calculate mean, median, min, max, and standard deviation
5. Build probability distribution (frequency and probability of each overlap count)
6. Assemble final probability matrix

### Tools Used

- **Python 3.14** - Core programming language
- **Pandas** - Data processing and analysis
- **Matplotlib & Seaborn** - Data visualization
- **ReportLab** - PDF report generation
- **Pillow** - Image processing

## Key Interpretations

### Why Do Larger Windows Show More Overlaps?

This is a fundamental probability phenomenon. In 5 consecutive draws (5 numbers each), there are 25 number slots; in 10 consecutive draws, there are 50 slots. More slots mean higher probability of number repetition.

### What Does This Mean?

- This describes **historical patterns**
- Reflects the **empirical distribution** of the past 16 years
- **Cannot be used for prediction** of future drawings
- **Cannot improve** winning odds

### Important Warning

⚠️ **This is historical analysis, not prediction**
- Past overlap patterns do not predict future outcomes
- Lottery mechanism may change at any time
- Results are specific to the 2010-2026 period
- Lottery outcomes are inherently random and unpredictable

## Limitations

1. **Time-Specific** - Analysis based on 2010-2026 data only
2. **Mechanism Changes** - Lottery rules may change in the future
3. **No Predictive Value** - Cannot be used to predict future drawings
4. **Sample Size** - 1,967 draws are substantial but still small in the full probability space

## Conclusions

This study provides a complete statistical description of white ball overlap patterns in historical Powerball lottery data. Through rolling window analysis, we clearly demonstrate the distribution of number overlaps across different time horizons.

**Core Finding**: Larger window sizes show more average overlaps, which is entirely consistent with probability theory expectations.

**Most Important Takeaway**: This describes historical data and cannot be used for prediction or to improve odds.

## Related Resources

- Official NY State Lottery: https://nylottery.ny.gov/
- Powerball Official Website: https://www.powerball.com/
- GitHub Repository: https://github.com/siren7075/powerball-study

---

**Project Information**
- Creation Date: July 2026
- Data Through: July 15, 2026
- Analysis Tools: Python, Pandas, Matplotlib, ReportLab
- Repository: https://github.com/siren7075/powerball-study (Private)

**Last Updated**: July 17, 2026

*Data tells stories, but the story here is understanding the randomness of the data.* 📊
