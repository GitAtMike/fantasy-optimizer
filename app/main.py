from espn_api.football import League
from config import LEAGUE_ID, YEAR, SWID, ESPN_S2, MY_TEAM_NAME
from data import build_slots, filter_healthy_players, build_player_tuples
from optimizer import fillSlot
import math

league = League(league_id=LEAGUE_ID, year=YEAR, swid=SWID, espn_s2=ESPN_S2)

slots = build_slots(league.settings.position_slot_counts)

for team in league.scoreboard():
    if team.home_team.team_name == MY_TEAM_NAME:
        opponentTeam = team.away_team
        opponentTeamName = opponentTeam.team_name
    elif team.away_team.team_name == MY_TEAM_NAME:
        opponentTeam = team.home_team
        opponentTeamName = opponentTeam.team_name

for team in league.teams:
    if team.team_name == MY_TEAM_NAME:
        fullHealthyRoster = filter_healthy_players(team.roster)
        fullBuiltRoster = build_player_tuples(fullHealthyRoster,league.current_week)
        finalRosterScore, finalRosterBuild = fillSlot(0, slots, fullBuiltRoster, set(), {})

myTotalScore = math.floor(finalRosterScore * 10) / 10
print(f"\nMy Total Score: {myTotalScore}\n")
for slot_index, player_index in finalRosterBuild:
    print(slots[slot_index], "->", fullBuiltRoster[player_index][0])

opponentActualScore = 0
lineupBySlot = {}
for player in opponentTeam.roster:
    if player.lineupSlot == "BE" or player.lineupSlot == "IR":
        continue
    opponentActualScore += player.stats[league.current_week]['projected_points']
    if player.lineupSlot == "RB/WR/TE":
        key = "FLEX"
    else:
        key = player.lineupSlot
    if key not in lineupBySlot:
        lineupBySlot[key] = []
    lineupBySlot[key].append(player.name)

opponentTotalScore = math.floor(opponentActualScore * 10) / 10
print(f"\nOpponent Total Score: {opponentTotalScore}\n")

for position in slots:
    if position in lineupBySlot and lineupBySlot[position]:
        print(position, "->", lineupBySlot[position].pop())

print("\n")

print(f"Your score: {myTotalScore}\n")
print(f"{opponentTeamName}'s score: {opponentTotalScore}\n")

if finalRosterScore > opponentActualScore:
    print(f"You are projected to win by {math.floor((myTotalScore - opponentTotalScore) * 10) / 10} points.")
elif finalRosterScore == opponentActualScore:
    print("You are projected to tie.")
else:
    print(f"You are projected to lose by {math.floor((opponentTotalScore - myTotalScore) * 10) / 10} points.")

print("\n")