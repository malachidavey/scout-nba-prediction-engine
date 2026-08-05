
import time
import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

SEASONS = [
    "2018-19", "2019-20", "2020-21", "2021-22", 
    "2022-23", "2023-24", "2024-25", "2025-26"
]

def get_season_games(season: str) -> pd.DataFrame:
    # Put all teams' regular season games for one season.
    gamefinder = leaguegamefinder.LeagueGameFinder(
        season_nullable=season,
        season_type_nullable="Regular Season",
    )
    return gamefinder.get_data_frames()[0]

def main():
    all_seasons = []

    for season in SEASONS:
        print(f"Fetching {season}...")
        season_df = get_season_games(season)
        all_seasons.append(season_df)
        time.sleep(1)  # avoid hammering api back-to-back

    all_games = pd.concat(all_seasons, ignore_index=True)

    print("Total rows: ", len(all_games))
    print("Seasons included: ", sorted(all_games['SEASON_ID'].unique()))

    all_games.to_csv("data/raw/games.csv", index=False)
    print("Data saved to data/raw/games.csv")

if __name__ == "__main__":
    main()