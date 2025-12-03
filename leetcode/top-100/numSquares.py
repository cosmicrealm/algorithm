class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = i
            j = 1
            while i - j**2 >= 0:
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                j += 1
        return dp[n]
