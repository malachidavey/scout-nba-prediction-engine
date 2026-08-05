import pandas as pd

df = pd.read_csv("data/raw/games.csv")

print("Printing df.shape: ",df.shape)
print("Printing columns: ", df.columns)

print("Printing null values: ", df.isnull().sum())

game_counts = df['GAME_ID'].value_counts()
not_two = game_counts[game_counts != 2]
print("Printing games without exactly 2 rows: ", not_two)

null_row = df[df['FT_PCT'].isnull()]
print("Printing rows with null FT_PCT: ", null_row[['GAME_DATE', 'TEAM_ABBREVIATION', 'MATCHUP', 'FTA', 'FTM', 'FT_PCT']])