class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complimentaryNum = target - nums[i]
            remainingList = nums[i + 1:]
            if complimentaryNum in remainingList:
                return [i, i + 1 + remainingList.index(complimentaryNum)]
        return []