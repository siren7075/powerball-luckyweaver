import pandas as pd
from pathlib import Path
import json

def analyze_consecutive_overlap(clean_data_file):
    """
    Study 2: Analyze overlapping white ball numbers between consecutive drawings.

    For each pair of consecutive drawings, count how many white ball numbers
    appear in both drawings (overlap count).
    """

    # Read cleaned data
    df = pd.read_csv(clean_data_file)
    df['Date'] = pd.to_datetime(df['Date'])

    # Create sets of white balls for each drawing
    def get_white_balls_set(row):
        return set([row['White1'], row['White2'], row['White3'], row['White4'], row['White5']])

    df['white_balls_set'] = df.apply(get_white_balls_set, axis=1)

    # Calculate overlap for consecutive drawings
    overlaps = []
    overlap_counts = {}

    for i in range(len(df) - 1):
        current_balls = df.iloc[i]['white_balls_set']
        next_balls = df.iloc[i+1]['white_balls_set']

        # Count overlapping numbers
        overlap = len(current_balls & next_balls)
        overlaps.append(overlap)

        # Track counts
        if overlap not in overlap_counts:
            overlap_counts[overlap] = 0
        overlap_counts[overlap] += 1

    # Create summary statistics
    overlap_df = pd.DataFrame({
        'Overlap': sorted(overlap_counts.keys()),
        'Count': [overlap_counts[i] for i in sorted(overlap_counts.keys())]
    })

    total_consecutive_pairs = len(overlaps)
    overlap_df['Probability'] = (overlap_df['Count'] / total_consecutive_pairs * 100).round(2)
    overlap_df['Probability_Str'] = overlap_df['Probability'].apply(lambda x: f"{x}%")

    # Calculate statistics
    avg_overlap = sum(overlaps) / len(overlaps)
    max_overlap = max(overlaps)
    min_overlap = min(overlaps)

    report = {
        'study': 'Study 2: Consecutive Drawing Overlap Analysis',
        'total_consecutive_pairs': int(total_consecutive_pairs),
        'average_overlap': round(avg_overlap, 2),
        'min_overlap': int(min_overlap),
        'max_overlap': int(max_overlap),
        'overlap_distribution': overlap_df.to_dict('records'),
        'insights': []
    }

    # Generate insights
    report['insights'].append(f"Average overlap between consecutive drawings: {avg_overlap:.2f} numbers")
    report['insights'].append(f"Most common overlap: {overlap_df.loc[overlap_df['Count'].idxmax(), 'Overlap']} numbers "
                             f"({overlap_df['Count'].max()} times, {overlap_df['Probability'].max()}%)")
    report['insights'].append(f"Probability of NO overlap (0 shared numbers): {overlap_counts.get(0, 0) / total_consecutive_pairs * 100:.2f}%")

    return report, overlap_df, overlaps

if __name__ == "__main__":
    clean_data_file = Path("/tmp/powerball-study/data/powerball_clean.csv")

    print("Running Study 2: Consecutive Drawing Overlap Analysis...")
    report, overlap_df, overlaps = analyze_consecutive_overlap(clean_data_file)

    # Print summary
    print("\n" + "="*60)
    print(f"Total consecutive pairs: {report['total_consecutive_pairs']}")
    print(f"Average overlap: {report['average_overlap']} numbers")
    print(f"Min overlap: {report['min_overlap']}")
    print(f"Max overlap: {report['max_overlap']}")
    print("\nOverlap Distribution:")
    print(overlap_df.to_string(index=False))
    print("="*60)

    # Print insights
    print("\nKey Insights:")
    for insight in report['insights']:
        print(f"  • {insight}")

    # Save report
    results_dir = Path("/tmp/powerball-study/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Save as JSON
    with open(results_dir / "study2_results.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    # Save as CSV
    overlap_df.to_csv(results_dir / "study2_overlap_distribution.csv", index=False)

    print(f"\nResults saved to {results_dir}")
