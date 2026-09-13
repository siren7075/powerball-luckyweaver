# Project Structure Guide

A complete map of where everything lives in Powerball-LuckyWeaver.

## Quick Navigation

| What | Where | Purpose |
|------|-------|---------|
| Run the app | `python3 app.py` → http://localhost:5001 | Interactive web interface |
| Analysis code | `src/` | Historical pattern research and data analysis |
| Generated results | `results/` | Visualizations, reports, analysis outputs |
| Raw data | `data/` | Powerball historical draws (CSV) |
| Web frontend | `templates/index.html` | Multilingual UI with generation controls |
| Main algorithms | `powerball_generator.py` | Decay weighting and number generation logic |

---

## Directory Structure

```
powerball-study/
├── app.py                          # Flask server (starts web app)
├── powerball_generator.py          # Core algorithms: decay + lucky numbers
├── requirements.txt                # Python dependencies
├── run.sh / run.bat               # Quick-start scripts
│
├── templates/
│   └── index.html                 # Full interactive web interface
│
├── src/                           # Analysis & Research Code
│   ├── study1_analysis.py         # Historical pattern analysis
│   ├── study2_overlap_analysis.py # Number overlap patterns
│   ├── study3_number_patterns.py  # Position-specific patterns
│   ├── rolling_window_analysis.py # Time-series trends
│   ├── lottery_odds_analysis.py   # Probability calculations
│   ├── advanced_odds_analysis.py  # Complex statistical models
│   ├── visualizations.py          # Chart generation
│   ├── visualizations_extended.py # Extended visualizations
│   ├── data_cleaner.py            # Data validation
│   ├── generate_report_and_infographic.py
│   ├── comprehensive_report.py
│   └── generate_enhanced_reports.py
│
├── data/                          # Raw & Processed Data
│   └── powerball_draws.csv        # 1,967+ historical draws
│
├── results/                       # Analysis Output
│   ├── data/                      # Processed datasets
│   ├── visualizations/            # Generated charts & graphs
│   └── reports/                   # Statistical reports
│
├── Documentation
│   ├── README.md                  # (You are here)
│   ├── QUICKSTART.md              # 30-second setup guide
│   ├── FEATURES.md                # Complete feature reference
│   ├── STEERING_LUCKY_WEIGHTS.md  # Lucky numbers design doc
│   ├── DATA_UPDATE.md             # How to keep data fresh
│   ├── DATA_SOURCES.md            # Data source documentation
│   ├── LOTTERY_ODDS_EXPLAINED.md  # Probability primer
│   ├── PROJECT_SUMMARY.md         # Portuguese overview
│   └── PROJECT_SUMMARY_EN.md      # English detailed summary
│
└── Virtual Environments
    ├── venv/                      # Development environment
    └── app_venv/                  # Application environment
```

---

## What's Where: Quick Reference

### Web Application (Interactive Tool)

The heart of the project. Run this to generate Powerball numbers.

**File: `app.py`**
- Flask HTTP server
- Default port: 5001
- Serves the interactive UI

**File: `templates/index.html`**
- Full web interface
- Multilingual UI (5 languages)
- Lucky numbers selector
- Generation controls
- Results display with statistics

**File: `powerball_generator.py`**
- Contains the two main algorithms:
  - Decay weighting: Reduces recently drawn numbers
  - Lucky numbers: Custom number weights (0.5x - 2.5x multipliers)
- Called by the Flask API
- NumPy-optimized for speed

**How they work together:**
```
User visits http://localhost:5001
    ↓
Flask (app.py) serves index.html
    ↓
User clicks "Generate" with settings
    ↓
JavaScript sends /api/generate request
    ↓
powerball_generator.py runs the algorithm
    ↓
Results displayed with recent draw data
```

---

### Research & Analysis Code

Deep-dive statistical explorations of Powerball patterns. Located in `src/`.

**Core Analysis Files:**

| File | What It Does |
|------|-------------|
| `study1_analysis.py` | Initial historical pattern discovery |
| `study2_overlap_analysis.py` | Analyzes which numbers appear together frequently |
| `study3_number_patterns.py` | Position-specific patterns (first white ball, etc.) |
| `rolling_window_analysis.py` | Trend analysis over time windows (30 days, 6 months, etc.) |
| `lottery_odds_analysis.py` | Probability calculations and odds breakdown |
| `advanced_odds_analysis.py` | Complex statistical models and correlations |

**Utility & Visualization:**

| File | What It Does |
|------|-------------|
| `data_cleaner.py` | Validates, cleans, and normalizes raw Powerball data |
| `visualizations.py` | Generates core charts (frequency, trends, distributions) |
| `visualizations_extended.py` | Advanced visualization suite |
| `generate_report_and_infographic.py` | Creates PDF/image reports |
| `comprehensive_report.py` | Full statistical summaries |
| `generate_enhanced_reports.py` | Enhanced report generation |

**Running analysis:**
```bash
# Example: Run study 1
python3 src/study1_analysis.py

# Run rolling window analysis
python3 src/rolling_window_analysis.py

# Generate visualizations
python3 src/visualizations.py
```

Output goes to `results/` (visualizations, data, reports).

---

### Data Layers

**Input: `data/`**
- `powerball_draws.csv` — Raw historical data (1,967+ draws from 2010-2026)
- One row per draw with date, white balls, red ball

**Processing: `src/data_cleaner.py`**
- Validates dates
- Handles missing values
- Normalizes number ranges
- Outputs cleaned data

**Output: `results/data/`**
- Processed datasets created by analysis scripts
- Intermediate files for calculations
- Cleaned subsets for specific studies

**Keeping it fresh:**
```bash
# Update with latest draws (Powerball: 3x/week)
python3 download_latest_data.py

# Or schedule with cron
0 23 * * 6 cd /path/to/luckyweaver && python3 download_latest_data.py
```

See [DATA_UPDATE.md](DATA_UPDATE.md) for details.

---

### Generated Results

**Location: `results/`**

**Visualizations** (`results/visualizations/`)
- Frequency distribution charts
- Time-series trend plots
- Heatmaps of number patterns
- Period-based weight visualizations
- Position-specific analysis charts

**Reports** (`results/reports/`)
- Statistical summaries
- Pattern analysis reports
- Odds breakdowns
- PDF/image exports

**Data** (`results/data/`)
- Intermediate processed datasets
- Study-specific subsets
- Aggregated statistics

These are generated by the analysis scripts:
```bash
python3 src/visualizations.py       # Creates all charts
python3 src/comprehensive_report.py # Creates reports
```

---

## Workflow: From Raw Data to Generated Numbers

```
Historical Data (data/powerball_draws.csv)
    ↓
[data_cleaner.py validates & normalizes]
    ↓
Analysis Pipeline (src/)
    ├─ study1_analysis.py
    ├─ study2_overlap_analysis.py
    ├─ study3_number_patterns.py
    ├─ rolling_window_analysis.py
    └─ lottery_odds_analysis.py
    ↓
Results (results/)
    ├─ visualizations/ (charts & graphs)
    ├─ reports/ (statistical summaries)
    └─ data/ (processed datasets)
    ↓
[powerball_generator.py uses decay patterns]
    ↓
Web App (app.py + index.html)
    ↓
User generates numbers with custom weights
    ↓
Live generation with statistics
```

---

## Key Files at a Glance

**To understand the algorithms:**
- Start with `powerball_generator.py` (core logic)
- Then read [FEATURES.md](FEATURES.md) (algorithm explanation)

**To see the research:**
- Start with `src/study1_analysis.py` (initial patterns)
- Check `results/visualizations/` for outputs

**To run the web app:**
- `python3 app.py` then http://localhost:5001

**To update data:**
- `python3 download_latest_data.py`

**To explore analysis:**
- Any file in `src/` can be run independently
- Check `results/` for generated outputs

---

## Development Environments

**app_venv/** (Application)
- Used when running `app.py`
- Install with `pip install -r requirements.txt`

**venv/** (Development)
- Alternative environment
- Same dependencies

**Activate on Mac/Linux:**
```bash
source app_venv/bin/activate
```

**Activate on Windows:**
```bash
app_venv\Scripts\activate
```

---

## File Dependencies

```
app.py
  ├── powerball_generator.py (number generation)
  ├── data/powerball_draws.csv (historical data)
  └── templates/index.html (web interface)

src/study1_analysis.py
  └── data/powerball_draws.csv

src/data_cleaner.py
  └── data/powerball_draws.csv

src/visualizations.py
  └── results/data/ (processed datasets)
```

---

## Running Each Component

**The Web App (interactive generation):**
```bash
python3 app.py
# Visit http://localhost:5001
```

**Individual Analysis:**
```bash
python3 src/study1_analysis.py      # Pattern analysis
python3 src/rolling_window_analysis.py  # Time trends
python3 src/lottery_odds_analysis.py    # Odds calculations
```

**Generate All Visualizations:**
```bash
python3 src/visualizations.py
python3 src/visualizations_extended.py
```

**Create Reports:**
```bash
python3 src/comprehensive_report.py
python3 src/generate_enhanced_reports.py
```

**Update Data:**
```bash
python3 download_latest_data.py
```

---

## Documentation Roadmap

| Want to... | Read... |
|-----------|---------|
| Get running in 30 seconds | [QUICKSTART.md](QUICKSTART.md) |
| Understand all features | [FEATURES.md](FEATURES.md) |
| Learn how decay works | [FEATURES.md](FEATURES.md) + [LOTTERY_ODDS_EXPLAINED.md](LOTTERY_ODDS_EXPLAINED.md) |
| Know about lucky numbers | [STEERING_LUCKY_WEIGHTS.md](STEERING_LUCKY_WEIGHTS.md) |
| Keep data current | [DATA_UPDATE.md](DATA_UPDATE.md) |
| Understand data sources | [DATA_SOURCES.md](DATA_SOURCES.md) |
| Deep project overview | [PROJECT_SUMMARY_EN.md](PROJECT_SUMMARY_EN.md) |

---

## Code Organization Philosophy

- **Small & focused** — Each analysis script has one purpose
- **Reusable utilities** — Common functions in `data_cleaner.py`, `visualizations.py`
- **Lean frontend** — No frameworks, vanilla HTML/CSS/JS
- **Python-based backend** — Flask + NumPy for performance
- **Clear data flow** — Raw → Cleaned → Analyzed → Visualized → Generated

---

Last updated: September 2026
