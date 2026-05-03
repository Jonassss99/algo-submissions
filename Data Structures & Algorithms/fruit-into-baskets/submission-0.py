class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)    # fruittype -> count
        l = 0
        total = 0
        result = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1
            total += 1

            while len(count) > 2:
                count[fruits[l]] -= 1
                total -= 1
                
                if not count[fruits[l]]:
                    count.pop(fruits[l])
                
                l += 1

            result = max(result, total)

        return result

        # count = defaultdict(int)
        # l, total, res = 0, 0, 0

        # for r in range(len(fruits)):
        #     count[fruits[r]] += 1
        #     total += 1

        #     while len(count) > 2:
        #         f = fruits[l]
        #         count[f] -= 1
        #         total -= 1
        #         l += 1
        #         if not count[f]:
        #             count.pop(f)

        #     res = max(res, total)

        # return res       
                

