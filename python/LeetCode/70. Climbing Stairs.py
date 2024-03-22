class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0, 1, 2] + [0 for _ in range(43)]
        for i in range(3, n+1):
            ways[i] = ways[i-2] + ways[i-1]
        return ways[n]