"""
Analysis: Why Avoiding Previous Numbers Doesn't Increase Your Odds

This script addresses a common misconception about lottery strategy.
"""

import math
from pathlib import Path

def calculate_powerball_odds():
    """Calculate Powerball odds."""
    # Choose 5 white balls from 69
    white_combinations = math.comb(69, 5)
    # Choose 1 powerball from 26
    powerball_options = 26
    # Total combinations
    total_combinations = white_combinations * powerball_options

    return white_combinations, total_combinations

def analyze_misconception():
    """
    Analyze the misconception: "If I avoid numbers from the last drawing,
    I'll have better odds of winning."

    The Logic (Flawed):
    - Last drawing had 5 white balls: A, B, C, D, E
    - Those balls won't appear again next time
    - So if I avoid A, B, C, D, E, my odds improve!

    Why It's Wrong:
    """

    white_combos, total_combos = calculate_powerball_odds()

    print("=" * 80)
    print("LOTTERY ODDS ANALYSIS: WHY AVOIDING PREVIOUS NUMBERS DOESN'T WORK")
    print("=" * 80)
    print()

    print("BASIC FACTS:")
    print(f"  • Total white balls available: 69")
    print(f"  • White balls to select: 5")
    print(f"  • Total white ball combinations: {white_combos:,}")
    print(f"  • Powerball options: 26")
    print(f"  • Total possible combinations: {total_combos:,}")
    print(f"  • Odds of winning jackpot: 1 in {total_combos:,}")
    print()

    print("=" * 80)
    print("THE MISCONCEPTION")
    print("=" * 80)
    print()
    print("CLAIM: 'If last drawing was {1, 5, 23, 45, 67}, I should avoid these")
    print("       numbers. Then my odds improve!'")
    print()
    print("WHY THIS SOUNDS LOGICAL:")
    print("  1. We know those 5 numbers already appeared (they're 'used up')")
    print("  2. Our study shows only 65.82% chance of ANY overlap with consecutive draws")
    print("  3. So logically, avoiding them should improve our odds...")
    print()

    print("=" * 80)
    print("WHY IT'S MATHEMATICALLY WRONG")
    print("=" * 80)
    print()

    print("KEY INSIGHT: Your odds depend on TOTAL COMBINATIONS, not your strategy.")
    print()

    print("SCENARIO A: You avoid {1, 5, 23, 45, 67}")
    print("-" * 80)
    print(f"  • You now have 64 numbers to choose from (69 - 5 avoided)")
    print(f"  • You need to select 5 from these 64")
    combos_a = math.comb(64, 5)
    print(f"  • Your possible combinations: {combos_a:,}")
    print(f"  • You can only win if:")
    print(f"    - Your 5 numbers match the 5 drawn")
    print(f"    - AND those 5 are all from your restricted 64")
    print(f"  • If the drawing includes any of the 5 you avoided → YOU LOSE")
    print(f"  • Your actual winning odds: 0% if any avoided number is drawn")
    print()

    print("SCENARIO B: You don't avoid anything (normal play)")
    print("-" * 80)
    print(f"  • You have all 69 numbers available")
    print(f"  • You need to select 5 from 69")
    print(f"  • Your possible combinations: {white_combos:,}")
    print(f"  • You can win if your 5 match the 5 drawn")
    print(f"  • Your odds: 1 in {white_combos:,} (for white balls)")
    print()

    print("=" * 80)
    print("THE MATHEMATICAL TRUTH")
    print("=" * 80)
    print()

    print("FACT 1: Independence")
    print("  • Each drawing is completely independent")
    print("  • Last drawing's numbers don't affect this drawing's probability")
    print("  • The machine doesn't 'remember' previous draws")
    print()

    print("FACT 2: Equal Probability")
    print("  • ANY combination of 5 numbers has equal probability")
    print("  • {1, 2, 3, 4, 5} has same odds as {1, 5, 23, 45, 67}")
    print("  • Picking 'all 1s' has same odds as picking 'all different'")
    print(f"  • All have: 1 in {white_combos:,} chance")
    print()

    print("FACT 3: Why Avoiding Numbers REDUCES Your Options")
    print("  • If you avoid 5 numbers, you have fewer combinations")
    print("  • Fewer combinations = LESS chance to match (not more!)")
    print("  • You're voluntarily reducing your odds")
    print()

    print("=" * 80)
    print("WHAT OUR STUDY ACTUALLY SHOWS")
    print("=" * 80)
    print()

    print("Our Rolling Window Analysis Found:")
    print("  ✓ 65.82% of consecutive draws have ZERO overlap")
    print("  ✓ This is a HISTORICAL OBSERVATION")
    print("  ✓ It describes PAST patterns")
    print()

    print("What This DOES NOT Mean:")
    print("  ✗ It doesn't predict future outcomes")
    print("  ✗ It doesn't suggest a winning strategy")
    print("  ✗ It doesn't mean avoiding numbers helps")
    print()

    print("What This DOES Mean:")
    print("  ✓ Numbers change frequently between draws")
    print("  ✓ The lottery is working as a random system")
    print("  ✓ There's no predictable pattern to exploit")
    print()

    print("=" * 80)
    print("ANALOGY: COIN FLIPS")
    print("=" * 80)
    print()

    print("Imagine a coin flip:")
    print("  • Last 10 flips were all HEADS")
    print("  • Does that mean next flip is more likely to be TAILS?")
    print("  • NO! It's still 50-50")
    print()
    print("Lottery is the same:")
    print("  • Previous numbers don't influence next drawing")
    print("  • Your strategy of 'avoiding' doesn't change odds")
    print("  • You can't improve on 1 in 300-million odds")
    print()

    print("=" * 80)
    print("FINAL ANSWER: WHY YOU SHOULDN'T AVOID NUMBERS")
    print("=" * 80)
    print()

    print("1. MATHEMATICALLY: It reduces your available combinations")
    print("2. STATISTICALLY: All combinations have equal probability")
    print("3. LOGICALLY: Independence means history doesn't matter")
    print("4. PRACTICALLY: No strategy can improve lottery odds")
    print()

    print("THE BEST STRATEGY:")
    print("  ✓ Pick numbers you like (odds are identical)")
    print("  ✓ Play for entertainment, not investment")
    print("  ✓ Don't spend money you can't afford to lose")
    print("  ✓ Understand the true odds (1 in 292 million)")
    print()

    print("=" * 80)

if __name__ == "__main__":
    analyze_misconception()
