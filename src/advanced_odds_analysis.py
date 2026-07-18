"""
Advanced Lottery Analysis: Does Avoiding Numbers Increase Chances of Winning Something?

User Question: "Even if I can't win jackpot, can I win MORE smaller prizes
               by avoiding previous numbers?"

This analysis breaks it down by prize tier.
"""

import math
from scipy.special import comb

def analyze_prize_tiers():
    """Analyze all Powerball prize tiers."""

    print("=" * 90)
    print("POWERBALL PRIZE TIERS & PROBABILITIES")
    print("=" * 90)
    print()

    # Prize structure
    prizes = {
        'Jackpot (6 of 6)': {
            'white_match': 5,
            'powerball_match': True,
            'odds': 1/292201338,
            'approx_winnings': 100000000
        },
        'Match 5 + PB': {
            'white_match': 5,
            'powerball_match': True,
            'odds': 1/11238513,
            'approx_winnings': 1000000
        },
        'Match 5 white': {
            'white_match': 5,
            'powerball_match': False,
            'odds': 1/292199216,
            'approx_winnings': 2000000
        },
        'Match 4 + PB': {
            'white_match': 4,
            'powerball_match': True,
            'odds': 1/913129,
            'approx_winnings': 50000
        },
        'Match 4 white': {
            'white_match': 4,
            'powerball_match': False,
            'odds': 1/36525,
            'approx_winnings': 100
        },
        'Match 3 + PB': {
            'white_match': 3,
            'powerball_match': True,
            'odds': 1/14494,
            'approx_winnings': 100
        },
        'Match 3 white': {
            'white_match': 3,
            'powerball_match': False,
            'odds': 1/580,
            'approx_winnings': 7
        },
        'Match 2 + PB': {
            'white_match': 2,
            'powerball_match': True,
            'odds': 1/701,
            'approx_winnings': 7
        },
        'Match 1 + PB': {
            'white_match': 1,
            'powerball_match': True,
            'odds': 1/91,
            'approx_winnings': 4
        },
        'Match PB only': {
            'white_match': 0,
            'powerball_match': True,
            'odds': 1/38,
            'approx_winnings': 3
        }
    }

    for prize, data in prizes.items():
        print(f"{prize}")
        print(f"  Odds: 1 in {int(1/data['odds']):,}")
        print()

    print("=" * 90)
    print("THE QUESTION: Should I Avoid Previous Numbers?")
    print("=" * 90)
    print()

    print("YOUR THEORY:")
    print("-" * 90)
    print("  Last drawing: {1, 5, 23, 45, 67}")
    print("  I avoid these 5, pick: {2, 3, 4, 6, 7}")
    print()
    print("  If next drawing has many of the same numbers (65.82% don't overlap)")
    print("  Then I'm MORE likely to have 0 overlaps with their selection")
    print("  But I might match 4 or 5 numbers randomly!")
    print()
    print("  Doesn't that increase my chance of winning SOMETHING?")
    print()

    print("=" * 90)
    print("THE MATHEMATICAL REALITY")
    print("=" * 90)
    print()

    print("CRITICAL INSIGHT: Probability of matching K numbers is INDEPENDENT")
    print("                  of WHICH 5 numbers you choose")
    print()

    print("PROOF:")
    print("-" * 90)
    print()

    print("Let's calculate: P(match exactly 4 white balls)")
    print()

    # Probability of matching exactly 4 white balls (any selection)
    # Choose 4 from my 5 selections * Choose 1 from remaining 64
    ways_match_4 = comb(5, 4, exact=True) * comb(64, 1, exact=True)
    total_ways = comb(69, 5, exact=True)
    prob_match_4 = ways_match_4 / total_ways

    print(f"  Ways to match exactly 4 of MY 5 numbers: {ways_match_4:,}")
    print(f"  Total possible white ball combinations: {total_ways:,}")
    print(f"  Probability: {prob_match_4:.6f} or 1 in {int(1/prob_match_4):,}")
    print()

    print("KEY QUESTION: Does this probability change based on WHICH 5 I pick?")
    print()
    print("ANSWER: NO! Here's why:")
    print()

    print("  The formula doesn't depend on what numbers you choose!")
    print("  P(match 4) = C(5,4) × C(64,1) / C(69,5)")
    print()
    print("  This calculation is IDENTICAL whether you pick:")
    print("    • {1, 2, 3, 4, 5}")
    print("    • {2, 3, 4, 6, 7}  (avoiding previous numbers)")
    print("    • {65, 66, 67, 68, 69}")
    print()

    print("=" * 90)
    print("DETAILED SCENARIO ANALYSIS")
    print("=" * 90)
    print()

    print("SCENARIO: Last drawing was {1, 5, 23, 45, 67}")
    print()

    print("CASE 1: You play NORMALLY (select any 5)")
    print("-" * 90)
    print("  Your selection: {1, 5, 23, 45, 67}  (same as last)")
    print()
    print("  Next drawing possibilities:")
    print()
    print("  Sub-case A: {1, 5, 23, 45, 68}")
    print("    You match: 4 white balls → WIN (prize tier payment)")
    print()
    print("  Sub-case B: {2, 3, 4, 6, 8}")
    print("    You match: 0 white balls → LOSE")
    print()

    print("CASE 2: You AVOID previous numbers")
    print("-" * 90)
    print("  Your selection: {2, 3, 4, 6, 7}  (avoiding 1,5,23,45,67)")
    print()
    print("  Next drawing possibilities:")
    print()
    print("  Sub-case A: {1, 5, 23, 45, 68}")
    print("    You match: 0 white balls (none of your numbers) → LOSE")
    print()
    print("  Sub-case B: {2, 3, 4, 6, 8}")
    print("    You match: 4 white balls → WIN (same prize as Case 1, Sub-A)")
    print()

    print("THE KEY POINT:")
    print("-" * 90)
    print("  • In Case 1, Sub-A: You won when numbers mostly repeated")
    print("  • In Case 2, Sub-A: You lost when numbers mostly repeated")
    print()
    print("  • In Case 1, Sub-B: You lost when numbers were all different")
    print("  • In Case 2, Sub-B: You won when numbers were all different")
    print()
    print("  Avoiding numbers doesn't CREATE more winning opportunities")
    print("  It just SHIFTS which situations benefit you")
    print("  And since it reduces total combinations, you have LESS overall")
    print()

    print("=" * 90)
    print("PROBABILITY DISTRIBUTION")
    print("=" * 90)
    print()

    # Calculate probabilities for different matching scenarios
    print("If you select 5 from 69 numbers, what's your probability for each tier?")
    print()

    match_scenarios = {
        5: ("Match all 5", comb(5, 5, exact=True) * comb(64, 0, exact=True)),
        4: ("Match exactly 4", comb(5, 4, exact=True) * comb(64, 1, exact=True)),
        3: ("Match exactly 3", comb(5, 3, exact=True) * comb(64, 2, exact=True)),
        2: ("Match exactly 2", comb(5, 2, exact=True) * comb(64, 3, exact=True)),
        1: ("Match exactly 1", comb(5, 1, exact=True) * comb(64, 4, exact=True)),
        0: ("Match 0", comb(5, 0, exact=True) * comb(64, 5, exact=True)),
    }

    total = comb(69, 5, exact=True)

    for matches in [5, 4, 3, 2, 1, 0]:
        desc, ways = match_scenarios[matches]
        prob = ways / total
        print(f"  {desc:20s}: {ways:>12,} ways ({prob*100:6.3f}%) = 1 in {int(1/prob):>12,}")

    print()
    print("CRUCIAL FINDING:")
    print("-" * 90)
    print("  These probabilities are the SAME for ANY selection of 5 numbers")
    print("  Whether you avoid previous numbers or not!")
    print()

    print("=" * 90)
    print("EXPECTED VALUE ANALYSIS")
    print("=" * 90)
    print()

    print("If you play $1 and win $X, your 'expected value' is:")
    print("  E(value) = P(win) × $X")
    print()

    print("Let's compare: Normal play vs. Avoiding previous numbers")
    print()

    print("NORMAL PLAY:")
    print("  Combinations available: 11,238,513")
    print("  ÷ Powerball options: 26")
    print("  = Unique tickets: 11,238,513 × 26")
    print()

    print("AVOIDING PREVIOUS 5:")
    print("  Combinations available: 7,624,512")
    print("  ÷ Powerball options: 26")
    print("  = Unique tickets: 7,624,512 × 26")
    print()

    print("RESULT:")
    print("  You have FEWER possible tickets")
    print("  Fewer tickets = LOWER chance of any win")
    print("  Lower chance = WORSE expected value")
    print()

    print("=" * 90)
    print("FINAL ANSWER")
    print("=" * 90)
    print()

    print("Q: If I avoid previous numbers, can I win MORE smaller prizes?")
    print()
    print("A: NO. Here's why:")
    print()
    print("  1. MATHEMATICALLY:")
    print("     - P(match K numbers) is independent of which numbers you choose")
    print("     - Avoiding numbers doesn't change these probabilities")
    print()
    print("  2. COMBINATORIALLY:")
    print("     - You reduce from 11.2M to 7.6M combinations (32% fewer)")
    print("     - Fewer combinations = LOWER chance of ANY win")
    print()
    print("  3. LOGICALLY:")
    print("     - You're just shifting which scenarios benefit you")
    print("     - But with fewer total tickets to match")
    print()
    print("  4. EMPIRICALLY:")
    print("     - Expected value = (probability of win) × (prize money)")
    print("     - Your probability goes DOWN (fewer combinations)")
    print("     - Your expected value goes DOWN")
    print()

    print("CONCLUSION:")
    print("─" * 90)
    print("  ✗ You CANNOT increase your chances by avoiding previous numbers")
    print("  ✗ You CANNOT increase your expected winnings")
    print("  ✗ You're just reducing your available combinations")
    print()
    print("  ✓ The lottery is truly random")
    print("  ✓ All strategies have identical odds")
    print("  ✓ Pick whatever numbers you want - odds are the same")
    print()

if __name__ == "__main__":
    analyze_prize_tiers()
