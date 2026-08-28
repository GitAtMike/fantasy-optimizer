import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))
from optimizer import fillSlot

def test_fillSlot():
    players = [
        ("Mahomes", "QB", 22, ["QB"]),
        ("Gibbs", "RB", 18, ["RB", "RB/WR/TE"]),
        ("Nabers", "WR", 16, ["WR", "RB/WR/TE"]),
    ]

    slots = ["QB", "FLEX"]

    resultScore, resultAssignment = fillSlot(0, slots, players, set())

    assert resultScore == 40
    assert resultAssignment == [(0, 0), (1, 1)]