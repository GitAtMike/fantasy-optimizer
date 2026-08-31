# Filters out injured players from a roster
def filter_healthy_players(roster):
    allowList = {"ACTIVE", "NORMAL", "QUESTIONABLE"}
    healthyPlayers = []
    for player in roster:
        if isinstance(player.injuryStatus, str): # Checks if the injuryStatus is a string, as some players may have an empty list for injuryStatus such as the defense/special teams position
                if (player.injuryStatus in allowList):
                    healthyPlayers.append(player)
        else:
            healthyPlayers.append(player)
    return healthyPlayers

# Builds a list of slots based on the position_slot_counts dictionary from the league settings
def build_slots(position_slot_counts):
    slots=[]
    for position in ["QB", "RB", "WR", "TE", "RB/WR/TE", "D/ST", "K"]:
        if position in ["RB/WR/TE"]: # ESPN uses RB/WR/TE for the FLEX position, so to show FLEX in the output, we need to add it to the slots list for each FLEX position in the league settings
             slots += ["FLEX"] * position_slot_counts["RB/WR/TE"]
        else:
            slots += [position] * position_slot_counts[position]
    return slots

# Builds a list of player tuples based on the roster and the current week, where each tuple contains the player's name, position, projected points for the current week, and eligible slots
def build_player_tuples(roster, week):
    players = []
    for player in roster:
        playerInfo = (player.name, player.position, player.stats.get(week, {}).get('projected_points', 0), player.eligibleSlots) # Subs a 0 for projected points if the player does not have a projection for the current week
        players.append(playerInfo)
    return players