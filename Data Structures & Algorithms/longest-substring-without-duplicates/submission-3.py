class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxlength = 0

        for r in range(len(s)):
            while s[r] in charSet: # when spotting a repetition
                charSet.remove(s[l]) # remove curr left from the set
                l += 1  # move left pointer to the right by 1

            charSet.add(s[r]) # no more repetitions now, add curr right to the set
            
            maxlength = max(maxlength, len(charSet))

        return maxlength        
        