from espn_api.football import League
from config import LEAGUE_ID, YEAR, SWID, ESPN_S2
from data import build_slots, filter_healthy_players, build_player_tuples
from optimizer import fillSlot

league = League(league_id=LEAGUE_ID, year=YEAR, swid=SWID, espn_s2=ESPN_S2)

slots = build_slots(league.settings.position_slot_counts)
# print(slots)
# print(len(slots))

for team in league.teams:
    if team.team_name == "Mike's Mafia":
        fullHealthyRoster = filter_healthy_players(team.roster)
        fullBuiltRoster = build_player_tuples(fullHealthyRoster)
        finalRosterScore, finalRosterBuild = fillSlot(0, slots, fullBuiltRoster, set(), {})

# print(finalRosterScore, finalRosterBuild)

print(f"Total Score: {finalRosterScore:.2f}\n")
for slot_index, player_index in finalRosterBuild:
    print(slots[slot_index], "->", fullBuiltRoster[player_index][0])