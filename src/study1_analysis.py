import pandas as pd
from pathlib import Path
import json

def analyze_duplicates(clean_data_file):
    """
    Study 1: Determine whether there has ever been an identical Powerball drawing.

    An identical drawing means all 5 white balls AND the powerball are the same
    (order doesn't matter for white balls, but let's check exact matches first).
    """

    # Read cleaned data
    df = pd.read_csv(clean_data_file)
    df['Date'] = pd.to_datetime(df['Date'])

    # Create a tuple of winning numbers (sorted white balls, then powerball)
    def create_drawing_tuple(row):
        white_balls = sorted([row['White1'], row['White2'], row['White3'], row['White4'], row['White5']])
        powerball = row['Powerball']
        return tuple(white_balls + [powerball])

    df['drawing_tuple'] = df.apply(create_drawing_tuple, axis=1)

    # Count occurrences
    drawing_counts = df['drawing_tuple'].value_counts()
    duplicates = drawing_counts[drawing_counts > 1]

    total_drawings = len(df)
    num_duplicate_drawings = len(duplicates)
    duplicate_rate = (num_duplicate_drawings / total_drawings * 100) if total_drawings > 0 else 0

    # Collect duplicate details
    duplicate_details = []
    if num_duplicate_drawings > 0:
        for drawing_tuple in duplicates.index:
            matching_rows = df[df['drawing_tuple'] == drawing_tuple].copy()
            matching_rows = matching_rows.sort_values('Date')

            duplicate_details.append({
                'drawing': drawing_tuple,
                'count': len(matching_rows),
                'dates': matching_rows['Date'].dt.strftime('%Y-%m-%d').tolist(),
                'white_balls': sorted([int(drawing_tuple[i]) for i in range(5)]),
                'powerball': int(drawing_tuple[5])
            })

    # Generate report
    report = {
        'study': 'Study 1: Duplicate Drawing Analysis',
        'total_drawings': int(total_drawings),
        'number_of_duplicate_drawings': int(num_duplicate_drawings),
        'duplicate_rate_percent': round(duplicate_rate, 2),
        'duplicates_found': num_duplicate_drawings > 0,
        'duplicate_details': duplicate_details
    }

    return report, df

if __name__ == "__main__":
    clean_data_file = Path("/tmp/powerball-study/data/powerball_clean.csv")

    print("Running Study 1: Duplicate Drawing Analysis...")
    report, df = analyze_duplicates(clean_data_file)

    # Print summary
    print("\n" + "="*60)
    print(f"Total number of drawings: {report['total_drawings']}")
    print(f"Number of duplicate drawings: {report['number_of_duplicate_drawings']}")
    print(f"Duplicate rate: {report['duplicate_rate_percent']}%")
    print("="*60)

    if report['duplicates_found']:
        print("\n⚠️  DUPLICATES FOUND!")
        for dup in report['duplicate_details']:
            print(f"\nDrawing: {dup['white_balls']} + {dup['powerball']}")
            print(f"Count: {dup['count']} times")
            print(f"Dates: {', '.join(dup['dates'])}")
    else:
        print("\n✓ No identical duplicate drawings found in the dataset!")

    # Save report
    results_dir = Path("/tmp/powerball-study/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Save as JSON
    with open(results_dir / "study1_results.json", "w") as f:
        json.dump(report, f, indent=2, default=str)

    # Save as text
    with open(results_dir / "study1_results.txt", "w") as f:
        f.write("POWERBALL STUDY 1: DUPLICATE DRAWING ANALYSIS\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total number of drawings: {report['total_drawings']}\n")
        f.write(f"Number of duplicate drawings: {report['number_of_duplicate_drawings']}\n")
        f.write(f"Duplicate rate: {report['duplicate_rate_percent']}%\n\n")

        if report['duplicates_found']:
            f.write("DUPLICATES FOUND:\n")
            f.write("-" * 60 + "\n")
            for dup in report['duplicate_details']:
                f.write(f"\nDrawing: {' '.join(map(str, dup['white_balls']))} + {dup['powerball']}\n")
                f.write(f"Occurrence count: {dup['count']}\n")
                f.write(f"Dates:\n")
                for date in dup['dates']:
                    f.write(f"  - {date}\n")
        else:
            f.write("No identical duplicate drawings found in the dataset.\n")

    print(f"\nResults saved to {results_dir}")
