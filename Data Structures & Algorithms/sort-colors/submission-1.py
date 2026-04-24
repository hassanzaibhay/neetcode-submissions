class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = nums.count(0), nums.count(1), nums.count(2)
        nums[:zeros] = [0] * zeros
        nums[zeros:zeros+ones] = [1] * ones
        nums[zeros+ones:] = [2] * twos