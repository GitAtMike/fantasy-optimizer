import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))
from types import SimpleNamespace
from data import filter_healthy_players, build_slots, build_player_tuples

def test_filter_healthy_players():
    objectOne = SimpleNamespace(name="Test Player One", injuryStatus="ACTIVE")
    objectTwo = SimpleNamespace(name="Test Player Two", injuryStatus="INJURED")
    objectThree = SimpleNamespace(name="Test Player Three", injuryStatus="NORMAL")
    objectFour = SimpleNamespace(name="Test Player Four", injuryStatus=[])
    players = [objectOne, objectTwo, objectThree, objectFour]
    healthy_players = filter_healthy_players(players)
    assert len(healthy_players) == 3
    assert healthy_players[0] == objectOne
    assert healthy_players[1] == objectThree
    assert healthy_players[2] == objectFour

def test_build_slots():
    position_slot_counts = {
        "QB": 1,
        "RB": 2,
        "WR": 2,
        "TE": 1,
        "RB/WR/TE": 1,
        "D/ST": 1,
        "K": 1
    }
    slots = build_slots(position_slot_counts)
    assert slots == ["QB", "RB", "RB", "WR", "WR", "TE", "FLEX", "D/ST", "K"]

def test_build_player_tuples():
    objectOne = SimpleNamespace(name="Test Player One", position="QB", stats={1: {'projected_points': 10}}, eligibleSlots=["QB"])
    objectTwo = SimpleNamespace(name="Test Player Two", position="RB", stats={1: {'projected_points': 15}}, eligibleSlots=["RB", "RB/WR/TE"])
    objectThree = SimpleNamespace(name="Test Player Three", position="WR", stats={1: {'projected_points': 20}}, eligibleSlots=["WR", "RB/WR/TE"])
    objectFour = SimpleNamespace(name="Test Player Four", position="K", stats={}, eligibleSlots=["K"])
    players = [objectOne, objectTwo, objectThree, objectFour]
    player_tuples = build_player_tuples(players, 1)
    assert player_tuples == [
        ("Test Player One", "QB", 10, ["QB"]),
        ("Test Player Two", "RB", 15, ["RB", "RB/WR/TE"]),
        ("Test Player Three", "WR", 20, ["WR", "RB/WR/TE"]),
        ("Test Player Four", "K", 0, ["K"])
    ]