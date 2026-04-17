class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        uniqueList = list(numsSet)
        return len(nums) != len(uniqueList)
        