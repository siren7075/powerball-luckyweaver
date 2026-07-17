import pandas as pd
from pathlib import Path
import json
import statistics

def analyze_number_patterns(clean_data_file):
    """
    Study 3: Analyze patterns in white ball numbers.

    Including:
    - Hot/Cold numbers (most/least frequent)
    - Even/Odd distribution
    - Number gap analysis
    """

    # Read cleaned data
    df = pd.read_csv(clean_data_file)

    # Collect all white ball numbers
    all_white_balls = []
    for col in ['White1', 'White2', 'White3', 'White4', 'White5']:
        all_white_balls.extend(df[col].values)

    # Hot/Cold numbers
    number_counts = pd.Series(all_white_balls).value_counts()

    hottest_10 = number_counts.head(10).to_dict()
    coldest_10 = number_counts.tail(10).to_dict()

    # Even/Odd analysis
    def is_even(n):
        return n % 2 == 0

    even_count = sum(1 for n in all_white_balls if is_even(n))
    odd_count = len(all_white_balls) - even_count

    # Number gaps within drawings
    gaps = []
    for i in range(len(df)):
        balls = sorted([int(df.iloc[i]['White1']), int(df.iloc[i]['White2']),
                       int(df.iloc[i]['White3']), int(df.iloc[i]['White4']),
                       int(df.iloc[i]['White5'])])
        for j in range(len(balls) - 1):
            gap = int(balls[j+1] - balls[j])
            gaps.append(gap)

    report = {
        'study': 'Study 3: Number Patterns Analysis',
        'total_white_ball_occurrences': len(all_white_balls),
        'unique_numbers': len(number_counts),
        'hot_numbers': {
            'top_10': {int(k): int(v) for k, v in list(hottest_10.items())},
            'hottest': int(number_counts.index[0]),
            'hottest_count': int(number_counts.iloc[0])
        },
        'cold_numbers': {
            'bottom_10': {int(k): int(v) for k, v in list(coldest_10.items())},
            'coldest': int(number_counts.index[-1]),
            'coldest_count': int(number_counts.iloc[-1])
        },
        'even_odd_distribution': {
            'even_count': int(even_count),
            'odd_count': int(odd_count),
            'even_percentage': round(even_count / len(all_white_balls) * 100, 2),
            'odd_percentage': round(odd_count / len(all_white_balls) * 100, 2)
        },
        'number_gaps': {
            'average_gap': round(statistics.mean(gaps), 2),
            'median_gap': statistics.median(gaps),
            'min_gap': min(gaps),
            'max_gap': max(gaps),
            'std_dev': round(statistics.stdev(gaps), 2)
        },
        'insights': []
    }

    # Generate insights
    report['insights'].append(f"Hottest number: {report['hot_numbers']['hottest']} (appeared {report['hot_numbers']['hottest_count']} times)")
    report['insights'].append(f"Coldest number: {report['cold_numbers']['coldest']} (appeared {report['cold_numbers']['coldest_count']} times)")
    report['insights'].append(f"Even/Odd split: {report['even_odd_distribution']['even_percentage']}% even, {report['even_odd_distribution']['odd_percentage']}% odd")
    report['insights'].append(f"Average gap between consecutive numbers in a drawing: {report['number_gaps']['average_gap']}")

    return report

if __name__ == "__main__":
    clean_data_file = Path("/tmp/powerball-study/data/powerball_clean.csv")

    print("Running Study 3: Number Patterns Analysis...")
    report = analyze_number_patterns(clean_data_file)

    # Print summary
    print("\n" + "="*60)
    print("HOT NUMBERS (Top 10)")
    print("-"*60)
    for num, count in report['hot_numbers']['top_10'].items():
        print(f"  Number {num:2d}: {count:3d} occurrences")

    print("\nCOLD NUMBERS (Bottom 10)")
    print("-"*60)
    for num, count in report['cold_numbers']['bottom_10'].items():
        print(f"  Number {num:2d}: {count:3d} occurrences")

    print("\nEVEN/ODD DISTRIBUTION")
    print("-"*60)
    print(f"  Even: {report['even_odd_distribution']['even_count']} ({report['even_odd_distribution']['even_percentage']}%)")
    print(f"  Odd:  {report['even_odd_distribution']['odd_count']} ({report['even_odd_distribution']['odd_percentage']}%)")

    print("\nNUMBER GAP ANALYSIS")
    print("-"*60)
    print(f"  Average gap: {report['number_gaps']['average_gap']}")
    print(f"  Median gap:  {report['number_gaps']['median_gap']}")
    print(f"  Min gap:     {report['number_gaps']['min_gap']}")
    print(f"  Max gap:     {report['number_gaps']['max_gap']}")
    print(f"  Std Dev:     {report['number_gaps']['std_dev']}")
    print("="*60)

    # Print insights
    print("\nKey Insights:")
    for insight in report['insights']:
        print(f"  • {insight}")

    # Save report
    results_dir = Path("/tmp/powerball-study/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    with open(results_dir / "study3_results.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    print(f"\nResults saved to {results_dir}")
