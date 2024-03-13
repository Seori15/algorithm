class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # [1] Sort arr
        arr.sort()

        # [2] Find Minimum Absolute Difference
        minV = 2 * 10 ** 6
        for i in range(len(arr) - 1):
            minV = min(minV, arr[i + 1] - arr[i])

        # [3] Append pairs having Minimum Absolute Difference
        answer = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minV:
                answer.append([arr[i], arr[i + 1]])
        return answer