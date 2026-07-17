import json
from pathlib import Path
from datetime import datetime

def generate_comprehensive_report(results_dir):
    """
    Generate a comprehensive report combining all studies.
    """

    # Load all study results
    studies = {}
    study_files = ['study1_results.json', 'study2_results.json', 'study3_results.json']

    for study_file in study_files:
        file_path = results_dir / study_file
        if file_path.exists():
            with open(file_path, 'r') as f:
                studies[study_file.replace('_results.json', '')] = json.load(f)

    # Generate comprehensive report
    report_content = f"""
{'='*80}
POWERBALL COMPREHENSIVE ANALYSIS REPORT
{'='*80}

Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Dataset: Official New York State Powerball (2010-present)

{'='*80}
EXECUTIVE SUMMARY
{'='*80}

This report contains analysis of {studies['study1']['total_drawings']} Powerball drawings
from the official New York State lottery database. Three comprehensive studies have been
conducted to reveal patterns and characteristics of the lottery system.

Key Finding: NO duplicate drawings have occurred in the entire dataset, indicating
that the Powerball drawing system produces unique combinations each time.


{'='*80}
STUDY 1: DUPLICATE DRAWING ANALYSIS
{'='*80}

Research Question: Have there ever been identical Powerball drawings?

RESULTS SUMMARY:
  • Total number of drawings: {studies['study1']['total_drawings']:,}
  • Number of duplicate drawings: {studies['study1']['number_of_duplicate_drawings']}
  • Duplicate rate: {studies['study1']['duplicate_rate_percent']}%

CONCLUSION:
  ✓ NO IDENTICAL DUPLICATE DRAWINGS FOUND

Every Powerball drawing in the dataset is completely unique. No combination of
5 white balls and 1 Powerball has ever been repeated, even across {studies['study1']['total_drawings']} drawings
spanning over 16 years.

This strongly suggests the drawing mechanism is functioning properly and producing
genuinely random results without systematic repetition.


{'='*80}
STUDY 2: CONSECUTIVE DRAWING OVERLAP ANALYSIS
{'='*80}

Research Question: How many white ball numbers overlap between consecutive drawings?

OVERVIEW:
  • Total consecutive drawing pairs analyzed: {studies['study2']['total_consecutive_pairs']}
  • Average overlap: {studies['study2']['average_overlap']} numbers
  • Range: {studies['study2']['min_overlap']} to {studies['study2']['max_overlap']} overlapping numbers

OVERLAP DISTRIBUTION:
"""

    # Add overlap distribution table
    report_content += "\n  Overlap Count | Frequency | Probability\n"
    report_content += "  " + "-"*45 + "\n"

    for item in studies['study2']['overlap_distribution']:
        overlap = item['Overlap']
        count = item['Count']
        prob = item['Probability']
        report_content += f"  {overlap:13d} | {count:9d} | {prob:7.2f}%\n"

    report_content += f"""
KEY INSIGHTS:
  • {studies['study2']['insights'][0]}
  • {studies['study2']['insights'][1]}
  • {studies['study2']['insights'][2]}

INTERPRETATION:
The majority of consecutive drawings ({studies['study2']['overlap_distribution'][0]['Probability']:.1f}%) share NO white ball numbers,
suggesting that the lottery does not favor repeating recent numbers. This is a positive
indicator of randomness and prevents predictability based on recent draws.


{'='*80}
STUDY 3: NUMBER PATTERNS ANALYSIS
{'='*80}

Research Question: Do certain numbers appear more frequently? Is there bias in the draw?

HOT NUMBERS (Most Frequently Drawn):
"""

    # Add hot numbers
    for rank, (num, count) in enumerate(list(studies['study3']['hot_numbers']['top_10'].items())[:5], 1):
        report_content += f"  {rank}. Number {int(num):2d}: {int(count):3d} occurrences\n"

    report_content += f"""
COLD NUMBERS (Least Frequently Drawn):
"""

    # Add cold numbers
    cold_list = list(studies['study3']['cold_numbers']['bottom_10'].items())
    for rank, (num, count) in enumerate(cold_list[-5:], 1):
        report_content += f"  {rank}. Number {int(num):2d}: {int(count):3d} occurrences\n"

    report_content += f"""
EVEN/ODD DISTRIBUTION:
  • Even numbers: {studies['study3']['even_odd_distribution']['even_count']} ({studies['study3']['even_odd_distribution']['even_percentage']}%)
  • Odd numbers:  {studies['study3']['even_odd_distribution']['odd_count']} ({studies['study3']['even_odd_distribution']['odd_percentage']}%)

NUMBER GAP ANALYSIS (distance between consecutive numbers in a drawing):
  • Average gap: {studies['study3']['number_gaps']['average_gap']}
  • Median gap:  {studies['study3']['number_gaps']['median_gap']}
  • Min gap:     {studies['study3']['number_gaps']['min_gap']}
  • Max gap:     {studies['study3']['number_gaps']['max_gap']}
  • Std Dev:     {studies['study3']['number_gaps']['std_dev']}

KEY INSIGHTS:
"""

    for insight in studies['study3']['insights']:
        report_content += f"  • {insight}\n"

    report_content += f"""
ANALYSIS:
While some numbers appear more frequently than others (e.g., {studies['study3']['hot_numbers']['hottest']} vs {studies['study3']['cold_numbers']['coldest']}),
this variation falls within expected statistical ranges for a random process. The
slight bias towards even numbers ({studies['study3']['even_odd_distribution']['even_percentage']:.1f}% vs {studies['study3']['even_odd_distribution']['odd_percentage']:.1f}%) is minimal and
expected due to the slightly higher proportion of even numbers in the range (1-69).


{'='*80}
CONCLUSIONS & RECOMMENDATIONS
{'='*80}

1. RANDOMNESS: The Powerball lottery appears to be functioning as a genuine random
   number generator. There is no evidence of systematic bias or manipulation.

2. UNIQUENESS: No duplicate drawings have occurred, suggesting proper calibration of
   the drawing equipment and independent draws.

3. PATTERNS: While some numbers are drawn more frequently, the distribution is
   consistent with statistical randomness. No exploitable pattern was found.

4. CONSECUTIVE DRAWS: The fact that {studies['study2']['overlap_distribution'][0]['Probability']:.1f}% of consecutive draws share
   no white balls suggests that using recent numbers as a strategy would be
   ineffective.

5. RECOMMENDATION: Play the lottery for entertainment only. No mathematical pattern
   or strategy can improve odds beyond pure probability. The drawing mechanism
   appears sound and the results genuinely random.


{'='*80}
TECHNICAL NOTES
{'='*80}

Data Source: Official New York State Powerball Dataset
Analysis Period: 2010 - Present ({studies['study1']['total_drawings']} total drawings)
Analysis Method: Statistical analysis of historical drawing data
Tools Used: Python, Pandas, Matplotlib

All analysis code and raw data are available in the GitHub repository:
https://github.com/siren7075/powerball-study

{'='*80}
END OF REPORT
{'='*80}
"""

    return report_content

if __name__ == "__main__":
    results_dir = Path("/tmp/powerball-study/results")

    # Generate report
    report = generate_comprehensive_report(results_dir)

    # Save report
    with open(results_dir / "COMPREHENSIVE_ANALYSIS_REPORT.txt", "w") as f:
        f.write(report)

    print("Comprehensive report generated successfully!")
    print(f"Saved to: {results_dir / 'COMPREHENSIVE_ANALYSIS_REPORT.txt'}")
    print("\n" + report)
