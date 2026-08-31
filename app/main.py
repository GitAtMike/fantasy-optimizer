from espn_api.football import League
from config import LEAGUE_ID, YEAR, SWID, ESPN_S2, MY_TEAM_NAME
from data import build_slots, filter_healthy_players, build_player_tuples
from optimizer import fillSlot
import math

league = League(league_id=LEAGUE_ID, year=YEAR, swid=SWID, espn_s2=ESPN_S2)

slots = build_slots(league.settings.position_slot_counts)

# Gets the home and away teams for the current week and determines which is the user's team and which is the opponent's team
for team in league.scoreboard():
    if team.home_team.team_name == MY_TEAM_NAME:
        opponentTeam = team.away_team
        opponentTeamName = opponentTeam.team_name
    elif team.away_team.team_name == MY_TEAM_NAME:
        opponentTeam = team.home_team
        opponentTeamName = opponentTeam.team_name

# Builds the user's optimal roster and calculates the total score for that roster, then prints out the total score and the players in each slot
for team in league.teams:
    if team.team_name == MY_TEAM_NAME:
        fullHealthyRoster = filter_healthy_players(team.roster)
        fullBuiltRoster = build_player_tuples(fullHealthyRoster,league.current_week)
        finalRosterScore, finalRosterBuild = fillSlot(0, slots, fullBuiltRoster, set(), {})

myTotalScore = math.floor(finalRosterScore * 10) / 10
print(f"\nMy Total Score: {myTotalScore}\n")
for slot_index, player_index in finalRosterBuild:
    print(slots[slot_index], "->", fullBuiltRoster[player_index][0])

# Calculates the opponent's actual score and builds a list of their lineup by slot.
# Gets the opponent's actual roster instead of the optimal as this is what the user is competing against
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

# Prints out the opponent's lineup by slot, popping players off the list to ensure that if there are multiple players in a slot, they are printed in the order they were added to the list
for position in slots:
    if position in lineupBySlot and lineupBySlot[position]:
        print(position, "->", lineupBySlot[position].pop())

print("\n")

print(f"Your score: {myTotalScore}\n")
print(f"{opponentTeamName}'s score: {opponentTotalScore}\n")

# Compares the user's total score to the opponent's total score and prints out whether the user is projected to win, lose, or tie
if finalRosterScore > opponentActualScore:
    print(f"You are projected to win by {math.floor((myTotalScore - opponentTotalScore) * 10) / 10} points.")
elif finalRosterScore == opponentActualScore:
    print("You are projected to tie.")
else:
    print(f"You are projected to lose by {math.floor((opponentTotalScore - myTotalScore) * 10) / 10} points.")

print("\n")


freeAgentHealthyRoster = filter_healthy_players(league.free_agents())
freeAgentBuiltRoster = build_player_tuples(freeAgentHealthyRoster,league.current_week)

# Compares the user's roster to the free agent pool and prints out any potential upgrades for each position in the user's roster
# Slot-by-slot comparison used due to time complexity of fillSlot with a large free agent pool
for slot_index, play_index in finalRosterBuild:
    bestPoints = 0
    bestName = None
    for freeAgent in freeAgentBuiltRoster:
        if ((slots[slot_index] in freeAgent[3]) or (slots[slot_index] == "FLEX" and "RB/WR/TE" in freeAgent[3])):
            if freeAgent[2] > bestPoints:
                bestPoints = freeAgent[2]
                bestName = freeAgent[0]
    if bestPoints > fullBuiltRoster[play_index][2]:
        print(f"Slot: {slots[slot_index]} | Current Player: {fullBuiltRoster[play_index][0]} ({fullBuiltRoster[play_index][2]}) | Best Free Agent: {bestName} ({bestPoints})")
