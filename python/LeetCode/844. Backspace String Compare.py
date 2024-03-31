from collections import deque
class Solution:
		# [A] typing() returns typed letters
    def typing(self, s: str) -> list:
        typed = deque()
        for letter in s:
            if letter == '#':
                if len(typed) == 0:
                    continue
                typed.pop()
            else:
                typed.append(letter)
        return typed

		# [1] by typing(), we have two typed letters
		#			compare them and return True or False
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.typing(s) == self.typing(t)