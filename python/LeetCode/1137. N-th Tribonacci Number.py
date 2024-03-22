class Solution:
    def tribonacci(self, n: int) -> int:
        tribonacci = [0, 1, 1] + [0 for _ in range(35)]
        for i in range(3, n+1):
            tribonacci[i] = tribonacci[i-3] + tribonacci[i-2] + tribonacci[i-1]
        return tribonacci[n]