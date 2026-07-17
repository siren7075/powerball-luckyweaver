#!/usr/bin/env python3
"""Main script to run the complete Powerball analysis."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from data_cleaner import clean_powerball_data
from study1_analysis import analyze_duplicates
from visualizations import create_visualizations

def main():
    print("Starting Powerball Analysis Pipeline...")
    print("=" * 60)

    # Step 1: Clean data
    print("\n[1/3] Cleaning data...")
    raw_data_file = Path("/Users/lynnzic/Downloads/Tech/powerball/export.csv")
    clean_data_file = Path(__file__).parent / "data" / "powerball_clean.csv"
    clean_data_file.parent.mkdir(parents=True, exist_ok=True)

    clean_df = clean_powerball_data(raw_data_file)
    clean_df.to_csv(clean_data_file, index=False)
    print(f"✓ Data cleaned. Total rows: {len(clean_df)}")

    # Step 2: Run Study 1 analysis
    print("\n[2/3] Running Study 1 analysis...")
    report, _ = analyze_duplicates(clean_data_file)
    print(f"✓ Analysis complete.")
    print(f"   - Total drawings: {report['total_drawings']}")
    print(f"   - Duplicate drawings: {report['number_of_duplicate_drawings']}")
    print(f"   - Duplicate rate: {report['duplicate_rate_percent']}%")

    # Step 3: Create visualizations
    print("\n[3/3] Creating visualizations...")
    results_json_file = Path(__file__).parent / "results" / "study1_results.json"
    create_visualizations(clean_data_file, results_json_file)
    print(f"✓ Visualizations created.")

    print("\n" + "=" * 60)
    print("✓ Analysis complete!")
    print(f"\nResults saved to: {Path(__file__).parent / 'results'}")
    print("\nGenerated files:")
    results_dir = Path(__file__).parent / "results"
    for file in sorted(results_dir.glob("*")):
        print(f"  - {file.name}")

if __name__ == "__main__":
    main()
