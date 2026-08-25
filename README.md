# Fantasy Football Lineup Optimizer

## What it does

The Fantasy Football Lineup Optimizer builds an optimal fantasy football lineup for the user based off of live ESPN data of their team in their league.
This app looks at the roster, sees the average fantasy points per game, and puts the players in the respective positions.
It accounts for constraints such as position eligibility and one player per slot.

## Setup

1. Clone the repo
2. Create and activate the venv (python -m venv venv) (venv\Scripts\activate)
3. Install dependencies (pip install espn_api)
4. Create your own config.py needing your league ID and ESPN cookies by manually getting your SWID/espn_S2 from browser cookies for any private leagues
```
LEAGUE_ID = 123456
YEAR = 2026
SWID = "{your-swid-here}"
ESPN_S2 = "your-espn-s2-here"
```
5. Run by typing python main.py in the terminal

## How it works

I started with treating this app as a budget-constrained optimization problem. Each player would have a salary and the goal is to build the best roster under a shared budget.
I did not go with this as roster slots must be filled. This caused the chosen algorithm to change. There is no budget to optimize.
In place, I built a recursive, memoized algorithm that assigns players to slots(positions) correctly handling FLEX-eligible players.
It tracks a set of used players instead of a shrinking numeric budget.

## Foundations

This folder shows the progression and building blocks to build the app.
(hash sets -> two pointers -> recursion -> memoized knapsack -> memoized slot-assignment)

## Example output

Total Score: 122.32

QB -> Brock Purdy
RB -> Jahmyr Gibbs
RB -> Kenneth Walker III
WR -> Malik Nabers
WR -> Zay Flowers
TE -> Sam LaPorta
FLEX -> D'Andre Swift
D/ST -> Lions D/ST
K -> Eddy Pineiro
