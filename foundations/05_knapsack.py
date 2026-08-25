# You have a knapsack that can hold a max weight of capacity.
# You're given a list of items, each with a weight and a value.
# Choose a subset of items - each item can be used at most once - so the total weight doesn't exceed capacity,
# and the total value is as large as possible. Return the max value achievable.

# Example: capacity = 10, items = [(weight = 6, value = 30), (weight = 4, value = 40), (weight = 5, value = 50)] -> best answer is 90 (pick the last two: weight 4 + 5 <= 10, value 40 + 50 = 90).
import time
import random

def knap(capacity, items, index, memo={}):
    if index >= len(items):
        return 0;

    elif (index, capacity) in memo:
        return memo[(index, capacity)]

    else:
        weight = items[index][0]
        value = items[index][1]
        skip = knap(capacity, items, index+1, memo)
        include = knap(capacity - weight, items, index+1, memo) + value

        if weight > capacity:
            memo[(index, capacity)] = skip
            return memo[(index, capacity)]
        else:
            memo[(index, capacity)] = max(skip, include)
            return memo[(index, capacity)]

print(knap(10, [(6, 30), (4, 40), (5, 50)], 0))

random.seed(1)
big_items = [(random.randint(1, 20), random.randint(10, 100)) for _ in range(20)]

start = time.time()
print(knap(50, big_items, 0))
end = time.time()
print(f"Took {end - start:.4f} seconds")