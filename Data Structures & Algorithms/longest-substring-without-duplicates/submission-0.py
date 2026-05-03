class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = r = maxlength = 0

        for c in s:
            if c in charSet:
                while c in charSet:
                    charSet.remove(s[l])
                    l += 1
            charSet.add(c)
            r += 1
            maxlength = max(maxlength, r - l)

        return maxlength        
        