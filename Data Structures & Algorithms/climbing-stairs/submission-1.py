class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1         # fibonacci

        for i in range(n - 1):
            temp = one          # temp to keep the original one
            one = one + two     # update one
            two = temp          # update two with temp (original one)

        return one