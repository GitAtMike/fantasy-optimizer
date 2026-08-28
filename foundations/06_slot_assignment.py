def fillSlot(slot, slots, playerList, usedPlayers, memo=None): # slot = position we are trying to fill, slots = positions available, playerList = list of players, usedPlayers = set of players already used in roster using their indices in the list
    if memo is None:
        memo = {} # Memoization dictionary to store previously computed results for specific slot and usedPlayers combinations
    if slot >= len(slots): # Checks amount of positions, if no position is filled
        return (0, [])
    elif (slot, frozenset(usedPlayers)) in memo:
        return memo[(slot, frozenset(usedPlayers))]
    else:
        eligiblePlayers = []
        for playerIndex, player in enumerate(playerList): # Gets a list of eligible players for a position
            if ((slots[slot] in player[3]) or (slots[slot] == "FLEX" and "RB/WR/TE" in player[3])) and playerIndex not in usedPlayers: # FLEX gets it's own check due to multiple positions being eligible
                eligiblePlayers.append(playerIndex)
        if len(eligiblePlayers) == 0: # If no eligible players are found for a position, stops immediately and raises an error
            raise ValueError(f"No eligible players found for position {slots[slot]}.")
        bestScore = 0
        bestAssignment = []
        for candidate in eligiblePlayers: # Gets the best score for a position
            score, assignments = fillSlot(slot + 1, slots, playerList, usedPlayers | {candidate}, memo)
            bestPossibleScore = playerList[candidate][2] + score # Gets the best score per player on the roster and provides the total
            if bestPossibleScore > bestScore:
                bestScore = bestPossibleScore
                bestAssignment = [(slot, candidate)] + assignments #gets the candidate with the slot and it's assignment
        memo[(slot, frozenset(usedPlayers))] = (bestScore, bestAssignment)
        return memo[(slot, frozenset(usedPlayers))] # Returns the best score and assignment in the line up
players = [
    ("Mahomes", "QB", 22, ["QB"]),
    ("Gibbs", "RB", 18, ["RB", "RB/WR/TE"]),
    ("Nabers", "WR", 16, ["WR", "RB/WR/TE"]),
]

slots = ["QB", "FLEX"]

resultScore, resultAssignment = fillSlot(0, slots, players, set())
print(resultScore)
print(resultAssignment)