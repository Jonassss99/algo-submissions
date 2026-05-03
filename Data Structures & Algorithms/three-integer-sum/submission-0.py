class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort the array first

        for i, a in enumerate(nums):
            if a > 0:   # res > 0 if a > 0 (a is the leftmost num in nums)
                break

            if i > 0 and a == nums[i - 1]:  # skip duplicate values
                continue

            l = i + 1   # a = num[i]
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:    # sum too big, move r to the left
                    r -= 1
                elif threeSum < 0:  # sum too small, move l to the right
                    l += 1
                else:   # sum = 0, carry on with l to right, r to left
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]: # skip duplicate at l
                        l += 1

        return res

        