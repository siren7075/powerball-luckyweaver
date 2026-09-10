# 🎰 Powerball 数据来源完整指南

## 官方数据源

### 1. **Powerball.com** (官方网站)
**URL:** https://www.powerball.com/results

📍 **如何获取：**
- 访问网站
- 点击 "Results" 或 "Past Results"
- 手动查看或复制最新的开奖号码

📊 **数据质量:** ⭐⭐⭐⭐⭐  
💾 **覆盖:** 所有开奖记录

---

### 2. **纽约州彩票** (NY Lottery)
**URL:** https://nylottery.ny.gov/

📍 **如何获取：**
1. 访问网站
2. 找到 "Powerball Results" 
3. 查看最近的开奖

📊 **数据质量:** ⭐⭐⭐⭐⭐  
💾 **覆盖:** NY地区的官方记录

---

### 3. **美国彩票** (USALottery)
**URL:** https://www.usalottery.com/powerball/results

📍 **如何获取：**
- 查看历史结果
- 支持按日期搜索

📊 **数据质量:** ⭐⭐⭐⭐  
💾 **覆盖:** 完整历史记录

---

### 4. **Lottery.com**
**URL:** https://www.lottery.com/powerball/results

📍 **如何获取：**
- 浏览历史开奖
- 提供CSV导出选项（某些情况下）

📊 **数据质量:** ⭐⭐⭐⭐  
💾 **覆盖:** 最近的开奖

---

## 自动化下载方法

### 方法 A: 使用现成的Python库

```bash
pip install lottery-data
```

```python
from lottery_data import PowerballScraper

scraper = PowerballScraper()
recent_draws = scraper.get_recent(100)  # 获取最近100期

# 保存到CSV
import pandas as pd
df = pd.DataFrame(recent_draws)
df.to_csv('powerball_new.csv', index=False)
```

### 方法 B: 使用Web抓取库 (BeautifulSoup)

```bash
pip install beautifulsoup4 requests lxml
```

```python
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_powerball():
    """从USALottery抓取数据"""
    url = "https://www.usalottery.com/powerball/results"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    drawings = []
    
    # 查找结果表格
    table = soup.find('table', {'class': 'results-table'})
    
    if table:
        rows = table.find_all('tr')[1:]  # 跳过表头
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 6:
                try:
                    date_str = cols[0].text.strip()
                    white_balls = [int(x.strip()) for x in cols[1:6]]
                    powerball = int(cols[6].text.strip())
                    
                    drawings.append({
                        'Date': date_str,
                        'White1': white_balls[0],
                        'White2': white_balls[1],
                        'White3': white_balls[2],
                        'White4': white_balls[3],
                        'White5': white_balls[4],
                        'Powerball': powerball
                    })
                except:
                    continue
    
    return drawings

# 使用
if __name__ == '__main__':
    draws = scrape_powerball()
    print(f"找到 {len(draws)} 期开奖")
    
    # 保存
    with open('powerball_from_web.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Date', 'White1', 'White2', 'White3', 'White4', 'White5', 'Powerball'])
        writer.writeheader()
        writer.writerows(draws)
```

---

## 手动方法

### 方法 1: 从网站复制-粘贴

1. **访问:** powerball.com/results
2. **选择:** 选择最新的开奖
3. **复制:** 复制号码
4. **粘贴:** 添加到 `data/powerball_clean.csv`

**格式：**
```
Date,White1,White2,White3,White4,White5,Powerball
2026-09-08,12,35,41,52,68,19
```

### 方法 2: 使用电子表格

1. 创建 `new_draws.csv`
2. 手动输入最新的号码
3. 运行合并脚本：

```python
import pandas as pd

# 读取旧数据
df_old = pd.read_csv('data/powerball_clean.csv')

# 读取新数据
df_new = pd.read_csv('new_draws.csv')

# 合并
df_merged = pd.concat([df_old, df_new], ignore_index=True)
df_merged = df_merged.drop_duplicates(subset=['Date'])
df_merged = df_merged.sort_values('Date')

# 保存
df_merged.to_csv('data/powerball_clean.csv', index=False)
print(f"✅ 合并成功！总共 {len(df_merged)} 期开奖")
```

---

## Google 电子表格方法

如果你想在线维护数据：

1. **创建Google Sheet**
   - 创建列: Date, White1-5, Powerball

2. **定期更新**
   - 从powerball.com复制-粘贴

3. **导出为CSV**
   - 文件 → 下载 → CSV

4. **上传到项目**
   ```bash
   # 将下载的CSV放入项目
   cp ~/Downloads/Powerball_Draws.csv data/powerball_clean.csv
   ```

---

## API 端点参考

### 可用的Public APIs

| 服务 | 端点 | 备注 |
|------|------|------|
| Powerball.com | /api/draws | 需要验证 |
| NY Lottery | data.ny.gov API | 公开数据 |
| lottery.com | /api/games/powerball | 有限制 |
| sporting-life.com | /powerball/results | 无API |

---

## 自动化更新脚本

### 使用Cron作业 (Linux/Mac)

**1. 创建更新脚本 `update_powerball.sh`:**

```bash
#!/bin/bash

cd /path/to/powerball-study

# 从Powerball.com下载最新数据
# (需要自己实现或使用现成脚本)

# 更新时间戳
echo "最后更新时间: $(date)" >> data/update_log.txt

# 如果使用web app，可以重启
# pkill -f "python3 app.py"
# sleep 1
# source app_venv/bin/activate
# python3 app.py &
```

**2. 添加到Cron:**

```bash
crontab -e

# 每周六晚上11点更新 (Powerball抽签时间之后)
0 23 * * 6 /path/to/powerball-study/update_powerball.sh
```

---

## 推荐工作流

### 对于个人项目:

```
每周:
1. 访问 powerball.com/results
2. 查看最新3期开奖
3. 复制号码到 new_draws.csv
4. 运行合并脚本
5. 上传到GitHub
```

### 对于生产环境:

```
每周:
1. 使用Web爬取脚本 (BeautifulSoup)
2. 自动验证数据
3. 合并到现有数据
4. 运行单元测试
5. 提交到GitHub
```

---

## 数据格式标准

确保数据符合此格式:

```csv
Date,White1,White2,White3,White4,White5,Powerball
2026-01-01,5,17,28,43,52,18
```

**验证:**
- Date: YYYY-MM-DD 格式
- White1-5: 1-69之间，已排序
- Powerball: 1-26之间

---

## 添加你自己的来源

如果你找到新的数据源:

1. **测试它**
   - 确认有效和准确

2. **添加到 download_latest_data.py**
   ```python
   def download_from_my_source(self):
       # 你的代码
       pass
   ```

3. **提交PR** 到项目

---

## 数据更新提示

✅ **DO:**
- 定期更新 (每周)
- 验证数据准确性
- 保留备份
- 检查重复日期

❌ **DON'T:**
- 手动编辑历史数据
- 混合不同格式
- 忘记备份
- 使用未验证的来源

---

## 常见问题

**Q: 最新数据在哪里？**  
A: powerball.com/results 总是有最新的

**Q: 多久更新一次？**  
A: Powerball每周抽签3次 (周一、三、六晚上10:59 EST)

**Q: 可以自动化吗？**  
A: 是的，使用BeautifulSoup或现成的库

**Q: 需要API密钥吗？**  
A: 大多数公开来源不需要

---

## 有用的链接

- 📌 [Powerball官网](https://www.powerball.com/)
- 📌 [NY Lottery](https://nylottery.ny.gov/)
- 📌 [USA Lottery](https://www.usalottery.com/)
- 📌 [美国彩票数据](https://www.uslottery.com/)

*保持数据最新，生成器会用最新的号码！* 🎰
