class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""    # Initialize result

        for i in range(len(strs[0])):   # Iterate through every char in 1st string
            for s in strs:              # Iterate through every string in list of strings
                if i == len(s) or s[i] != strs[0][i]:  # Check s out of bound, then compare each string's index i with 1st string's index i
                    return res
                
            res += strs[0][i]           # Update result
        return res