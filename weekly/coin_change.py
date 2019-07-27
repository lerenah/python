cache = {}

def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    if amount < 0:
        return float('inf')
    if amount == 0:
        return 0
    if amount in cache:
        return cache[amount]
    else:
        cache[amount] = min(1 + coinChange(coins, amount - coin) for coin in coins)

    return cache[amount]
