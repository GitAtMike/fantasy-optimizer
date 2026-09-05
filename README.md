# Fantasy Football Lineup Optimizer

## What it does

The Fantasy Football Lineup Optimizer builds an optimal fantasy football lineup for the user based off of live ESPN data of their team in their league.
This app looks at the roster, sees the average fantasy points per game, and puts the players in the respective positions.
It accounts for constraints such as position eligibility and one player per slot.
Compares user's most optimal lineup against opponent's current lineup and compares the two scores.
Surfaces free-agent pool slot-by-slot and provides suggestions if a free-agent provides more points at a given position.

## Setup

1. Clone the repo
2. Create and activate the venv (python -m venv venv) (venv\Scripts\activate)
3. Install dependencies (pip install -r requirements.txt)
4. Create your own config.py needing your league ID and ESPN cookies by manually getting your SWID/espn_S2 from browser cookies for any private leagues
```
LEAGUE_ID = 123456
YEAR = 2026
SWID = "{your-swid-here}"
ESPN_S2 = "your-espn-s2-here"
MY_TEAM_NAME = "Your Team Name"
```
5. Run by typing python main.py in the terminal

## How it works

I started with treating this app as a budget-constrained optimization problem. Each player would have a salary and the goal is to build the best roster under a shared budget.
I did not go with this as roster slots must be filled. This caused the chosen algorithm to change. There is no budget to optimize.
In place, I built a recursive, memoized algorithm that assigns players to slots(positions) correctly handling FLEX-eligible players.
It tracks a set of used players instead of a shrinking numeric budget.
For free-agent comparisons, I initially was going to use fillSlot to compare free agents with roster, but hit exponential slowdown once the pool got larger.
Switched to a slot-by-slot comparison to increase speed.

## Foundations

This folder shows the progression and building blocks to build the app.
(hash sets -> two pointers -> recursion -> memoized knapsack -> memoized slot-assignment)

## Tests

These tests verify that the program runs as it is intended.
The core algorithm is put against toy data with an expected pass or fail dependent on the toy data values.
test_optimizer.py tests the fill_slot algorithm.
test_data.py tests the data-shaping functions including any edge cases.
The test locks in on a known correct-answer. If the algorithm breaks, the test will catch it.
```
Command: pytest
```

## Example output
```
My Total Score: 120.6

QB -> Patrick Mahomes
RB -> Kenneth Walker III
RB -> Jahmyr Gibbs
WR -> Malik Nabers
WR -> Zay Flowers
TE -> Sam LaPorta
FLEX -> D'Andre Swift
D/ST -> Lions D/ST
K -> Eddy Pineiro

Opponent Total Score: 125.9

QB -> Jalen Hurts
RB -> Jadarian Price
RB -> Chase Brown
WR -> Carnell Tate
WR -> Puka Nacua
TE -> Trey McBride
FLEX -> Jameson Williams
D/ST -> Eagles D/ST
K -> Jason Myers

Your score: 120.6
the 67 , s's score: 125.9
You are projected to lose by 5.3 points.

Slot: QB | Current Player: Patrick Mahomes (15.5) | Best Free Agent: Kyler Murray (16.39)
Slot: K | Current Player: Eddy Pineiro (8.7) | Best Free Agent: Chris Boswell (9.02)
```