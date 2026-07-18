import pandas as pd
import numpy as np
from pathlib import Path
import json

def analyze_rolling_windows(clean_data_file):
    """
    Rolling Window Overlap Analysis

    For each window size (2-10), analyze how many white ball numbers
    are repeated within that window across all historical drawings.
    """

    df = pd.read_csv(clean_data_file)
    df['Date'] = pd.to_datetime(df['Date'])

    # Create sets of white balls for each drawing
    df['white_balls_set'] = df.apply(
        lambda row: set([
            int(row['White1']), int(row['White2']),
            int(row['White3']), int(row['White4']),
            int(row['White5'])
        ]),
        axis=1
    )

    window_sizes = list(range(2, 11))  # 2 to 10
    results = {}

    for window_size in window_sizes:
        print(f"\nAnalyzing window size: {window_size}")

        overlaps = []

        # For each possible window in the dataset
        for i in range(len(df) - window_size + 1):
            window = df.iloc[i:i+window_size]

            # Get union of all white balls in this window
            union_balls = set()
            for j in range(window_size):
                union_balls.update(window.iloc[j]['white_balls_set'])

            # Count how many numbers appear more than once
            number_counts = {}
            for j in range(window_size):
                for ball in window.iloc[j]['white_balls_set']:
                    number_counts[ball] = number_counts.get(ball, 0) + 1

            # Count repeated numbers (appearing >= 2 times)
            repeated_count = sum(1 for count in number_counts.values() if count >= 2)
            overlaps.append(repeated_count)

        # Calculate statistics
        overlaps = np.array(overlaps)
        stats = {
            'window_size': window_size,
            'total_windows': len(overlaps),
            'mean': float(np.mean(overlaps)),
            'median': float(np.median(overlaps)),
            'min': int(np.min(overlaps)),
            'max': int(np.max(overlaps)),
            'std': float(np.std(overlaps))
        }

        # Calculate probability distribution
        prob_dist = {}
        for count in range(int(np.max(overlaps)) + 1):
            frequency = np.sum(overlaps == count)
            probability = frequency / len(overlaps) * 100
            prob_dist[count] = {
                'count': int(frequency),
                'probability': round(probability, 2)
            }

        stats['distribution'] = prob_dist
        results[window_size] = stats

        print(f"  Mean overlaps: {stats['mean']:.2f}")
        print(f"  Distribution: {prob_dist}")

    return results, df

def build_probability_matrix(results):
    """
    Build a probability matrix for all window sizes.

    Rows: Window Size (2-10)
    Columns: Number of repeated numbers (0, 1, 2, 3, ...)
    Values: Probability (%)
    """

    # Find max repeated count across all windows
    max_repeated = 0
    for window_size, stats in results.items():
        max_repeated = max(max_repeated, max(stats['distribution'].keys()))

    # Build matrix
    matrix_data = []
    for window_size in sorted(results.keys()):
        row = {'Window_Size': window_size}
        dist = results[window_size]['distribution']

        for repeated_count in range(int(max_repeated) + 1):
            if repeated_count in dist:
                row[f'Repeated_{repeated_count}'] = dist[repeated_count]['probability']
            else:
                row[f'Repeated_{repeated_count}'] = 0.0

        matrix_data.append(row)

    matrix_df = pd.DataFrame(matrix_data)
    return matrix_df

if __name__ == "__main__":
    clean_data_file = Path("/tmp/powerball-study/data/powerball_clean.csv")

    print("=" * 70)
    print("ROLLING WINDOW OVERLAP ANALYSIS")
    print("=" * 70)

    results, df = analyze_rolling_windows(clean_data_file)

    # Build probability matrix
    matrix_df = build_probability_matrix(results)

    print("\n" + "=" * 70)
    print("PROBABILITY MATRIX")
    print("=" * 70)
    print(matrix_df.to_string(index=False))

    # Save results
    results_dir = Path("/tmp/powerball-study/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Save as JSON
    with open(results_dir / "rolling_window_results.json", "w") as f:
        json.dump(results, f, indent=2, default=str)

    # Save matrix as CSV
    matrix_df.to_csv(results_dir / "rolling_window_matrix.csv", index=False)

    print(f"\nResults saved to {results_dir}")
    print(f"  - rolling_window_results.json")
    print(f"  - rolling_window_matrix.csv")
