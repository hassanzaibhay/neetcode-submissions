class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums):
            t = target - val
            if t in seen:
                return [seen[t], idx]
            seen[val] = idx