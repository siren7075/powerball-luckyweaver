# 🎰 Powerball-LuckyWeaver - Intelligent Powerball Number Generator

> **Your lucky numbers meet probability patterns** ✨

An interactive, multilingual Powerball lottery number generator with lucky numbers weighting, decay-based probability analysis, and batch generation capabilities.

**🌟 Quick Start:** 
```bash
source app_venv/bin/activate  # or venv\Scripts\activate on Windows
python3 app.py
# Then visit http://localhost:5001
```

**📊 Data-Driven:** 1,967+ historical Powerball draws (2010-2026)  
**🌍 Multilingual:** English • Español • Português • Français • 中文  
**⚡ Smart Algorithms:** 
- Decay-based probability weighting with adjustable intensity
- Lucky numbers custom weighting (0.5x - 2.5x multipliers)

---

## ✨ What is Powerball-LuckyWeaver?

Powerball-LuckyWeaver is an intelligent number generation tool that combines two powerful features:
1. **Decay Weighting:** Reduces probability of recently drawn numbers
2. **Lucky Numbers:** Select your own lucky numbers and assign custom weights

It's not a prediction tool (lottery is random!), but rather a **fun exploration of probability patterns** based on historical data and your personal preferences.

### Key Features

✨ **Lucky Numbers Weighting**
- Select your own lucky numbers (1-69 for white, 1-26 for red)
- Assign custom weight multipliers (0.5x - 2.5x)
- Combine with decay weighting for powerful customization
- Weights persist in browser storage

🎲 **Smart Generation**
- Decay-based weighting: Recent numbers have higher probability reduction
- Adjustable strength (0-100%) from random to strong avoidance
- Generate 1-20 sets at once for exploration

🌍 **Multilingual Interface**
- English, Spanish, Portuguese, French, Chinese
- Instant language switching
- Saved preference

📊 **Intelligent Analysis**
- Period-based weight visualization
- Recent draw statistics
- Historical pattern breakdown

🎨 **Beautiful UI**
- Gradient design with smooth animations
- Responsive mobile-friendly layout
- Real-time visual feedback

---

## 🚀 Quick Start (30 seconds)

```bash
git clone https://github.com/siren7075/luckyweaver.git
cd luckyweaver
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open browser → **http://localhost:5001** ✨

---

## 🎯 How It Works

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

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **[QUICKSTART.md](QUICKSTART.md)** | 30-second setup guide with examples |
| **[FEATURES.md](FEATURES.md)** | Complete feature breakdown & API docs |
| **[STEERING_LUCKY_WEIGHTS.md](STEERING_LUCKY_WEIGHTS.md)** | Lucky numbers feature design & roadmap |
| **[DATA_UPDATE.md](DATA_UPDATE.md)** | Keep data current with latest draws |
| **[DATA_SOURCES.md](DATA_SOURCES.md)** | How to fetch & update Powerball data |

---

## 🌐 Supported Languages

| Language | Code | Native Name |
|----------|------|-------------|
| 🇬🇧 English | en | English |
| 🇪🇸 Spanish | es | Español |
| 🇵🇹 Portuguese | pt | Português |
| 🇫🇷 French | fr | Français |
| 🇨🇳 Chinese | zh | 中文 |

All UI text, buttons, labels, and help text translated!

---

## 🛠️ Tech Stack

**Frontend:**
- HTML5 / CSS3 (Vanilla, no frameworks)
- JavaScript (i18n support, zero dependencies)
- Responsive gradient design

**Backend:**
- Python 3.8+
- Flask (lightweight web framework)
- NumPy (probability calculations)
- Pandas (data processing)

**Data:**
- 1,967 historical Powerball draws
- Cleaned & validated dataset
- CSV format for easy updates

---

## 📊 Use Cases

### 🎉 For Fun
Generate lottery combinations using intelligent probability analysis. Explore different "decay strengths" and see how patterns change.

### 📚 For Learning
Study probability theory, statistical weighting, and pattern analysis using real lottery data. Great for students and data enthusiasts.

### 🔬 For Research
Analyze historical draws, test weighting hypotheses, and understand pattern distributions across 16+ years of data.

---

## 🎮 API Endpoints

### Generate Numbers
```http
POST /api/generate
Content-Type: application/json

{
  "weight_strength": 0.6,    // 0-1 (0=random, 1=complete avoidance)
  "periods": 5,               // Recent periods to consider
  "count": 5                   // 1-20 sets to generate
}

Response:
{
  "numbers": [
    {"white": [1, 15, 27, 33, 69], "red": 10},
    {"white": [6, 22, 38, 51, 64], "red": 15},
    ...
  ],
  "recent_numbers": [...],
  "recent_white": [2, 5, 7, ...],
  "recent_red": [3, 4, 5, 16, 18]
}
```

### Get Latest Draw
```http
GET /api/latest

Response:
{
  "date": "2026-07-15",
  "white": [2, 7, 18, 29, 38],
  "red": 16
}
```

---

## 📥 Keeping Data Current

Powerball draws **3 times per week** (Mon, Wed, Sat). Keep your dataset fresh:

### Quick Update
```bash
python3 download_latest_data.py
```

### Schedule Automatic Updates
```bash
# Add to crontab (update every Saturday at 11 PM)
0 23 * * 6 cd /path/to/luckyweaver && python3 download_latest_data.py
```

See **[DATA_UPDATE.md](DATA_UPDATE.md)** for full details.

---

## ⚖️ Important Disclaimer

⚠️ **For Entertainment Only**

- ❌ **No predictive power** - Lottery drawings are random and independent
- ❌ **No guaranteed wins** - Statistical patterns don't guarantee future outcomes
- ❌ **Entertainment tool** - LuckyWeaver is for fun exploration, not gambling advice
- ✅ **Educational** - Learn about probability and statistical analysis
- ✅ **Data-driven** - Based on 16+ years of real Powerball history

**Each drawing is a fresh event with equal probability for all numbers.**

Play responsibly. Never gamble more than you can afford to lose.

---

## 🌟 Why LuckyWeaver?

| Feature | Benefit |
|---------|---------|
| **Intelligent** | Decay-based algorithm, not purely random |
| **Interactive** | Real-time generation, beautiful UI |
| **Multilingual** | 5 languages, accessible worldwide |
| **Data-Driven** | 1,967 historical draws for analysis |
| **Open Source** | Full transparency, no hidden algorithms |
| **Customizable** | Adjust strength, count, language, UI |
| **Educational** | Learn probability theory in action |
| **Fast** | Instant generation with NumPy optimization |

---

## 🤝 Contributing

Found a bug? Have an idea? Want to add a new language?

1. **Fork** the repository
2. **Create** a feature branch
3. **Commit** your changes
4. **Push** to your fork
5. **Submit** a pull request

---

## 📈 Project Stats

- **Downloads:** [Join us!]
- **Languages:** 5 (expanding)
- **Historical Data:** 1,967 draws
- **Lines of Code:** 500+ (lean & efficient)
- **Commits:** 10+ feature releases

---

## 🔗 Resources

- **🎰 [Powerball Official](https://www.powerball.com/)**
- **🎯 [How to Play](https://www.powerball.com/how-to-play)**
- **📊 [Historical Data](https://nylottery.ny.gov/)**
- **🔍 [Probability Theory](https://en.wikipedia.org/wiki/Probability_theory)**

---

## 📝 License

This project is open source and available for educational and entertainment purposes.

---

## 🎊 Getting Started

**New here?** Start with **[QUICKSTART.md](QUICKSTART.md)**

**Want features?** Check **[FEATURES.md](FEATURES.md)**

**Need data?** See **[DATA_SOURCES.md](DATA_SOURCES.md)**

---

## ⭐ Love LuckyWeaver?

Drop a star on GitHub! ⭐ It helps others discover this tool.

---

**Made with ❤️ for lottery enthusiasts, data scientists, and probability explorers everywhere.**

*Weave probability patterns into winning possibilities.* 🎯

---

**Latest Commit:** `cc15d8b` - Add data download tools  
**Last Updated:** September 2026  
**Status:** ✅ Active & Maintained
