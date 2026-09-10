#!/usr/bin/env python3
"""
Download latest Powerball lottery data from multiple sources.
Supports: Powerball.com API, NY Lottery website, lottery.com
"""

import csv
import json
import requests
import pandas as pd
from datetime import datetime
from pathlib import Path

class PowerballDataDownloader:
    def __init__(self, output_file='data/powerball_clean.csv'):
        self.output_file = output_file
        self.base_path = Path(output_file).parent
        self.base_path.mkdir(parents=True, exist_ok=True)

    def download_from_powerball_api(self):
        """
        Download from Powerball.com API (Most reliable)
        Tries multiple API endpoints
        """
        print("📥 Downloading from Powerball.com API...")

        # Try multiple endpoints
        endpoints = [
            "https://www.powerball.com/api/v1/draws/games/powerball/last/100",
            "https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD",  # NY Lottery open data
            "https://www.powerball.com/api/draws/powerball/100",
            "https://powerball.com/api/v1/powerball/draws",
        ]

        for url in endpoints:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }

                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()

                data = response.json()
                drawings = self._parse_powerball_response(data, url)

                if drawings:
                    print(f"✅ Downloaded {len(drawings)} drawings from Powerball.com API")
                    return drawings

            except Exception as e:
                continue

        print("❌ All Powerball API endpoints failed")
        return None

    def _parse_powerball_response(self, data, url):
        """Parse different Powerball API response formats"""
        drawings = []

        # Format 1: Standard Powerball API
        if isinstance(data, dict):
            if 'draws' in data:
                for draw in data.get('draws', []):
                    try:
                        draw_date = draw.get('drawDate', '') or draw.get('date', '')
                        winning_numbers = draw.get('winningNumbers', {})
                        white_balls = winning_numbers.get('whiteballnumbers', []) or draw.get('whiteballs', [])
                        powerball = winning_numbers.get('powerballnumber', 0) or draw.get('powerball', 0)

                        if len(white_balls) == 5 and powerball > 0:
                            drawings.append({
                                'Date': str(draw_date)[:10],
                                'White1': int(white_balls[0]),
                                'White2': int(white_balls[1]),
                                'White3': int(white_balls[2]),
                                'White4': int(white_balls[3]),
                                'White5': int(white_balls[4]),
                                'Powerball': int(powerball)
                            })
                    except (KeyError, IndexError, ValueError):
                        continue

            # Format 2: NY Lottery open data
            elif 'data' in data:
                for row in data.get('data', []):
                    try:
                        # NY Lottery format: [id, date, w1, w2, w3, w4, w5, pb, ...]
                        if len(row) >= 8:
                            draw_date = str(row[1])[:10]
                            white1, white2, white3, white4, white5 = int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6])
                            powerball = int(row[7])

                            if 1 <= powerball <= 26:
                                drawings.append({
                                    'Date': draw_date,
                                    'White1': white1,
                                    'White2': white2,
                                    'White3': white3,
                                    'White4': white4,
                                    'White5': white5,
                                    'Powerball': powerball
                                })
                    except (IndexError, ValueError):
                        continue

        return drawings

    def download_from_ny_lottery(self):
        """
        Download from NY Lottery website
        Alternative source for recent draws
        """
        print("📥 Downloading from NY Lottery website...")
        try:
            # NY Lottery usually has CSV export
            url = "https://nylottery.ny.gov/wps/portal/Home/Lottery/Results/P/Powerball"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # Note: NY Lottery website structure may vary
            # This is a placeholder - actual scraping would require parsing HTML
            print("⚠️  NY Lottery web scraping requires HTML parsing")
            return None

        except Exception as e:
            print(f"❌ Error downloading from NY Lottery: {e}")
            return None

    def download_from_lottery_dot_com(self):
        """
        Download from lottery.com API (Alternative source)
        """
        print("📥 Downloading from lottery.com...")
        try:
            url = "https://www.lottery.com/api/v2/lottery/drawings/powerball/recent"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()
            drawings = []

            if 'drawings' in data:
                for draw in data['drawings']:
                    try:
                        draw_date = draw.get('drawDate')
                        numbers = draw.get('numbers', [])
                        powerball = draw.get('powerball', 0)

                        if len(numbers) >= 5 and powerball > 0:
                            drawings.append({
                                'Date': draw_date,
                                'White1': numbers[0],
                                'White2': numbers[1],
                                'White3': numbers[2],
                                'White4': numbers[3],
                                'White5': numbers[4],
                                'Powerball': powerball
                            })
                    except (KeyError, IndexError):
                        continue

            if drawings:
                print(f"✅ Downloaded {len(drawings)} drawings from lottery.com")
                return drawings
            else:
                return None

        except Exception as e:
            print(f"❌ Error downloading from lottery.com: {e}")
            return None

    def merge_with_existing(self, new_drawings):
        """
        Merge new drawings with existing data, avoiding duplicates
        """
        print("🔄 Merging with existing data...")

        if not Path(self.output_file).exists():
            print(f"   Creating new file: {self.output_file}")
            df_new = pd.DataFrame(new_drawings)
            df_new['Date'] = pd.to_datetime(df_new['Date'])
            df_new = df_new.sort_values('Date').reset_index(drop=True)
            return df_new

        # Load existing data
        try:
            df_existing = pd.read_csv(self.output_file)
            df_existing['Date'] = pd.to_datetime(df_existing['Date'])
        except Exception as e:
            print(f"   Warning: Could not read existing file: {e}")
            df_existing = pd.DataFrame()

        if df_existing.empty:
            df_new = pd.DataFrame(new_drawings)
            df_new['Date'] = pd.to_datetime(df_new['Date'])
            return df_new

        df_new = pd.DataFrame(new_drawings)
        df_new['Date'] = pd.to_datetime(df_new['Date'])

        # Merge and remove duplicates
        df_merged = pd.concat([df_existing, df_new], ignore_index=True)
        df_merged = df_merged.drop_duplicates(subset=['Date'], keep='first')
        df_merged = df_merged.sort_values('Date').reset_index(drop=True)

        new_count = len(df_merged) - len(df_existing)
        print(f"   ✅ Added {new_count} new drawings")
        print(f"   Total: {len(df_merged)} drawings")

        return df_merged

    def save_data(self, df):
        """Save data to CSV"""
        try:
            # Sort by date
            df = df.sort_values('Date').reset_index(drop=True)

            # Save to CSV
            df.to_csv(self.output_file, index=False)
            print(f"✅ Saved to {self.output_file}")

            # Print statistics
            print(f"\n📊 Dataset Statistics:")
            print(f"   Total drawings: {len(df)}")
            print(f"   Date range: {df['Date'].min()} to {df['Date'].max()}")

            return True
        except Exception as e:
            print(f"❌ Error saving data: {e}")
            return False

    def validate_data(self, df):
        """Validate data integrity"""
        print("\n✓ Validating data...")

        # Check for required columns
        required_cols = ['Date', 'White1', 'White2', 'White3', 'White4', 'White5', 'Powerball']
        if not all(col in df.columns for col in required_cols):
            print("❌ Missing required columns")
            return False

        # Check value ranges
        for col in ['White1', 'White2', 'White3', 'White4', 'White5']:
            if not df[col].between(1, 69).all():
                print(f"❌ {col} values out of range (1-69)")
                return False

        if not df['Powerball'].between(1, 26).all():
            print("❌ Powerball values out of range (1-26)")
            return False

        # Check for duplicates
        if df.duplicated(subset=['Date']).any():
            print("⚠️  Warning: Duplicate dates found")

        print("✅ Data validation passed")
        return True

    def download_and_update(self):
        """Main method to download and update data"""
        print("=" * 60)
        print("🎰 Powerball Data Downloader")
        print("=" * 60)

        # Try Powerball.com API first (most reliable)
        new_drawings = self.download_from_powerball_api()

        # Fallback to lottery.com if API fails
        if not new_drawings:
            new_drawings = self.download_from_lottery_dot_com()

        if not new_drawings:
            print("\n❌ Failed to download data from all sources")
            return False

        # Merge with existing data
        df = self.merge_with_existing(new_drawings)

        # Validate
        if not self.validate_data(df):
            print("⚠️  Validation failed, but continuing...")

        # Save
        if self.save_data(df):
            print("\n" + "=" * 60)
            print("✅ Data update completed successfully!")
            print("=" * 60)
            return True

        return False


def main():
    import sys

    # Optional: specify custom output file
    output_file = sys.argv[1] if len(sys.argv) > 1 else 'data/powerball_clean.csv'

    downloader = PowerballDataDownloader(output_file)
    downloader.download_and_update()


if __name__ == '__main__':
    main()
