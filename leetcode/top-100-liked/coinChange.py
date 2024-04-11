class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            j = coins[i]
            while j <= amount:
                if dp[j - coins[i]] != inf:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
                j += 1
        if dp[amount] == inf:
            return -1
        return dp[amount]
