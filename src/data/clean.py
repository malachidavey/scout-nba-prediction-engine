import pandas as pd

def clean_games(df: pd.DataFrame):
    df['FT_PCT'] = df['FT_PCT'].fillna(0)
    df['GAME_DATE'] = pd.to_datetime(df['GAME_DATE'])
    return df

def main():
    df = pd.read_csv("data/raw/games.csv")

    print("Nulls before cleaning: ", df['FT_PCT'].isnull().sum())

    df = clean_games(df)
    print("Nulls after cleaning: ", df['FT_PCT'].isnull().sum())

    df.to_csv("data/processed/games_processed.csv", index=False)

    print(df['GAME_DATE'].dtype)

if __name__ == "__main__":
    main()