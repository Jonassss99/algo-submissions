class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Initialize S -> T and T -> S pairs
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            charS = s[i]    # Current character in s
            charT = t[i]    # Current character in T

            if (charS in mapST and mapST[charS] != charT) or (charT in mapTS and mapTS[charT] != charS):
                return False

            mapST[charS] = charT
            mapTS[charT] = charS

        return True

