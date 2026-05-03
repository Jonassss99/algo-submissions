class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}    # Create num : index

        # Track index and num in nums
        for i, n in enumerate(nums):
            diff = target - n   # Get diff between current num and target

            if diff in prevMap:     # If diff appears in past nums
                return [prevMap[diff], i] 

            prevMap[n] = i  # Store current num and index in past nums