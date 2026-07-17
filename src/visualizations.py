import pandas as pd
import matplotlib.pyplot as plt
import json
from pathlib import Path

def create_visualizations(clean_data_file, results_json_file):
    """Create visualizations for the Powerball analysis."""

    # Read data
    df = pd.read_csv(clean_data_file)
    df['Date'] = pd.to_datetime(df['Date'])

    with open(results_json_file, 'r') as f:
        report = json.load(f)

    results_dir = Path("/tmp/powerball-study/results")
    results_dir.mkdir(parents=True, exist_ok=True)

    # Figure 1: Summary statistics
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Powerball Study 1: Duplicate Drawing Analysis', fontsize=16, fontweight='bold')

    # Plot 1: Total vs Unique drawings
    ax = axes[0, 0]
    total = report['total_drawings']
    unique = total - report['number_of_duplicate_drawings']
    ax.bar(['Total Drawings', 'Unique Drawings'], [total, unique], color=['#FF6B6B', '#4ECDC4'])
    ax.set_ylabel('Count')
    ax.set_title('Total vs Unique Drawings')
    for i, v in enumerate([total, unique]):
        ax.text(i, v + 5, str(v), ha='center', fontweight='bold')

    # Plot 2: Duplicate rate
    ax = axes[0, 1]
    dup_rate = report['duplicate_rate_percent']
    ax.pie([dup_rate, 100 - dup_rate],
           labels=['Duplicates', 'Unique'],
           autopct='%1.2f%%',
           colors=['#FF6B6B', '#4ECDC4'],
           startangle=90)
    ax.set_title('Duplicate Rate')

    # Plot 3: White ball frequency
    ax = axes[1, 0]
    all_white_balls = []
    for col in ['White1', 'White2', 'White3', 'White4', 'White5']:
        all_white_balls.extend(df[col].values)

    white_counts = pd.Series(all_white_balls).value_counts().sort_index()
    ax.bar(white_counts.index, white_counts.values, color='#95E1D3')
    ax.set_xlabel('White Ball Number')
    ax.set_ylabel('Frequency')
    ax.set_title('White Ball Number Frequency Distribution')
    ax.grid(axis='y', alpha=0.3)

    # Plot 4: Powerball frequency
    ax = axes[1, 1]
    powerball_counts = df['Powerball'].value_counts().sort_index()
    ax.bar(powerball_counts.index, powerball_counts.values, color='#FFD93D')
    ax.set_xlabel('Powerball Number')
    ax.set_ylabel('Frequency')
    ax.set_title('Powerball Number Frequency Distribution')
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    plt.savefig(results_dir / 'study1_summary.png', dpi=300, bbox_inches='tight')
    print(f"Saved visualization: {results_dir / 'study1_summary.png'}")

    # Figure 2: Drawing timeline
    fig, ax = plt.subplots(figsize=(14, 6))

    # Count drawings per month
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_counts = df['YearMonth'].value_counts().sort_index()
    monthly_counts.index = monthly_counts.index.to_timestamp()

    ax.plot(monthly_counts.index, monthly_counts.values, marker='o', linewidth=2, markersize=5, color='#4ECDC4')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Drawings')
    ax.set_title('Powerball Drawings per Month Over Time')
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(results_dir / 'drawing_timeline.png', dpi=300, bbox_inches='tight')
    print(f"Saved visualization: {results_dir / 'drawing_timeline.png'}")

    # Figure 3: Summary stats text
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.axis('off')

    summary_text = f"""
    POWERBALL STUDY 1: DUPLICATE DRAWING ANALYSIS
    {'='*50}

    RESULTS SUMMARY:

    Total Number of Drawings: {report['total_drawings']:,}
    Number of Duplicate Drawings: {report['number_of_duplicate_drawings']}
    Duplicate Rate: {report['duplicate_rate_percent']}%

    """

    if report['duplicates_found']:
        summary_text += f"⚠️  DUPLICATES FOUND!\n"
        summary_text += f"\nDetails:\n"
        for i, dup in enumerate(report['duplicate_details'], 1):
            white_str = ' '.join(map(str, dup['white_balls']))
            summary_text += f"\n{i}. Drawing: {white_str} + {dup['powerball']}\n"
            summary_text += f"   Occurred {dup['count']} times\n"
            summary_text += f"   Dates: {', '.join(dup['dates'])}\n"
    else:
        summary_text += "✓ NO DUPLICATES FOUND\n"
        summary_text += "\nConclusion: Every Powerball drawing in the dataset\n"
        summary_text += "is unique. No identical drawings have occurred."

    ax.text(0.1, 0.5, summary_text, fontsize=12, family='monospace',
            verticalalignment='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig(results_dir / 'study1_summary_text.png', dpi=300, bbox_inches='tight')
    print(f"Saved visualization: {results_dir / 'study1_summary_text.png'}")

    plt.close('all')
    print("\nAll visualizations generated successfully!")

if __name__ == "__main__":
    clean_data_file = Path("/tmp/powerball-study/data/powerball_clean.csv")
    results_json_file = Path("/tmp/powerball-study/results/study1_results.json")

    create_visualizations(clean_data_file, results_json_file)
