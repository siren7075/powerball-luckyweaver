# Powerball-LuckyWeaver: Intelligent Powerball Number Generator

Transform lottery selection into an intelligent probability exploration. LuckyWeaver generates Powerball numbers using decay-based probability weighting and personalized lucky number algorithms — no predictions, just data-driven patterns from 16+ years of real draws.

## Quick Start

```bash
source app_venv/bin/activate  # Windows: venv\Scripts\activate
python3 app.py
```

Then open http://localhost:5001 in your browser.

**What you get immediately:**
- Multilingal interactive UI (5 languages)
- Decay weighting: reduce probability of recently drawn numbers
- Lucky numbers: assign custom weights to your favorite numbers (0.5x - 2.5x)
- Batch generation: 1-20 combinations at once
- Built on 1,967+ historical Powerball draws (2010-2026)

---

## What is Powerball-LuckyWeaver?

An interactive tool for exploring lottery number patterns using two complementary algorithms:

1. **Decay Weighting** - Probability gradually decreases for recently drawn numbers (configurable strength 0-100%)
2. **Lucky Numbers** - Personalize your combinations by weighting your favorite numbers

This is not a prediction system — lottery drawings are random and independent. Instead, LuckyWeaver lets you explore probability patterns, learn about statistical weighting, and generate combinations based on historical trends and personal preference.

## Core Features

**Lucky Numbers Weighting**
- Choose your own lucky numbers (1-69 for white balls, 1-26 for red)
- Assign custom multipliers (0.5x - 2.5x)
- Combine with decay weighting for layered customization
- Browser storage keeps your preferences persistent

**Smart Generation Algorithms**
- Decay weighting: Recent numbers get graduated probability reduction
- Configurable strength (0-100%) from fully random to strong avoidance
- Batch generation: 1-20 combinations at once

**Multilingual Interface**
- English, Español, Português, Français, 中文
- Instant language switching with saved preference
- All UI text, buttons, labels translated

**Analysis Dashboard**
- Period-based weight visualization showing how patterns shift
- Recent draw statistics and frequency analysis
- Historical breakdowns across 16+ years

---

## Installation (Full Setup)

```bash
git clone https://github.com/siren7075/powerball-luckyweaver.git
cd powerball-luckyweaver
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open http://localhost:5001

For Windows, use `venv\Scripts\activate` instead.

---

## Project Structure

### Web Application
- **`app.py`** - Flask server (runs on localhost:5001)
- **`templates/index.html`** - Interactive frontend with multilingual UI
- **`powerball_generator.py`** - Core number generation algorithms
- **`requirements.txt`** - Python dependencies

### Research & Analysis
All analysis code lives in `src/`:
- **`study1_analysis.py`** - Initial historical patterns analysis
- **`study2_overlap_analysis.py`** - Number overlap and frequency patterns
- **`study3_number_patterns.py`** - Position-specific pattern analysis
- **`rolling_window_analysis.py`** - Time-series trend analysis
- **`lottery_odds_analysis.py`** - Statistical odds calculations
- **`advanced_odds_analysis.py`** - Complex probability models
- **`visualizations.py` & `visualizations_extended.py`** - Chart generation
- **`data_cleaner.py`** - Data validation and cleaning utilities

### Data & Results
- **`data/`** - Historical Powerball draws (CSV format)
- **`results/`** - Generated analysis outputs
  - `visualizations/` - Charts and graphs
  - `reports/` - Statistical reports

### Documentation
See the guides below for deep dives on specific topics.

---

## How the Algorithms Work

### Two-Layer Weighting System

Powerball-LuckyWeaver combines two algorithms for maximum customization:

**1. Decay Algorithm** (Always Active)

Instead of purely random selection, applies intelligent probability weighting:

**Example:** With 60% decay strength
- **Period 5** (most recent) → 100% weight reduction
- **Period 4** → 80% weight reduction  
- **Period 3** → 60% weight reduction
- **Period 2** → 40% weight reduction
- **Period 1** (oldest) → 20% weight reduction

This creates a **gradual probability curve** rather than hard avoidance, resulting in more natural number distributions.

**2. Lucky Numbers Algorithm** (Optional)

Layer custom weights on top of decay weighting:

- **Select lucky numbers** from 1-69 (white) and 1-26 (red)
- **Assign multipliers**: 0.5x (less likely) to 2.5x (more likely)
- **Control strength**: Global multiplier (0-2.0x) affects how much lucky weights influence results

**Example:** If you set lucky number 7 to 1.5x with strength 1.0x:
- Without decay: 7 has 1.5× normal probability
- Combined with decay: Effect compounds for sophisticated weighting

---

## Documentation Guides

**Project Overview**
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Complete map: where code, analysis, data, and results live
- **[PROJECT_SUMMARY_EN.md](PROJECT_SUMMARY_EN.md)** - Detailed project overview

**Getting Started**
- **[QUICKSTART.md](QUICKSTART.md)** - 30-second setup with working examples

**Features & API**
- **[FEATURES.md](FEATURES.md)** - Complete feature breakdown with API endpoints
- **[STEERING_LUCKY_WEIGHTS.md](STEERING_LUCKY_WEIGHTS.md)** - Lucky numbers feature design and roadmap

**Data Management**
- **[DATA_UPDATE.md](DATA_UPDATE.md)** - How to keep your dataset current (Powerball draws 3x/week)
- **[DATA_SOURCES.md](DATA_SOURCES.md)** - Where and how we fetch Powerball data
- **[LOTTERY_ODDS_EXPLAINED.md](LOTTERY_ODDS_EXPLAINED.md)** - Probability theory behind the numbers

**Localized**
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Portuguese summary

---

## Languages Supported

English • Español • Português • Français • 中文

All UI text, buttons, labels, and help fully translated. Switch languages instantly in the app; preference is saved.

---

## Tech Stack

**Frontend**
- HTML5 / CSS3 (vanilla, no frameworks)
- JavaScript with i18n support (zero external dependencies)
- Responsive gradient design with smooth animations

**Backend**
- Python 3.8+
- Flask (lightweight HTTP server)
- NumPy (fast probability calculations)
- Pandas (data cleaning and analysis)

**Data**
- 1,967+ historical Powerball draws (2010-2026)
- Cleaned and validated
- CSV format for easy updates

---

## Use Cases

**For Fun:** Generate combinations based on probability patterns. Experiment with decay strength and watch how distributions shift.

**For Learning:** Study probability theory, statistical weighting algorithms, and pattern analysis using 16+ years of real lottery data. Ideal for students and data enthusiasts.

**For Research:** Analyze historical draws, test hypotheses about number distributions, and understand frequency patterns across multiple timeframes.

---

## API Reference

**POST /api/generate** - Generate number combinations

```json
{
  "weight_strength": 0.6,
  "periods": 5,
  "count": 5
}
```

Returns array of number sets with recent draw history.

**GET /api/latest** - Get the most recent Powerball draw

```json
{
  "date": "2026-07-15",
  "white": [2, 7, 18, 29, 38],
  "red": 16
}
```

See [FEATURES.md](FEATURES.md) for complete API documentation.

---

## Keeping Data Current

Powerball draws 3 times per week (Mon, Wed, Sat). Update your dataset:

```bash
python3 download_latest_data.py
```

Or schedule automatic updates with cron:
```bash
# Every Saturday at 11 PM
0 23 * * 6 cd /path/to/luckyweaver && python3 download_latest_data.py
```

Full instructions in [DATA_UPDATE.md](DATA_UPDATE.md).

---

## Important Disclaimer

**For entertainment and educational use only.**

- Lottery drawings are random and independent — no predictive power
- Statistical patterns do not guarantee future outcomes
- This tool is for fun exploration and learning, not gambling advice
- Each drawing starts fresh with equal probability for all numbers

Play responsibly. Never wager more than you can afford to lose.

---

## Why LuckyWeaver?

- **Intelligent Algorithms** — Decay weighting and personalized lucky numbers, not random
- **Interactive & Real-Time** — Instant generation with responsive UI
- **Multilingual** — 5 languages built in
- **Data-Driven** — 1,967+ historical draws for analysis
- **Transparent** — Open source, all algorithms visible
- **Customizable** — Adjust strength, batch size, language, UI
- **Educational** — Learn probability and statistics with real data
- **Fast** — NumPy-optimized for instant results

---

## Contributing

Found a bug or have a feature idea?

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your fork
5. Submit a pull request

---

## Resources

- [Powerball Official](https://www.powerball.com/)
- [How to Play](https://www.powerball.com/how-to-play)
- [Historical Data Source](https://nylottery.ny.gov/)
- [Probability Theory](https://en.wikipedia.org/wiki/Probability_theory)

---

## License

Open source for educational and entertainment purposes.

---

## Next Steps

- **Understand the project layout?** Read [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)
- **New to the project?** Start with [QUICKSTART.md](QUICKSTART.md)
- **Want full features reference?** See [FEATURES.md](FEATURES.md)
- **Need data info?** Check [DATA_SOURCES.md](DATA_SOURCES.md)
- **Curious about the research?** Explore analysis code in `src/`

---

**Latest:** Version with data download tools  
**Last Updated:** September 2026  
**Status:** Active and maintained

Weave probability patterns into possibility. For lottery enthusiasts, data scientists, and probability explorers.
