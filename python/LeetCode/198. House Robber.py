class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        # [1] if length < 3: simply return max value.
        if length < 3:
            return max(nums)
        # [2] money[i] means max value at that index from 0 to i.
        #     compare rob or not
        else:
            money = [0 for _ in range(length)]
            money[0] = nums[0]
            money[1] = max(nums[0], nums[1])
            for i in range(2, length):
                money[i] = max(money[i-1], money[i-2] + nums[i])
            return money[length-1]