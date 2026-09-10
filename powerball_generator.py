import pandas as pd
import numpy as np
import json
from pathlib import Path

class PowerballGenerator:
    def __init__(self, csv_path="data/powerball_clean.csv"):
        self.df = pd.read_csv(csv_path)
        self.df['Date'] = pd.to_datetime(self.df['Date'])
        self.df = self.df.sort_values('Date').reset_index(drop=True)
        self.white_balls = list(range(1, 70))
        self.red_balls = list(range(1, 27))

    def get_recent_numbers_with_periods(self, periods=5):
        """获取最近N期出现的号码，带周期信息"""
        recent = self.df.tail(periods)
        period_data = []

        for idx, (_, row) in enumerate(recent.iterrows()):
            white = [int(row['White1']), int(row['White2']), int(row['White3']), int(row['White4']), int(row['White5'])]
            red = int(row['Powerball'])
            date = row['Date'].strftime('%Y-%m-%d')
            period_data.append({
                'period': periods - idx,  # 1=最近, N=最久
                'white': white,
                'red': red,
                'date': date
            })

        return period_data

    def generate_numbers(self, weight_strength=0.6, periods=5, count=1):
        """
        生成建议号码
        weight_strength: 0-1, 降权强度 (0=不降权, 1=完全避免)
        periods: 考虑最近多少期
        count: 生成多少组号码
        """
        period_data = self.get_recent_numbers_with_periods(periods)

        # 构建递减权重字典
        white_weight_dict = {num: 1.0 for num in self.white_balls}
        red_weight_dict = {num: 1.0 for num in self.red_balls}

        # 对每个周期的号码应用递减权重
        for data in period_data:
            period_factor = data['period'] / periods  # 最近的=1, 最久的=1/periods
            decay = weight_strength * period_factor   # 权重递减

            for num in data['white']:
                white_weight_dict[num] *= (1.0 - decay)

            red_weight_dict[data['red']] *= (1.0 - decay)

        # 转换为数组并标准化
        white_weights = np.array([white_weight_dict[num] for num in self.white_balls])
        white_weights = white_weights / white_weights.sum()

        red_weights = np.array([red_weight_dict[num] for num in self.red_balls])
        red_weights = red_weights / red_weights.sum()

        # 生成多组号码
        results = []
        for _ in range(count):
            white_result = sorted(np.random.choice(
                self.white_balls, size=5, replace=False, p=white_weights
            ))
            red_result = int(np.random.choice(
                self.red_balls, size=1, replace=False, p=red_weights
            )[0])
            results.append({
                'white': [int(x) for x in white_result],
                'red': red_result
            })

        # 收集最近号码
        recent_white = []
        recent_red = []
        for data in period_data:
            recent_white.extend(data['white'])
            recent_red.append(data['red'])

        return {
            'numbers': results,
            'recent_numbers': period_data,
            'recent_white': sorted(set(recent_white)),
            'recent_red': sorted(set(recent_red))
        }

    def get_latest_drawing(self):
        """获取最新一期的号码"""
        latest = self.df.iloc[-1]
        return {
            'date': latest['Date'].strftime('%Y-%m-%d'),
            'white': sorted([int(latest['White1']), int(latest['White2']),
                           int(latest['White3']), int(latest['White4']), int(latest['White5'])]),
            'red': int(latest['Powerball'])
        }

if __name__ == "__main__":
    gen = PowerballGenerator()
    latest = gen.get_latest_drawing()
    print(f"Latest drawing ({latest['date']}): {latest['white']} + {latest['red']}")

    result = gen.generate_numbers(weight_strength=0.6, periods=5)
    print(f"Recommended numbers: {result['white']} + {result['red']}")
    print(f"Recent white balls: {result['recent_white']}")
    print(f"Recent red balls: {result['recent_red']}")
