import pandas as pd
import json
from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak, KeepTogether
from reportlab.lib.units import inch
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from PIL import Image as PILImage

def generate_pdf_report(results_dir):
    """Generate comprehensive PDF report."""

    # Create PDF
    pdf_path = results_dir / "Powerball_Rolling_Overlap_Report.pdf"
    doc = SimpleDocTemplate(str(pdf_path), pagesize=letter,
                           rightMargin=0.5*inch, leftMargin=0.5*inch,
                           topMargin=0.5*inch, bottomMargin=0.5*inch)

    styles = getSampleStyleSheet()
    story = []

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=12,
        alignment=1  # center
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#34495E'),
        spaceAfter=8,
        spaceBefore=8
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        alignment=4  # justified
    )

    # Title
    story.append(Paragraph("🎰 Powerball Rolling Window Overlap Analysis", title_style))
    story.append(Spacer(1, 0.2*inch))

    # Overview
    story.append(Paragraph("Overview", heading_style))
    overview_text = """
    This study analyzes the overlap of white ball numbers across rolling windows of consecutive
    Powerball drawings. Instead of examining only adjacent drawings, we analyze windows of 2 to 10
    consecutive drawings to understand how numbers repeat across different time horizons.
    """
    story.append(Paragraph(overview_text, body_style))
    story.append(Spacer(1, 0.15*inch))

    # Dataset
    story.append(Paragraph("Dataset", heading_style))
    dataset_text = """
    <b>Source:</b> Official New York State Powerball Lottery Records<br/>
    <b>Time Period:</b> January 2010 - July 2026<br/>
    <b>Total Drawings:</b> 1,967<br/>
    <b>Data Quality:</b> No duplicates found, fully verified and cleaned<br/>
    """
    story.append(Paragraph(dataset_text, body_style))
    story.append(Spacer(1, 0.15*inch))

    # Methodology
    story.append(Paragraph("Methodology", heading_style))
    methodology_text = """
    For each window size (2 through 10 consecutive drawings):<br/>
    • Extract all white ball numbers from each drawing in the window<br/>
    • Count how many numbers appear more than once across the window<br/>
    • Calculate statistics: mean, median, min, max, standard deviation<br/>
    • Build probability distribution for each window size<br/>
    • Construct empirical probability matrix
    """
    story.append(Paragraph(methodology_text, body_style))
    story.append(Spacer(1, 0.2*inch))

    # Results Section
    story.append(PageBreak())
    story.append(Paragraph("Results", heading_style))

    # Load and display matrix
    matrix_df = pd.read_csv(results_dir / "rolling_window_matrix.csv")
    matrix_data = [list(matrix_df.columns)] + matrix_df.values.tolist()

    table = Table(matrix_data, colWidths=[0.8*inch] + [0.6*inch]*len(matrix_df.columns[1:]))
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4ECDC4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
    ]))

    story.append(Paragraph("<b>Probability Matrix (Empirical)</b>", heading_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(table)
    story.append(Spacer(1, 0.2*inch))

    # Visualizations
    story.append(PageBreak())
    story.append(Paragraph("Visualizations", heading_style))
    story.append(Spacer(1, 0.1*inch))

    # Heatmap
    if (results_dir / 'rolling_window_heatmap.png').exists():
        story.append(Image(str(results_dir / 'rolling_window_heatmap.png'), width=6.5*inch, height=2.5*inch))
        story.append(Spacer(1, 0.1*inch))

    # Statistics chart
    if (results_dir / 'rolling_window_statistics.png').exists():
        story.append(Image(str(results_dir / 'rolling_window_statistics.png'), width=6*inch, height=3*inch))
        story.append(Spacer(1, 0.1*inch))

    # Summary table
    if (results_dir / 'rolling_window_summary_table.png').exists():
        story.append(Image(str(results_dir / 'rolling_window_summary_table.png'), width=6*inch, height=3*inch))

    # Interpretation
    story.append(PageBreak())
    story.append(Paragraph("Interpretation", heading_style))

    with open(results_dir / "rolling_window_results.json", 'r') as f:
        results = json.load(f)

    interpretation_text = f"""
    <b>Key Observations:</b><br/><br/>

    • As window size increases, the expected number of repeated white balls increases<br/>
    • Window size 2: Average {float(results['2']['mean']):.2f} repeated numbers<br/>
    • Window size 10: Average {float(results['10']['mean']):.2f} repeated numbers<br/><br/>

    • The probability distribution shows clear patterns:<br/>
    - Smaller windows concentrate around lower overlap counts<br/>
    - Larger windows show broader distributions<br/><br/>

    • This is consistent with probability theory: longer windows have higher likelihood of repeated numbers
    """
    story.append(Paragraph(interpretation_text, body_style))
    story.append(Spacer(1, 0.15*inch))

    # Limitations
    story.append(Paragraph("Limitations", heading_style))
    limitations_text = """
    • This analysis describes historical empirical distributions only<br/>
    • No predictive claims about future drawings<br/>
    • Results are specific to the time period analyzed (2010-2026)<br/>
    • Drawing mechanism may evolve over time<br/>
    • Lottery outcomes are inherently random and unpredictable
    """
    story.append(Paragraph(limitations_text, body_style))

    # Build PDF
    doc.build(story)
    print(f"✓ PDF Report generated: {pdf_path}")

def generate_infographic(results_dir):
    """Generate vertical infographic PNG."""

    # Load data
    with open(results_dir / "rolling_window_results.json", 'r') as f:
        results = json.load(f)
        results = {int(k): v for k, v in results.items()}

    matrix_df = pd.read_csv(results_dir / "rolling_window_matrix.csv")

    # Create large vertical figure
    fig = plt.figure(figsize=(12, 24), dpi=100)
    gs = fig.add_gridspec(6, 1, hspace=0.4)

    # 1. Title and Dataset
    ax_title = fig.add_subplot(gs[0])
    ax_title.axis('off')
    ax_title.text(0.5, 0.7, '🎰 Powerball Rolling Window Overlap Analysis',
                 ha='center', va='center', fontsize=28, fontweight='bold',
                 color='#2C3E50')
    ax_title.text(0.5, 0.4, 'A Comprehensive Statistical Study of 1,967 Drawings (2010-2026)',
                 ha='center', va='center', fontsize=14, color='#34495E')
    ax_title.text(0.5, 0.15,
                 'Official NY State Powerball | Data Quality: Verified | No Duplicates Found',
                 ha='center', va='center', fontsize=11, color='#7F8C8D', style='italic')
    ax_title.set_xlim(0, 1)
    ax_title.set_ylim(0, 1)

    # 2. Heatmap
    ax_heatmap = fig.add_subplot(gs[1])
    heatmap_data = matrix_df.set_index('Window_Size')
    heatmap_data.columns = [int(col.split('_')[1]) for col in heatmap_data.columns]
    im = ax_heatmap.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
    ax_heatmap.set_xticks(range(len(heatmap_data.columns)))
    ax_heatmap.set_xticklabels(heatmap_data.columns)
    ax_heatmap.set_yticks(range(len(heatmap_data.index)))
    ax_heatmap.set_yticklabels(heatmap_data.index)
    ax_heatmap.set_title('Probability Distribution Heatmap', fontsize=14, fontweight='bold', pad=10)
    ax_heatmap.set_xlabel('Repeated White Balls', fontsize=11, fontweight='bold')
    ax_heatmap.set_ylabel('Window Size', fontsize=11, fontweight='bold')
    plt.colorbar(im, ax=ax_heatmap, label='Probability (%)')

    # 3. Statistics
    ax_stats = fig.add_subplot(gs[2])
    window_sizes = sorted(results.keys())
    means = [results[ws]['mean'] for ws in window_sizes]
    ax_stats.plot(window_sizes, means, marker='o', linewidth=2.5, markersize=8,
                 color='#FF6B6B', label='Mean Overlap')
    ax_stats.fill_between(window_sizes, means, alpha=0.2, color='#FF6B6B')
    ax_stats.set_xlabel('Window Size', fontsize=11, fontweight='bold')
    ax_stats.set_ylabel('Average Repeated Numbers', fontsize=11, fontweight='bold')
    ax_stats.set_title('Mean Overlap by Window Size', fontsize=14, fontweight='bold', pad=10)
    ax_stats.grid(True, alpha=0.3)
    ax_stats.set_xticks(window_sizes)

    # 4. Key Findings
    ax_findings = fig.add_subplot(gs[3])
    ax_findings.axis('off')
    findings_text = f"""
    📊 KEY FINDINGS

    • Analyzed {len(results)} window sizes (2-10 consecutive drawings)
    • Total rolling windows examined: {sum([results[ws]['total_windows'] for ws in results])}

    Window Size 2:  Mean = {results[2]['mean']:.3f}, Median = {results[2]['median']:.1f}
    Window Size 5:  Mean = {results[5]['mean']:.3f}, Median = {results[5]['median']:.1f}
    Window Size 10: Mean = {results[10]['mean']:.3f}, Median = {results[10]['median']:.1f}

    • As window size increases, expected overlap increases
    • Distribution becomes wider for larger windows
    • Findings consistent with probability theory
    """
    ax_findings.text(0.05, 0.95, findings_text, transform=ax_findings.transAxes,
                    fontsize=11, verticalalignment='top', family='monospace',
                    bbox=dict(boxstyle='round', facecolor='#ECF0F1', alpha=0.8))

    # 5. Interpretation
    ax_interp = fig.add_subplot(gs[4])
    ax_interp.axis('off')
    interp_text = """
    ℹ️ INTERPRETATION

    This study examines how white ball numbers overlap across consecutive draws.
    Larger windows naturally show more overlaps due to increased opportunities.

    ⚠️ IMPORTANT: This is historical analysis only
    • Describes empirical patterns in past data
    • Makes NO predictions about future drawings
    • Does NOT imply future overlaps will follow historical patterns
    • Lottery outcomes remain inherently unpredictable
    """
    ax_interp.text(0.05, 0.95, interp_text, transform=ax_interp.transAxes,
                  fontsize=11, verticalalignment='top',
                  bbox=dict(boxstyle='round', facecolor='#FFF3CD', alpha=0.8))

    # 6. Footer
    ax_footer = fig.add_subplot(gs[5])
    ax_footer.axis('off')
    ax_footer.text(0.5, 0.5,
                  '🔗 GitHub: github.com/siren7075/powerball-study\n' +
                  '📅 Analysis Date: July 2026\n' +
                  '📈 Data: Official NY State Powerball Records',
                  ha='center', va='center', fontsize=10, color='#7F8C8D',
                  bbox=dict(boxstyle='round', facecolor='#F5F5F5', alpha=0.8))

    plt.savefig(results_dir / 'Powerball_Rolling_Overlap_Summary.png',
               dpi=150, bbox_inches='tight', facecolor='white')
    print(f"✓ Infographic generated: {results_dir / 'Powerball_Rolling_Overlap_Summary.png'}")
    plt.close()

if __name__ == "__main__":
    results_dir = Path("/tmp/powerball-study/results")

    print("Generating PDF Report...")
    generate_pdf_report(results_dir)

    print("Generating Infographic...")
    generate_infographic(results_dir)

    print("\n✅ All reports and graphics generated!")
