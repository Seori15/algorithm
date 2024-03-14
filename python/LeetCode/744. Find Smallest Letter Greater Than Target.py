class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # [1] By binary search, find left which is index of string greater than target.
        left, right = 0, len(letters) - 1
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            elif letters[mid] <= target:
                left = mid + 1

		# [2] If left was found, return letters[left].
        if letters[left] > target:
            return letters[left]
        # [3] If target is the biggest, return first character.
        else:
            return letters[0]   