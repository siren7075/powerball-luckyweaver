import pandas as pd
import matplotlib.pyplot as plt
import json
from pathlib import Path

def create_extended_visualizations(results_dir):
    """Create visualizations for Study 2 and Study 3."""

    # Load Study 2 data
    with open(results_dir / "study2_results.json", 'r') as f:
        study2 = json.load(f)

    with open(results_dir / "study3_results.json", 'r') as f:
        study3 = json.load(f)

    # Study 2 Visualization
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Study 2: Consecutive Drawing Overlap Analysis', fontsize=14, fontweight='bold')

    # Plot 1: Overlap distribution
    ax = axes[0]
    overlap_data = study2['overlap_distribution']
    overlaps = [d['Overlap'] for d in overlap_data]
    counts = [d['Count'] for d in overlap_data]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8', '#F7DC6F'][:len(overlaps)]

    ax.bar(overlaps, counts, color=colors, edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Number of Overlapping White Balls')
    ax.set_ylabel('Frequency (consecutive pairs)')
    ax.set_title('Distribution of Overlaps Between Consecutive Drawings')
    ax.set_xticks(overlaps)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for i, (x, y) in enumerate(zip(overlaps, counts)):
        ax.text(x, y + 20, str(y), ha='center', fontweight='bold')

    # Plot 2: Overlap percentage
    ax = axes[1]
    probs = [d['Probability'] for d in overlap_data]
    labels = [f"{o} overlap\n({p}%)" for o, p in zip(overlaps, probs)]

    colors_pie = plt.cm.Set3(range(len(overlaps)))
    wedges, texts, autotexts = ax.pie(counts, labels=labels, autopct='%1.1f%%',
                                        colors=colors_pie, startangle=90)
    ax.set_title('Proportion of Each Overlap Level')

    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    plt.tight_layout()
    plt.savefig(results_dir / 'study2_overlap_analysis.png', dpi=300, bbox_inches='tight')
    print(f"Saved: {results_dir / 'study2_overlap_analysis.png'}")

    # Study 3 Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Study 3: Number Patterns Analysis', fontsize=14, fontweight='bold')

    # Plot 1: Hot vs Cold numbers
    ax = axes[0, 0]
    hot_nums = list(study3['hot_numbers']['top_10'].keys())[:5]
    hot_counts = list(study3['hot_numbers']['top_10'].values())[:5]
    cold_nums = list(study3['cold_numbers']['bottom_10'].keys())[-5:]
    cold_counts = list(study3['cold_numbers']['bottom_10'].values())[-5:]

    x_pos = range(len(hot_nums) + len(cold_nums) + 1)
    all_nums = hot_nums + [''] + cold_nums
    all_counts = hot_counts + [0] + cold_counts
    colors = ['#FF6B6B']*len(hot_nums) + ['white'] + ['#4ECDC4']*len(cold_nums)

    ax.bar(x_pos, all_counts, color=colors, edgecolor='black', linewidth=1)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(all_nums)
    ax.set_ylabel('Frequency')
    ax.set_title('Hot Numbers (Left) vs Cold Numbers (Right)')
    ax.axhline(y=study3['total_white_ball_occurrences']/69, color='green',
               linestyle='--', alpha=0.5, label='Expected Average')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Plot 2: Even/Odd distribution
    ax = axes[0, 1]
    even_count = study3['even_odd_distribution']['even_count']
    odd_count = study3['even_odd_distribution']['odd_count']

    colors = ['#FFD93D', '#6BCB77']
    wedges, texts, autotexts = ax.pie([even_count, odd_count],
                                        labels=['Even', 'Odd'],
                                        autopct='%1.1f%%',
                                        colors=colors,
                                        startangle=90)
    ax.set_title(f'Even/Odd Distribution\n(Total: {even_count + odd_count} draws)')

    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontweight('bold')

    # Plot 3: Number distribution (heatmap style)
    ax = axes[1, 0]
    # Create frequency for each number 1-69
    freq_dict = {}
    # Read from clean data to get frequencies
    clean_df = pd.read_csv(Path("/tmp/powerball-study/data/powerball_clean.csv"))
    all_whites = []
    for col in ['White1', 'White2', 'White3', 'White4', 'White5']:
        all_whites.extend(clean_df[col].values)

    for i in range(1, 70):
        freq_dict[i] = all_whites.count(i)

    nums = list(range(1, 70))
    freqs = [freq_dict[n] for n in nums]

    # Color code by frequency
    colors_list = ['#FF6B6B' if f > 160 else '#4ECDC4' if f < 140 else '#95E1D3'
                   for f in freqs]

    ax.bar(nums, freqs, color=colors_list, edgecolor='lightgray', linewidth=0.5)
    ax.set_xlabel('White Ball Number')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency Distribution of All White Ball Numbers (1-69)')
    ax.axhline(y=sum(freqs)/len(freqs), color='green', linestyle='--', alpha=0.5, label='Average')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)

    # Plot 4: Gap analysis
    ax = axes[1, 1]
    # Simulate gap distribution
    gaps_data = {
        '1-2': 0,
        '3-5': 0,
        '6-10': 0,
        '11-20': 0,
        '20+': 0
    }

    clean_df = pd.read_csv(Path("/tmp/powerball-study/data/powerball_clean.csv"))
    for i in range(len(clean_df)):
        balls = sorted([clean_df.iloc[i]['White1'], clean_df.iloc[i]['White2'],
                       clean_df.iloc[i]['White3'], clean_df.iloc[i]['White4'],
                       clean_df.iloc[i]['White5']])
        for j in range(len(balls) - 1):
            gap = balls[j+1] - balls[j]
            if gap <= 2:
                gaps_data['1-2'] += 1
            elif gap <= 5:
                gaps_data['3-5'] += 1
            elif gap <= 10:
                gaps_data['6-10'] += 1
            elif gap <= 20:
                gaps_data['11-20'] += 1
            else:
                gaps_data['20+'] += 1

    ax.bar(gaps_data.keys(), gaps_data.values(), color='#FF6B6B', edgecolor='black', linewidth=1.5)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Gap Distribution Between Consecutive Numbers\n(Avg: {study3["number_gaps"]["average_gap"]}, Median: {study3["number_gaps"]["median_gap"]})')
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for i, (k, v) in enumerate(gaps_data.items()):
        ax.text(i, v + 20, str(v), ha='center', fontweight='bold')

    plt.tight_layout()
    plt.savefig(results_dir / 'study3_patterns_analysis.png', dpi=300, bbox_inches='tight')
    print(f"Saved: {results_dir / 'study3_patterns_analysis.png'}")

    plt.close('all')

if __name__ == "__main__":
    results_dir = Path("/tmp/powerball-study/results")
    create_extended_visualizations(results_dir)
    print("\nAll extended visualizations generated successfully!")
