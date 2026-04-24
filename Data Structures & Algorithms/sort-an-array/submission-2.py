class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # counting sort
        min_n = min(nums)
        max_n = max(nums)
        
        offset = -min_n
        count = [0] * (max_n - min_n + 1)
        
        result = [0] *(len(nums))
        for num in nums:
            count[num + offset] += 1
        for i in range(1 ,len(count)):
            count[i] += count[i-1]
        for num in reversed(nums):
            count[num + offset] -= 1
            result[count[num + offset]] = num
        return result