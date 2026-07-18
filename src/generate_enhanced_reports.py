import pandas as pd
import json
from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak, KeepTogether
from reportlab.lib.units import inch
import numpy as np

def generate_enhanced_pdf(results_dir, language='EN'):
    """Generate enhanced PDF with markdown content and compact matrix."""

    if language == 'CN':
        pdf_path = results_dir / "reports" / "Powerball_Rolling_Window_Report_CN.pdf"
        title = "Powerball 滚动窗口重叠分析报告"
        sections = {
            'overview': "项目概述",
            'dataset': "数据集",
            'methodology': "方法论",
            'findings': "主要发现",
            'matrix': "概率矩阵",
            'entertainment': "娱乐性预测分析",
            'interpretation': "解释与启示",
            'limitations': "局限性",
            'visualizations': "可视化分析"
        }

        content_dict = {
            'overview': """这是一项对纽约州 Powerball 官方彩票数据的深度统计分析研究。
我们通过分析1,967场彩票抽签（2010-2026），探索相邻抽签之间白球号码的重叠模式。

核心研究方法是使用滚动窗口分析，分析2-10个连续抽签的窗口，建立完整的经验概率矩阵。""",
            'dataset': """来源：官方纽约州 Powerball 彩票数据
时间范围：2010年1月 - 2026年7月
样本量：1,967 场抽签
数据质量：已验证无重复、完全清理、标准化处理""",
            'methodology': """对于每个窗口大小 (2 到 10 个连续抽签)：

1. 从数据集中提取所有可能的连续 N 个抽签的窗口
2. 对于每个窗口，计算有多少个白球号码在该窗口中出现了 2 次或更多次
3. 收集所有重叠计数
4. 计算均值、中位数、最小值、最大值、标准差
5. 构建概率分布（每个重叠数出现的频率和概率）
6. 组装最终的概率矩阵""",
            'findings': """关键发现：

• 窗口越大，重叠数越多（符合概率论）
• 窗口大小 2：平均 0.38 个号码重叠
• 窗口大小 5：平均 3.30 个号码重叠
• 窗口大小 10：平均 11.39 个号码重叠

• 分布随窗口大小发生变化
• 小窗口：分布集中在低重叠数
• 大窗口：分布变宽，向高重叠数倾斜""",
            'entertainment': """娱乐性角度分析：

如果玩家选择避开"前几次最常出现的号码"，理论上的胜率会改变吗？

分析结果：
• 号码频率差异很小（最热175次 vs 最冷88次）
• 这种差异完全符合随机波动
• 避开"热号"或"冷号"都不会改变中奖概率

为什么？
• 彩票每次独立抽签
• 过去的频率不影响未来
• 从数学角度，选择任何5个号码的概率都相同

娱乐建议：
✓ 选择你喜欢的号码 - 概率都是一样的
✓ 不要因为历史频率改变选择
✓ 把彩票当做娱乐，不是投资""",
            'interpretation': """本研究提供了关于 Powerball 彩票历史数据中白球重叠模式的完整统计描述。

重要提示：
• 这是历史分析，不是预测
• 过去的模式不能预测未来
• 彩票结果本质上是随机且不可预测的
• 不存在能改进赢率的策略""",
            'limitations': """• 时间特定性 - 分析基于 2010-2026 数据
• 机制变化 - 彩票规则可能改变
• 无预测价值 - 不能用于预测未来抽签
• 样本量 - 1,967 次抽签虽然不少，但在全概率空间中仍很小"""
        }
    else:  # English
        pdf_path = results_dir / "reports" / "Powerball_Rolling_Window_Report_EN.pdf"
        title = "Powerball Rolling Window Overlap Analysis Report"
        sections = {
            'overview': "Project Overview",
            'dataset': "Dataset",
            'methodology': "Methodology",
            'findings': "Key Findings",
            'matrix': "Probability Matrix",
            'entertainment': "Entertainment Prediction Analysis",
            'interpretation': "Interpretation & Insights",
            'limitations': "Limitations",
            'visualizations': "Visualizations"
        }

        content_dict = {
            'overview': """This is a comprehensive statistical analysis study of official New York State Powerball lottery data.
By analyzing 1,967 lottery drawings (2010-2026), we explore the overlap patterns of white ball numbers across consecutive draws.

The core research method uses rolling window analysis, examining windows of 2-10 consecutive draws and constructing a complete empirical probability matrix.""",
            'dataset': """Source: Official New York State Powerball Lottery Records
Time Period: January 2010 - July 2026
Sample Size: 1,967 drawings
Data Quality: Verified duplicate-free, fully cleaned and standardized""",
            'methodology': """For each window size (2 to 10 consecutive drawings):

1. Extract all possible consecutive N-drawing windows from the dataset
2. For each window, count how many white ball numbers appear 2+ times
3. Collect all overlap counts
4. Calculate mean, median, min, max, and standard deviation
5. Build probability distribution
6. Assemble final probability matrix""",
            'findings': """Key Observations:

• Larger windows show more overlaps (consistent with probability theory)
• Window Size 2: Average 0.38 overlapping numbers
• Window Size 5: Average 3.30 overlapping numbers
• Window Size 10: Average 11.39 overlapping numbers

• Distribution shifts with window size
• Small windows: concentrated on low overlaps
• Large windows: broader distribution, skewed toward high overlaps""",
            'entertainment': """Entertainment Analysis: Avoiding "Hot Numbers"

Question: If a player avoids the "most frequently drawn numbers," does it improve odds?

Analysis Results:
• Number frequency differences are minimal (hottest 175x vs coldest 88x)
• This variation is completely consistent with random fluctuation
• Avoiding "hot" or "cold" numbers does NOT change winning probability

Why Not?
• Each lottery drawing is independent
• Past frequency doesn't affect future outcomes
• Mathematically, ANY selection of 5 numbers has identical probability

Entertainment Recommendations:
✓ Choose numbers you like - odds are the same
✓ Don't change your choice based on history
✓ Treat lottery as entertainment, not investment""",
            'interpretation': """This study provides a complete statistical description of white ball overlap patterns in historical Powerball data.

Important Notes:
• This is historical analysis, NOT prediction
• Past patterns cannot predict future outcomes
• Lottery outcomes are inherently random and unpredictable
• No strategy exists that can improve odds""",
            'limitations': """• Time-Specific: Analysis based on 2010-2026 data only
• Mechanism Changes: Lottery rules may change in future
• No Predictive Value: Cannot be used to predict future drawings
• Sample Size: 1,967 draws are substantial but still small in full probability space"""
        }

    # Create PDF
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
        alignment=1
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#34495E'),
        spaceAfter=8,
        spaceBefore=8
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        alignment=4
    )

    # Title
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.2*inch))

    # Content sections
    for key in ['overview', 'dataset', 'methodology', 'findings']:
        story.append(Paragraph(sections[key], heading_style))
        story.append(Paragraph(content_dict[key], body_style))
        story.append(Spacer(1, 0.15*inch))

    # Probability Matrix (Compact)
    story.append(PageBreak())
    story.append(Paragraph(sections['matrix'], heading_style))

    matrix_df = pd.read_csv(results_dir / "data" / "rolling_window_matrix.csv")

    # Create compact table (only first 10 columns for readability)
    cols_to_show = ['Window_Size', 'Repeated_0', 'Repeated_1', 'Repeated_2',
                    'Repeated_3', 'Repeated_4', 'Repeated_5', 'Repeated_6',
                    'Repeated_7', 'Repeated_8']
    matrix_compact = matrix_df[cols_to_show].copy()

    matrix_data = [list(matrix_compact.columns)] + matrix_compact.values.tolist()

    table = Table(matrix_data, colWidths=[0.7*inch] + [0.65*inch]*9)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4ECDC4')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))

    story.append(table)
    story.append(Spacer(1, 0.1*inch))
    if language == 'CN':
        story.append(Paragraph("<i>注：表格显示前8列重叠数。完整矩阵见 rolling_window_matrix.csv</i>", body_style))
    else:
        story.append(Paragraph("<i>Note: Table shows first 8 overlap columns. Full matrix in rolling_window_matrix.csv</i>", body_style))

    # Entertainment section
    story.append(PageBreak())
    story.append(Paragraph(sections['entertainment'], heading_style))
    story.append(Paragraph(content_dict['entertainment'], body_style))
    story.append(Spacer(1, 0.15*inch))

    # Visualizations
    story.append(PageBreak())
    story.append(Paragraph(sections['visualizations'], heading_style))
    story.append(Spacer(1, 0.1*inch))

    viz_path = results_dir / "visualizations" / "rolling_window_heatmap.png"
    if viz_path.exists():
        story.append(Image(str(viz_path), width=6.5*inch, height=2.5*inch))
        story.append(Spacer(1, 0.1*inch))

    viz_path = results_dir / "visualizations" / "rolling_window_statistics.png"
    if viz_path.exists():
        story.append(Image(str(viz_path), width=6*inch, height=3*inch))

    # Interpretation
    story.append(PageBreak())
    story.append(Paragraph(sections['interpretation'], heading_style))
    story.append(Paragraph(content_dict['interpretation'], body_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(sections['limitations'], heading_style))
    story.append(Paragraph(content_dict['limitations'], body_style))

    # Build PDF
    doc.build(story)
    print(f"✓ PDF generated: {pdf_path.name}")
    return pdf_path

if __name__ == "__main__":
    results_dir = Path("/Users/lynnzic/Downloads/Tech/powerball-study/results")

    print("Generating enhanced reports...\n")

    # Chinese PDF
    print("Creating Chinese PDF...")
    generate_enhanced_pdf(results_dir, language='CN')

    # English PDF
    print("Creating English PDF...")
    generate_enhanced_pdf(results_dir, language='EN')

    print("\n✅ All enhanced reports generated!")
