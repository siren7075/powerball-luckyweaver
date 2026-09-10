# LuckyWeaver - Local Version

Intelligent Powerball number generator with probability weighting. Run locally on your machine.

## Quick Start

### macOS / Linux

```bash
git clone https://github.com/siren7075/luckyweaver.git
cd luckyweaver
chmod +x run.sh
./run.sh
```

Then open: http://localhost:5001

### Windows

```bash
git clone https://github.com/siren7075/luckyweaver.git
cd luckyweaver
run.bat
```

Then open: http://localhost:5001

## Manual Setup

If you prefer manual setup:

```bash
# Create virtual environment
python3 -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
python3 app.py
```

## How to Use

1. Open http://localhost:5001 in your browser
2. Choose language from top-right buttons
3. Set decay strength (0-100%)
4. Set number of sets to generate (1-20)
5. Click Generate
6. View results

## Settings Explained

Decay Strength controls how much recently drawn numbers are reduced:
- 0% = completely random selection
- 50% = balanced approach
- 100% = avoid all recent numbers

Higher values avoid numbers that appeared in the last 5 draws.

## Update Data

To get latest Powerball draws:

```bash
python3 download_latest_data.py
```

This updates the data file with new draws automatically.

## File Structure

```
luckyweaver/
├── app.py                    Main application
├── powerball_generator.py    Algorithm
├── download_latest_data.py   Data update tool
├── requirements.txt          Dependencies
├── data/
│   └── powerball_clean.csv   Historical data
├── templates/
│   └── index.html            Web interface
├── run.sh                     Launch script (macOS/Linux)
└── run.bat                    Launch script (Windows)
```

## Languages Supported

- English
- Spanish (Español)
- Portuguese (Português)
- French (Français)
- Chinese (中文)

## Requirements

- Python 3.8 or higher
- Internet connection (first run only to validate)
- 100 MB disk space

## Stopping

Press Ctrl+C in the terminal to stop the application.

## Troubleshooting

Port 5001 in use?
- Edit app.py line 26, change port number
- Or stop whatever is using port 5001

Dependencies missing?
```bash
pip install -r requirements.txt --upgrade
```

Data too old?
```bash
python3 download_latest_data.py
```

## Documentation

- INSTALL.md - Detailed installation
- FEATURES.md - Feature list
- QUICKSTART.md - Quick start examples
- DATA_UPDATE.md - Data management
- DATA_SOURCES.md - Where to get data
- BRAND.md - Brand information

## Disclaimer

LuckyWeaver is for entertainment and education only. Lottery results are random and unpredictable. Not a gambling aid or prediction tool.

## Support

Issues? Check the documentation files or visit:
https://github.com/siren7075/luckyweaver

---

Enjoy exploring Powerball patterns locally!
