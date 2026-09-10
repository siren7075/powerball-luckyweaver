# 📥 Downloading Latest Powerball Data

## Quick Start

```bash
python3 download_latest_data.py
```

That's it! The script will:
1. ✅ Download latest drawings from Powerball.com API
2. ✅ Merge with existing data (removes duplicates)
3. ✅ Validate data integrity
4. ✅ Save to `data/powerball_clean.csv`

---

## How It Works

### Data Sources (in order of priority)

1. **Powerball.com API** (Primary) ⭐
   - Official Powerball website API
   - Most reliable and up-to-date
   - Covers last 100+ drawings

2. **lottery.com API** (Fallback)
   - Alternative source if Powerball API fails
   - Good backup coverage

3. **NY Lottery Website** (Future)
   - Regional data source
   - Currently requires HTML parsing

### Features

✓ **Automatic merging** - Avoids duplicate dates  
✓ **Data validation** - Checks number ranges (1-69 for white, 1-26 for red)  
✓ **Statistics** - Shows date range and total count  
✓ **Error handling** - Falls back if one source fails  
✓ **Incremental updates** - Only adds new drawings  

---

## Usage Examples

### Update default dataset
```bash
python3 download_latest_data.py
```

### Update custom file
```bash
python3 download_latest_data.py /path/to/custom_file.csv
```

### Run as scheduled task (cron)

**Update daily at 11 PM:**
```bash
# Edit crontab
crontab -e

# Add this line
0 23 * * * cd /path/to/powerball-study && python3 download_latest_data.py
```

**Update weekly (every Monday at 9 AM):**
```
0 9 * * 1 cd /path/to/powerball-study && python3 download_latest_data.py
```

---

## Output Example

```
============================================================
🎰 Powerball Data Downloader
============================================================
📥 Downloading from Powerball.com API...
✅ Downloaded 100 drawings from Powerball.com API
🔄 Merging with existing data...
   ✅ Added 5 new drawings
   Total: 1972 drawings

✓ Validating data...
✅ Data validation passed

✅ Saved to data/powerball_clean.csv

📊 Dataset Statistics:
   Total drawings: 1972
   Date range: 2010-02-03 to 2026-09-08

============================================================
✅ Data update completed successfully!
============================================================
```

---

## What Gets Validated

✅ **Required columns** - Date, White1-5, Powerball  
✅ **White ball range** - 1 to 69  
✅ **Red ball range** - 1 to 26  
✅ **No duplicates** - Each date appears once  

---

## Troubleshooting

### Script fails to download

**Problem:** "Connection error" or "API timeout"

**Solution:**
- Check internet connection
- Try running again (APIs can be temporary down)
- Check if firewall blocks requests
- Verify your IP isn't rate-limited

### Getting "SSL certificate error"

**Solution:**
```bash
# Disable SSL verification (not recommended for security)
# Edit the script and change:
response = requests.get(url, headers=headers, timeout=10, verify=False)
```

### Data seems old

**Problem:** New data isn't showing up

**Solution:**
- Powerball draws are typically on Monday, Wednesday, Saturday
- Wait for the next draw
- Check powerball.com manually to verify new draws exist

### Duplicate errors

**Problem:** Same date appears multiple times

**Solution:**
```bash
# The script removes duplicates automatically
# But to manually clean, use:
python3 -c "
import pandas as pd
df = pd.read_csv('data/powerball_clean.csv')
df = df.drop_duplicates(subset=['Date'])
df.to_csv('data/powerball_clean.csv', index=False)
"
```

---

## Advanced Usage

### Download and update web app in one command

```bash
#!/bin/bash
cd /path/to/powerball-study

# Update data
python3 download_latest_data.py

# Restart web app
pkill -f "python3 app.py"
sleep 1
source app_venv/bin/activate
python3 app.py &

echo "✅ Data updated and app restarted"
```

Save as `update_and_restart.sh`, then run:
```bash
chmod +x update_and_restart.sh
./update_and_restart.sh
```

### Python API

```python
from download_latest_data import PowerballDataDownloader

# Create downloader
downloader = PowerballDataDownloader('data/powerball_clean.csv')

# Download and update
downloader.download_and_update()

# Or download and get DataFrame directly
new_data = downloader.download_from_powerball_api()
df = downloader.merge_with_existing(new_data)
downloader.save_data(df)
```

---

## Supported Data Sources

| Source | Type | Coverage | Reliability |
|--------|------|----------|-------------|
| Powerball.com API | Official | Last 100+ draws | ⭐⭐⭐⭐⭐ |
| lottery.com API | Third-party | Last 100+ draws | ⭐⭐⭐⭐ |
| NY Lottery Website | Official | Recent draws | ⭐⭐⭐ |

---

## Dataset Format

The CSV file has this structure:

```
Date,White1,White2,White3,White4,White5,Powerball
2010-02-03,17,22,36,37,52,24
2010-02-06,14,22,52,54,59,4
...
```

**Columns:**
- `Date` - Drawing date (YYYY-MM-DD)
- `White1-5` - White ball numbers (1-69, sorted)
- `Powerball` - Red ball (1-26)

---

## FAQ

**Q: How often should I update?**  
A: Powerball draws 3x per week (Mon, Wed, Sat). Weekly updates are sufficient.

**Q: Does it preserve my original data?**  
A: Yes! It merges with existing data and removes duplicates. Your original data is never lost.

**Q: Can I add manual data?**  
A: Yes, just add rows to the CSV and the script will merge them correctly.

**Q: What if an API is down?**  
A: The script tries multiple sources automatically. If all fail, it will notify you.

**Q: Can I contribute new data sources?**  
A: Absolutely! Feel free to add new methods to the class and submit a pull request.

---

## Contributing

Found a better data source? Want to add support for another lottery?

1. Add a new method: `download_from_xyz()`
2. Call it in `download_and_update()`
3. Submit a pull request!

---

*Keep your Powerball data fresh and up-to-date! 🎰*
