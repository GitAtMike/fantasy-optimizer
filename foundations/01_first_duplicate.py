# Given a list of numbers, find the first number that appears twice.
# Example: [3, 1, 4, 1, 5, 9] -> return 1
# Do it in one pass, no nested loops.

def first_duplicate(nums):
    numsSet = set()
    for i in nums:
        if i in numsSet:
            return i
        else:
            numsSet.add(i)

print(first_duplicate([3, 1, 4, 1, 5, 9]))
