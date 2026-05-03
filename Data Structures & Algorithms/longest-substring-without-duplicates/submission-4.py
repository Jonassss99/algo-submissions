class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxlength = 0
        charSet = set() # make use of its nature of non-repeating elements

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            maxlength = max(maxlength, len(charSet))

        return maxlength

        
        