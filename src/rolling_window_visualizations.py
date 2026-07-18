import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import json
from pathlib import Path
import seaborn as sns

def create_heatmap(matrix_df, results_dir):
    """Create probability heatmap."""

    # Prepare data for heatmap
    heatmap_data = matrix_df.set_index('Window_Size')
    heatmap_data.columns = [int(col.split('_')[1]) for col in heatmap_data.columns]
    heatmap_data = heatmap_data.sort_index(axis=1)

    fig, ax = plt.subplots(figsize=(14, 6))

    sns.heatmap(heatmap_data, annot=True, fmt='.1f', cmap='YlOrRd',
                cbar_kws={'label': 'Probability (%)'}, ax=ax, linewidths=0.5)

    ax.set_title('Rolling Window Overlap Analysis: Probability Heatmap',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('Number of Repeated White Balls', fontsize=12, fontweight='bold')
    ax.set_ylabel('Window Size (consecutive drawings)', fontsize=12, fontweight='bold')

    plt.tight_layout()
    plt.savefig(results_dir / 'rolling_window_heatmap.png', dpi=300, bbox_inches='tight')
    print("Saved: rolling_window_heatmap.png")
    plt.close()

def create_grouped_bar_chart(results, results_dir):
    """Create grouped bar chart comparing window sizes."""

    window_sizes = sorted(results.keys())
    means = [results[ws]['mean'] for ws in window_sizes]
    medians = [results[ws]['median'] for ws in window_sizes]
    stds = [results[ws]['std'] for ws in window_sizes]

    x = np.arange(len(window_sizes))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))

    bars1 = ax.bar(x - width, means, width, label='Mean', color='#FF6B6B', alpha=0.8)
    bars2 = ax.bar(x, medians, width, label='Median', color='#4ECDC4', alpha=0.8)
    bars3 = ax.bar(x + width, stds, width, label='Std Dev', color='#95E1D3', alpha=0.8)

    ax.set_xlabel('Window Size', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Repeated White Balls', fontsize=12, fontweight='bold')
    ax.set_title('Rolling Window Statistics by Window Size',
                 fontsize=14, fontweight='bold', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(window_sizes)
    ax.legend(fontsize=11)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.2f}', ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.savefig(results_dir / 'rolling_window_statistics.png', dpi=300, bbox_inches='tight')
    print("Saved: rolling_window_statistics.png")
    plt.close()

def create_summary_table(results, results_dir):
    """Create and save summary table."""

    table_data = []
    for window_size in sorted(results.keys()):
        stats = results[window_size]
        table_data.append({
            'Window Size': window_size,
            'Mean Overlaps': f"{stats['mean']:.3f}",
            'Median': f"{stats['median']:.1f}",
            'Min': stats['min'],
            'Max': stats['max'],
            'Std Dev': f"{stats['std']:.3f}"
        })

    summary_df = pd.DataFrame(table_data)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')

    table = ax.table(cellText=summary_df.values,
                     colLabels=summary_df.columns,
                     cellLoc='center',
                     loc='center',
                     colWidths=[0.15, 0.15, 0.15, 0.15, 0.15, 0.15])

    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1, 2.5)

    # Style header
    for i in range(len(summary_df.columns)):
        table[(0, i)].set_facecolor('#4ECDC4')
        table[(0, i)].set_text_props(weight='bold', color='white')

    # Alternate row colors
    for i in range(1, len(summary_df) + 1):
        color = '#F0F0F0' if i % 2 == 0 else 'white'
        for j in range(len(summary_df.columns)):
            table[(i, j)].set_facecolor(color)

    plt.title('Rolling Window Analysis: Summary Statistics',
              fontsize=14, fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(results_dir / 'rolling_window_summary_table.png', dpi=300, bbox_inches='tight')
    print("Saved: rolling_window_summary_table.png")
    plt.close()

if __name__ == "__main__":
    results_dir = Path("/tmp/powerball-study/results")

    # Load results
    with open(results_dir / "rolling_window_results.json", 'r') as f:
        results = json.load(f)
        # Convert string keys to int
        results = {int(k): v for k, v in results.items()}

    # Load matrix
    matrix_df = pd.read_csv(results_dir / "rolling_window_matrix.csv")

    print("Generating visualizations...")
    create_heatmap(matrix_df, results_dir)
    create_grouped_bar_chart(results, results_dir)
    create_summary_table(results, results_dir)
    print("\nAll visualizations generated!")
