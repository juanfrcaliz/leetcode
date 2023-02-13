# Given two non-negative integers `low` and `high`.
# Return the count of odd numbers between `low` and `high` (inclusive).

def count_odds(low: int, high: int) -> int:
    import math
    count = math.ceil((high - low) / 2)
    if low % 2 != 0 and high % 2 != 0:
        count += 1
    return count
