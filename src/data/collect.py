from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder

#step 1: static team lookup - no network all, just bundled data
nba_teams = teams.get_teams()
celtics = [t for t in nba_teams if t['abbreviation'] == 'BOS'][0]
print("Celtics team id:", celtics['id'])

#step 2: live api call - pull recent celtics games
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=celtics['id'])
games = gamefinder.get_data_frames()[0]
print(games.head())
print("Total games returned:", len(games))