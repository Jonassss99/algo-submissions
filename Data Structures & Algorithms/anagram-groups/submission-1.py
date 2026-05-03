class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26 # from a to z

            for c in s:
                count[ord(c) - ord("a")] += 1 # using ASCII value

            res[tuple(count)].append(s)

        return list(res.values())