class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        preSum = 0
        preMap = {0 : 1} # initialize 0 to be seen once 

        for num in nums:
            preSum += num
            target = preSum - k

            if target in preMap:
                count += preMap[target]

            preMap[preSum] = preMap.get(preSum, 0) + 1

        return count