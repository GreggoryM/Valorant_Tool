# Get the ranked leaderboard of a region and print the
# top players. Shows leaderboard rank, game name, and
# number of wins. See documentation on `Client.get_leaderboard`
# for more info.

import os
import valorant

KEY = os.environ["VALPY-KEY"]

# Set our client's region to EU. Client uses NA by default.
client = valorant.Client(KEY, region="na")

# Get the top 15 players on the Ranked Leaderboard.
lb = client.get_leaderboard(size=25)

print("Top Players in NA:\n")

# Print all players on the leaderboard.
for p in lb.players:
    print(f"#{p.leaderboardRank} - {p.gameName} ({p.numberOfWins} wins, {p.rankedRating} rank, {p.puuid})")

total_players = lb.totalPlayers

total_players2 = lb.pages

print(total_players)

print(total_players2)