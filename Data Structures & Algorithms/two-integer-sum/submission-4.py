class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complimentaryNum = target - nums[i]
            remainingListStartIdx = i + 1
            remainingList = nums[remainingListStartIdx:]
            if complimentaryNum in remainingList:
                return [i, remainingListStartIdx + remainingList.index(complimentaryNum)]
        return []