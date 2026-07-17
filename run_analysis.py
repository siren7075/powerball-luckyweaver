#!/usr/bin/env python3
"""Main script to run the complete Powerball analysis."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from data_cleaner import clean_powerball_data
from study1_analysis import analyze_duplicates
from study2_overlap_analysis import analyze_consecutive_overlap
from study3_number_patterns import analyze_number_patterns
from visualizations import create_visualizations
from visualizations_extended import create_extended_visualizations
from comprehensive_report import generate_comprehensive_report

def main():
    print("Starting Powerball Analysis Pipeline...")
    print("=" * 60)

    results_dir = Path(__file__).parent / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: Clean data
    print("\n[1/6] Cleaning data...")
    raw_data_file = Path("/Users/lynnzic/Downloads/Tech/powerball/export.csv")
    clean_data_file = Path(__file__).parent / "data" / "powerball_clean.csv"
    clean_data_file.parent.mkdir(parents=True, exist_ok=True)

    clean_df = clean_powerball_data(raw_data_file)
    clean_df.to_csv(clean_data_file, index=False)
    print(f"✓ Data cleaned. Total rows: {len(clean_df)}")

    # Step 2: Run Study 1 analysis
    print("\n[2/6] Running Study 1: Duplicate Drawing Analysis...")
    report1, _ = analyze_duplicates(clean_data_file)
    print(f"✓ Study 1 complete - {report1['number_of_duplicate_drawings']} duplicates found")

    # Step 3: Run Study 2 analysis
    print("\n[3/6] Running Study 2: Consecutive Drawing Overlap Analysis...")
    report2, overlap_df, overlaps = analyze_consecutive_overlap(clean_data_file)
    print(f"✓ Study 2 complete - Average overlap: {report2['average_overlap']} numbers")

    # Step 4: Run Study 3 analysis
    print("\n[4/6] Running Study 3: Number Patterns Analysis...")
    report3 = analyze_number_patterns(clean_data_file)
    print(f"✓ Study 3 complete - Analyzed {report3['total_white_ball_occurrences']} white ball occurrences")

    # Step 5: Create visualizations
    print("\n[5/6] Creating visualizations...")
    results_json_file = results_dir / "study1_results.json"
    create_visualizations(clean_data_file, results_json_file)
    create_extended_visualizations(results_dir)
    print(f"✓ All visualizations created.")

    # Step 6: Generate comprehensive report
    print("\n[6/6] Generating comprehensive report...")
    comprehensive_report = generate_comprehensive_report(results_dir)
    print(f"✓ Comprehensive report generated.")

    print("\n" + "=" * 60)
    print("✓ All analyses complete!")
    print(f"\nResults saved to: {results_dir}")
    print("\nGenerated files:")
    for file in sorted(results_dir.glob("*")):
        if file.is_file():
            print(f"  - {file.name}")

if __name__ == "__main__":
    main()
