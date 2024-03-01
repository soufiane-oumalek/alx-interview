#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    coin_index = 0
    while coin_index < len(coins):
        coin = coins[coin_index]
        curr_total = coin

        while curr_total <= total:
            dp[curr_total] = min(dp[curr_total], dp[curr_total - coin] + 1)
            current_total += 1

        coin_index += 1
    return dp[total] if dp[total] != float('inf') else -1
