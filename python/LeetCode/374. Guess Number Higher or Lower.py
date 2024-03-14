class Solution:
    def guessNumber(self, n: int) -> int:
		    # [1] Continue binary search until we find right mid value.
        left, right = 1, n
        while True:
            mid = (left + right) // 2
            if guess(mid) == 1:
                left = mid + 1
            elif guess(mid) == -1:
                right = mid - 1
            else:
                return mid