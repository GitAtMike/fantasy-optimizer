def filter_healthy_players(roster):
    allowList = {"ACTIVE", "NORMAL", "QUESTIONABLE"}
    healthyPlayers = []
    for player in roster:
        if isinstance(player.injuryStatus, str):
                if (player.injuryStatus in allowList):
                    healthyPlayers.append(player)
        else:
            healthyPlayers.append(player)
    return healthyPlayers

def build_slots(position_slot_counts):
    slots=[]
    for position in ["QB", "RB", "WR", "TE", "RB/WR/TE", "D/ST", "K"]:
        if position in ["RB/WR/TE"]:
             slots += ["FLEX"] * position_slot_counts["RB/WR/TE"]
        else:
            slots += [position] * position_slot_counts[position]
    return slots

def build_player_tuples(roster, week):
    players = []
    for player in roster:
        playerInfo = (player.name, player.position, player.stats.get(week, {}).get('projected_points', 0), player.eligibleSlots)
        players.append(playerInfo)
    return players