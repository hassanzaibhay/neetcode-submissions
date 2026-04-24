class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            t = target - val
            start = idx + 1
            end = len(nums) - 1
            while start <= end:
                if nums[start] == t:
                    return [idx, start]
                elif nums[end] == t:
                    return [idx, end]
                start += 1
                end -= 1