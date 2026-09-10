# 🎰 LuckyWeaver - Intelligent Number Generator Features

## Web Application Highlights

### 🌍 Bilingual Support
- **English & 中文** - Switch instantly with one click
- All interface text and labels translated
- Responsive language switching

### 🎲 Intelligent Number Generation
**Decay-Based Probability Weighting:**
- Reduces probability of numbers that appeared in recent draws
- Weight decreases for older draws (exponential decay)
- Period 5 (most recent) has 100% decay weight
- Period 1 (oldest) has 20% decay weight

**Adjustable Strength:**
- 0% = No decay (random selection)
- 50% = Medium decay (balanced)
- 100% = Complete avoidance (no recent numbers)

### 📊 Batch Generation
Generate multiple combinations at once:
- 1-20 number sets per generation
- Each set independently generated
- Perfect for exploring multiple options

### 📈 Real-Time Analysis
- **Period table** - Shows decay weight for each recent draw
- **Statistics** - Display all recent white balls and red balls
- **Period breakdown** - Understand how weights change over time

### 🎨 Beautiful UI/UX
- Gradient design with smooth animations
- Responsive layout (desktop & mobile)
- Real-time visual feedback
- Color-coded balls (white = blue-purple, red = pink-red)

### ⚡ Performance
- Instant generation with NumPy optimization
- Fast API responses
- Smooth animations and transitions

---

## Technical Features

### Backend (Python Flask)
```python
# Probability weighting algorithm
- Period-based decay calculation
- NumPy vectorized operations
- JSON API with batch support
```

### Frontend (Vanilla JS)
```javascript
// No framework dependencies
- Lightweight HTML5/CSS3
- Vanilla JavaScript for interactions
- i18n (internationalization) support
```

### Data-Driven
- 1,967 historical Powerball draws (2010-2026)
- Clean, validated dataset
- Empirical probability analysis

---

## Use Cases

1. **Casual Fun** 🎉
   - Generate lottery tickets for entertainment
   - Explore different probability strategies
   - Compare multiple combinations

2. **Educational** 📚
   - Learn about probability weighting
   - Understand statistical decay functions
   - Analyze real lottery data

3. **Research** 🔬
   - Study pattern avoidance strategies
   - Analyze historical draws
   - Test hypotheses with batch generation

---

## Why Choose This Tool?

✅ **Interactive** - Real-time feedback and visualization  
✅ **Intelligent** - Smart probability decay based on recent data  
✅ **Customizable** - Adjustable strength and count  
✅ **Multilingual** - English & Chinese support  
✅ **Educational** - Built on real historical data  
✅ **Open Source** - Full source code available  
✅ **No Dependencies** - Frontend has zero JavaScript dependencies  

---

## Getting Started

### 1. Quick Start (5 minutes)
```bash
git clone https://github.com/siren7075/powerball-study.git
cd powerball-study
python3 -m venv app_venv
source app_venv/bin/activate
pip install -r requirements.txt
python3 app.py
# Open http://localhost:5001
```

### 2. Usage
1. Select language (English/中文)
2. Adjust decay strength (0-100%)
3. Set number of sets (1-20)
4. Click "Generate"
5. Explore results and statistics

### 3. Customization
- Modify `powerball_generator.py` for algorithm changes
- Edit `templates/index.html` for UI customization
- Change default values in `app.py`

---

## Perfect For

- 🎯 Lottery enthusiasts
- 📊 Data science learners
- 🎓 Statistics students
- 🔬 Researchers analyzing patterns
- 💻 Developers exploring Flask + NumPy

---

## API Endpoints

### Generate Numbers
```http
POST /api/generate
Content-Type: application/json

{
  "weight_strength": 0.6,    // 0-1
  "periods": 5,               // How many recent periods to consider
  "count": 5                   // 1-20 sets
}
```

**Response:**
```json
{
  "numbers": [
    {"white": [1, 2, 3, 4, 5], "red": 10},
    {"white": [6, 7, 8, 9, 10], "red": 15}
  ],
  "recent_numbers": [...],
  "recent_white": [...],
  "recent_red": [...]
}
```

### Get Latest Draw
```http
GET /api/latest
```

---

## Why This Works

The decay weighting algorithm is based on the intuition that:
1. Recently drawn numbers are "hot" and might avoid repetition
2. Older numbers gradually "cool down" and become normal again
3. Complete avoidance is unrealistic (1/69 chance), but selective reduction is reasonable

This is a **probability hypothesis**, not a guaranteed strategy.

---

## Disclaimer

🎰 **For Entertainment Only**

- This tool does NOT improve lottery odds
- Results are theoretical probability exercises
- Real lottery outcomes are random and independent
- No guarantee of winning
- Please gamble responsibly

Each drawing is a fresh event with equal probability for all numbers.

---

**Star ⭐ this project if you find it useful!**
