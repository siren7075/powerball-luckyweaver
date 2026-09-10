# LuckyWeaver - Local Installation Guide

## System Requirements

- Python 3.8 or higher
- 100 MB disk space
- macOS, Linux, or Windows

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/siren7075/luckyweaver.git
cd luckyweaver
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

Activate it:
- macOS/Linux: `source venv/bin/activate`
- Windows: `venv\Scripts\activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python3 app.py
```

Open browser: http://localhost:5001

## Usage

### Basic Usage

1. Select language (top right)
2. Adjust decay strength slider (0-100%)
3. Set number of sets to generate (1-20)
4. Click "Generate"
5. View results and statistics

### Update Data

Keep dataset current with latest drawings:

```bash
python3 download_latest_data.py
```

This merges new draws with existing data automatically.

## Stopping the Application

Press Ctrl+C in terminal

## Troubleshooting

### Port Already in Use

Edit `app.py` line 26:
```python
app.run(debug=True, port=5002)  # Change to different port
```

### Python Not Found

Ensure Python 3.8+ is installed:
```bash
python3 --version
```

### Module Not Found Error

Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Still Having Issues

Check the logs:
```bash
cat /tmp/flask_app.log
```

## Project Structure

```
luckyweaver/
├── app.py                    # Main Flask application
├── powerball_generator.py    # Number generation logic
├── download_latest_data.py   # Data update tool
├── requirements.txt          # Python dependencies
├── data/
│   └── powerball_clean.csv   # Historical draw data
├── templates/
│   └── index.html            # Web interface
└── README.md                 # Documentation
```

## Files You Can Customize

- `templates/index.html` - UI design and layout
- `powerball_generator.py` - Generation algorithm
- `app.py` - Server configuration
- `data/powerball_clean.csv` - Dataset

## Next Steps

1. Run the application locally
2. Explore different decay strengths
3. Try generating different numbers of sets
4. Read FEATURES.md for advanced usage
5. Check DATA_SOURCES.md for updating data

## Support

For issues or questions:
- Check existing documentation
- Review QUICKSTART.md
- See DATA_UPDATE.md for data questions
- Visit github.com/siren7075/luckyweaver

---

Enjoy using LuckyWeaver locally!
