#!/usr/bin/env python3
"""
Simple manual data update for Powerball
Paste latest draw data and update CSV
"""

import csv
import pandas as pd
from datetime import datetime

def add_draws_manually():
    """Add draws manually by user input"""
    print("PowerballWeaver - Manual Data Update")
    print("=" * 50)
    print("\nEnter latest Powerball draws (press Enter twice to finish)")
    print("Format: YYYY-MM-DD,W1,W2,W3,W4,W5,R")
    print("Example: 2026-09-08,5,12,24,35,52,18\n")

    draws = []
    while True:
        line = input("Enter draw: ").strip()
        if not line:
            break
        try:
            parts = line.split(',')
            if len(parts) != 7:
                print("Error: Need 7 values (date, white1-5, red)")
                continue

            date_str = parts[0]
            w1, w2, w3, w4, w5, r = [int(x) for x in parts[1:]]

            # Validate
            if not all(1 <= x <= 69 for x in [w1, w2, w3, w4, w5]):
                print("Error: White balls must be 1-69")
                continue
            if not (1 <= r <= 26):
                print("Error: Red ball must be 1-26")
                continue

            draws.append({
                'Date': date_str,
                'White1': w1,
                'White2': w2,
                'White3': w3,
                'White4': w4,
                'White5': w5,
                'Powerball': r
            })
            print(f"Added: {date_str} {[w1,w2,w3,w4,w5]} + {r}")

        except Exception as e:
            print(f"Error: {e}")

    if not draws:
        print("No draws added")
        return False

    # Load existing data
    df_existing = pd.read_csv('data/powerball_clean.csv')
    df_new = pd.DataFrame(draws)

    # Merge
    df_merged = pd.concat([df_existing, df_new], ignore_index=True)
    df_merged = df_merged.drop_duplicates(subset=['Date'], keep='first')
    df_merged = df_merged.sort_values('Date').reset_index(drop=True)

    # Save
    df_merged.to_csv('data/powerball_clean.csv', index=False)

    print(f"\nSuccess! Added {len(draws)} draws")
    print(f"Total draws: {len(df_merged)}")
    print(f"Latest: {df_merged['Date'].iloc[-1]}")
    return True

def import_from_csv():
    """Import from external CSV file"""
    filename = input("Enter CSV filename: ").strip()
    try:
        df_new = pd.read_csv(filename)
        df_existing = pd.read_csv('data/powerball_clean.csv')

        df_merged = pd.concat([df_existing, df_new], ignore_index=True)
        df_merged = df_merged.drop_duplicates(subset=['Date'], keep='first')
        df_merged = df_merged.sort_values('Date').reset_index(drop=True)

        df_merged.to_csv('data/powerball_clean.csv', index=False)

        added = len(df_new) - (len(df_merged) - len(df_existing))
        print(f"Imported from {filename}")
        print(f"Added {added} new draws")
        print(f"Total: {len(df_merged)} draws")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == '__main__':
    print("\nOptions:")
    print("1. Enter draws manually")
    print("2. Import from CSV file")

    choice = input("\nChoose (1 or 2): ").strip()

    if choice == '1':
        add_draws_manually()
    elif choice == '2':
        import_from_csv()
    else:
        print("Invalid choice")
