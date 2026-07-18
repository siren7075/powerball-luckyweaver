# Powerball Study

Analysis of New York State Powerball lottery drawings (2010-present).

## Study 1: Duplicate Drawing Analysis

This study determines whether there has ever been an identical Powerball drawing in history.

### Results
See `results/study1_results.txt` and visualizations in `results/`.

### Data
- Source: Official New York State Powerball dataset
- Format: Draw Date, Winning Numbers (5 white balls + 1 Powerball)
- Processing: Data cleaned and standardized in `data/powerball_clean.csv`

### Scripts
- `src/data_cleaner.py` - Data cleaning and preprocessing
- `src/study1_analysis.py` - Duplicate drawing analysis
- `src/visualizations.py` - Generate plots and charts
