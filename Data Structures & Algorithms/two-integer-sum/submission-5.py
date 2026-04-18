class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        for i in range(len(nums)):
            complimentaryNum = target - nums[i]
            if complimentaryNum in indexDict:
                return [indexDict[complimentaryNum], i]
            
            if nums[i] not in indexDict:
                indexDict[nums[i]] = i
        return []