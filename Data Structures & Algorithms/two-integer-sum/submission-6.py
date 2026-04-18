class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {}
        for i, n in enumerate(nums):
            complimentaryNum = target - n
            if complimentaryNum in indexDict:
                return [indexDict[complimentaryNum], i]
            indexDict[n] = i
        return