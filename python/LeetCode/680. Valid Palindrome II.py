class Solution:
    def validPalindrome(self, s: str) -> bool:
        # [0] Setting variables
        length = len(s)
        start = 0
        end = length - 1

        # [1] Reading s from start and end at the same time
        # [1-1] If it keeps going, s is palindrome. return True
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1

            # [1-2] However if start/end are not the same, try 2 more cases. 'a' & 'b'
            #       'a' means removing 'start letter', and 'b' means 'end letter' here.
            #       If one of them is palindrome, return True
            else:
                a = s[start:end]
                b = s[start + 1:end + 1]
                return a == a[::-1] or b == b[::-1]
        return True