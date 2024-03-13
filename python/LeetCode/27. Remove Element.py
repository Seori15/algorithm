# 첫 번째 풀이. 정렬 36ms 16.64MB
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [1] Return value = total length of nums - count(val)
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                nums[i] = 51
                length -= 1

        # [2] Since the output is nums[k]; I need to change nums.
        #     51 is over max value for this question, so it works for sort.
        nums.sort()
        return length


# 두 번째 풀이. pop 35ms 16.58MB
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [1] Pop every val from right
        length = len(nums)
        for i in range(length - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
                length -= 1

        return length


# 세 번째 풀이. 투 포인터 선택 정렬 32ms 16.59MB
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [1] Send all vals to the right by two pointers
        length = len(nums)
        left, right = 0, length - 1
        cnt = 0
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                length -= 1
                continue
            left += 1

        return length
