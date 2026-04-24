class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        from collections import Counter
        counter = Counter(nums)
        for _ in range(counter[val]):
            nums.remove(val)
        return len(nums)