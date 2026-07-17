import pandas as pd
from pathlib import Path

def clean_powerball_data(input_file):
    """Clean raw Powerball data and standardize format."""

    # Read raw data
    df = pd.read_csv(input_file)

    # Rename columns for clarity
    df = df.rename(columns={
        'Draw Date': 'Date',
        'Winning Numbers': 'winning_numbers'
    })

    # Parse the winning numbers (5 white balls + 1 powerball)
    def parse_winning_numbers(winning_str):
        """Parse 'W1 W2 W3 W4 W5 PB' format into separate columns."""
        parts = winning_str.split()
        if len(parts) != 6:
            return None, None, None, None, None, None
        try:
            return int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5])
        except:
            return None, None, None, None, None, None

    # Apply parsing
    parsed = df['winning_numbers'].apply(lambda x: parse_winning_numbers(x))

    df['White1'] = parsed.apply(lambda x: x[0])
    df['White2'] = parsed.apply(lambda x: x[1])
    df['White3'] = parsed.apply(lambda x: x[2])
    df['White4'] = parsed.apply(lambda x: x[3])
    df['White5'] = parsed.apply(lambda x: x[4])
    df['Powerball'] = parsed.apply(lambda x: x[5])

    # Convert date to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort by date
    df = df.sort_values('Date').reset_index(drop=True)

    # Select only the columns we need
    clean_df = df[['Date', 'White1', 'White2', 'White3', 'White4', 'White5', 'Powerball']].copy()

    # Drop any rows with missing values
    clean_df = clean_df.dropna()

    return clean_df

if __name__ == "__main__":
    input_file = Path("/Users/lynnzic/Downloads/Tech/powerball/export.csv")

    print(f"Reading data from {input_file}")
    clean_df = clean_powerball_data(input_file)

    # Save cleaned data
    output_dir = Path("/tmp/powerball-study/data")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "powerball_clean.csv"

    clean_df.to_csv(output_file, index=False)
    print(f"Saved cleaned data to {output_file}")
    print(f"Total rows: {len(clean_df)}")
    print("\nFirst 5 rows:")
    print(clean_df.head())
