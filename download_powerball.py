#!/usr/bin/env python3
"""
PowerballWeaver - Download Latest Powerball Data
Works on macOS, Linux, Windows
"""

import requests
import pandas as pd
from datetime import datetime
import sys

class PowerballDownloader:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        self.output_file = 'data/powerball_clean.csv'

    def download_from_ny_data(self):
        """Download from NY Open Data (most reliable)"""
        print("Downloading from NY State data portal...")
        try:
            # NY Lottery Powerball data
            url = "https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD"
            response = requests.get(url, headers=self.headers, timeout=15, verify=True)
            response.raise_for_status()

            data = response.json()
            drawings = []

            if 'data' in data:
                for row in data['data']:
                    try:
                        # NY format: [id, date, w1, w2, w3, w4, w5, pb, ...]
                        if len(row) >= 8:
                            date_str = str(row[1])[:10]
                            white = [int(row[i]) for i in range(2, 7)]
                            powerball = int(row[7])

                            if 1 <= powerball <= 26 and all(1 <= w <= 69 for w in white):
                                drawings.append({
                                    'Date': date_str,
                                    'White1': white[0],
                                    'White2': white[1],
                                    'White3': white[2],
                                    'White4': white[3],
                                    'White5': white[4],
                                    'Powerball': powerball
                                })
                    except (IndexError, ValueError, TypeError):
                        continue

            if drawings:
                print(f"Success! Downloaded {len(drawings)} draws")
                return drawings

        except Exception as e:
            print(f"NY Data failed: {e}")

        return None

    def download_from_usa_lottery(self):
        """Download from USA Lottery website"""
        print("Downloading from USA Lottery...")
        try:
            url = "https://www.usalottery.com/api/powerball/draws"
            response = requests.get(url, headers=self.headers, timeout=15, verify=True)
            response.raise_for_status()

            data = response.json()
            drawings = []

            if isinstance(data, list):
                for draw in data:
                    try:
                        date_str = draw.get('date', '')[:10]
                        white = draw.get('white_balls', [])
                        powerball = draw.get('powerball', 0)

                        if len(white) == 5 and 1 <= powerball <= 26:
                            drawings.append({
                                'Date': date_str,
                                'White1': int(white[0]),
                                'White2': int(white[1]),
                                'White3': int(white[2]),
                                'White4': int(white[3]),
                                'White5': int(white[4]),
                                'Powerball': int(powerball)
                            })
                    except (KeyError, IndexError, ValueError, TypeError):
                        continue

            if drawings:
                print(f"Success! Downloaded {len(drawings)} draws")
                return drawings

        except Exception as e:
            print(f"USA Lottery failed: {e}")

        return None

    def download_from_powerball_org(self):
        """Direct from powerball.com"""
        print("Downloading from Powerball.com...")
        try:
            url = "https://www.powerball.com/api/v1/draws/games/powerball/latest/100"
            response = requests.get(url, headers=self.headers, timeout=15, verify=True)
            response.raise_for_status()

            data = response.json()
            drawings = []

            if 'draws' in data:
                for draw in data.get('draws', []):
                    try:
                        date_str = draw.get('drawDate', '')[:10]
                        numbers = draw.get('winningNumbers', {})
                        white = numbers.get('whiteballnumbers', [])
                        powerball = numbers.get('powerballnumber', 0)

                        if len(white) == 5 and 1 <= powerball <= 26:
                            drawings.append({
                                'Date': date_str,
                                'White1': int(white[0]),
                                'White2': int(white[1]),
                                'White3': int(white[2]),
                                'White4': int(white[3]),
                                'White5': int(white[4]),
                                'Powerball': int(powerball)
                            })
                    except (KeyError, IndexError, ValueError, TypeError):
                        continue

            if drawings:
                print(f"Success! Downloaded {len(drawings)} draws")
                return drawings

        except Exception as e:
            print(f"Powerball.com failed: {e}")

        return None

    def merge_data(self, new_draws):
        """Merge new draws with existing data"""
        print("Merging with existing data...")

        # Load existing
        df_existing = pd.read_csv(self.output_file)
        df_new = pd.DataFrame(new_draws)

        # Merge
        df_merged = pd.concat([df_existing, df_new], ignore_index=True)
        df_merged = df_merged.drop_duplicates(subset=['Date'], keep='first')
        df_merged = df_merged.sort_values('Date').reset_index(drop=True)

        return df_merged

    def save_data(self, df):
        """Save to CSV"""
        df.to_csv(self.output_file, index=False)
        print(f"Saved to {self.output_file}")
        print(f"Total draws: {len(df)}")
        print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")

    def run(self):
        """Main execution"""
        print("=" * 60)
        print("PowerballWeaver - Data Downloader")
        print("=" * 60)
        print()

        # Try each source
        sources = [
            self.download_from_ny_data,
            self.download_from_powerball_org,
            self.download_from_usa_lottery,
        ]

        new_draws = None
        for source in sources:
            new_draws = source()
            if new_draws:
                break
            print()

        if not new_draws:
            print("\nError: Could not download from any source")
            print("Make sure you have internet connection")
            sys.exit(1)

        # Merge
        df = self.merge_data(new_draws)

        # Save
        self.save_data(df)

        print()
        print("=" * 60)
        print("Success! Data updated")
        print("=" * 60)
        print()
        print("Recent draws:")
        for idx, row in df.tail(5).iterrows():
            white = [int(row['White1']), int(row['White2']), int(row['White3']),
                    int(row['White4']), int(row['White5'])]
            print(f"  {row['Date']}: {white} + {int(row['Powerball'])}")

if __name__ == '__main__':
    downloader = PowerballDownloader()
    downloader.run()
