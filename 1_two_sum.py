class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mp = {}

        for i, num in enumerate(nums):
            rem = target - num
            if rem in mp:
                return [mp[rem], i]
            mp[num] = i
