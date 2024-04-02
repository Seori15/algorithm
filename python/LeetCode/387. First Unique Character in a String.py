class Solution:
    def firstUniqChar(self, s: str) -> int:
		# [1] Setting dictionary
        char = {}
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            char[letter] = 0
        # [2] First loop : counting letters with dictionary
        for letter in s:
            char[letter] += 1
        # [3] Second loop : finding letter whose count is 1.
        for letter in s:
            if char[letter] == 1:
                return s.index(letter)
        return -1