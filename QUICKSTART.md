# ⚡ Quick Start Guide

## 30-Second Setup

```bash
git clone https://github.com/siren7075/powerball-study.git
cd powerball-study
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open browser → **http://localhost:5001** ✅

---

## First Run

### Step 1: Choose Language
Click **"English"** or **"中文"** in top right

### Step 2: Adjust Settings
- **Decay Strength**: Slider (0-100%)
  - 0% = totally random
  - 60% = balanced (default)
  - 100% = avoid recent numbers completely

- **Generate Sets**: Input (1-20)
  - Enter `5` to get 5 lottery tickets
  - Enter `10` for 10 different combinations

### Step 3: Generate!
Click **"🎲 Generate"** button

### Step 4: Review Results
- See your recommended number sets
- Check the "Recent Period Analysis" table
- Understand how weights decay over time
- View statistics on recent numbers

---

## Examples

### Example 1: Single Conservative Set
1. Decay Strength = 80% (strong avoidance)
2. Generate Sets = 1
3. Click Generate
4. Get one conservative combination

### Example 2: Multiple Options
1. Decay Strength = 50% (balanced)
2. Generate Sets = 10
3. Click Generate
4. Pick your favorites from 10 options

### Example 3: Analysis Mode
1. Decay Strength = 0% (random baseline)
2. Generate Sets = 100
3. Use for data analysis
4. See what pure random looks like

---

## Understanding the Results

### Number Combo Display
```
[2, 15, 27, 33, 69] + 18
 └────────┬─────────┘   └─┘
 White balls (5)         Red ball (1)
```

### Period Analysis Table
| Period | Date | Weight |
|--------|------|--------|
| 5 | 2026-07-15 | 100% |
| 4 | 2026-07-13 | 80% |
| 3 | 2026-07-11 | 60% |
| 2 | 2026-07-08 | 40% |
| 1 | 2026-07-06 | 20% |

**Higher weight = Stronger penalty for those numbers**

---

## Common Questions

### Q: What does "decay strength" mean?
**A:** It reduces the chance of recent numbers appearing:
- 0% → Recent numbers have normal probability
- 60% → Recent numbers have 60% reduced probability
- 100% → Recent numbers cannot appear

### Q: Why should I generate multiple sets?
**A:** See different combinations and pick the best ones for your play style.

### Q: Is this better than random selection?
**A:** No - lottery is random. This is just a fun strategy for variety.

### Q: Can I run this offline?
**A:** Yes! After setup, run `python3 app.py` anytime without internet.

### Q: Can I modify the code?
**A:** Absolutely! Fork the repo and customize:
- `powerball_generator.py` - Change algorithm
- `templates/index.html` - Change UI design
- `app.py` - Add new features

---

## Troubleshooting

### Port 5001 in use?
Edit `app.py` line 26:
```python
app.run(debug=True, port=5002)  # Change to 5002, 5003, etc.
```

### Python version issues?
Ensure Python 3.8+:
```bash
python3 --version
```

### Module not found errors?
Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Still having issues?
Check Flask logs or submit an issue on GitHub!

---

## Next Steps

1. ✅ **Generated your first numbers?** → Try different settings
2. 📊 **Want to analyze data?** → Check `src/` folder for analysis scripts
3. 🎨 **Want to customize UI?** → Edit `templates/index.html`
4. ⭐ **Enjoying this?** → Star the repo on GitHub!

---

**Happy ticket generating! 🎉**

*Remember: Results are for entertainment. Lottery outcomes are random and unpredictable.*
