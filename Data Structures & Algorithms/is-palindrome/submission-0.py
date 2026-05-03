class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two-pointer

        # Initialize the left and right pointer
        l = 0
        r = len(s) - 1

        # While loop to move the pointers
        while l < r:

            while l < r and not self.alphaNum(s[l]):    # Skip if s[l] is not alphanumeric
                l += 1
            while r > l and not self.alphaNum(s[r]):    # Skip if s[r] is not alphanumeric
                r -= 1

            if s[l].lower() != s[r].lower():    # False when s[l] and s[r] no match
                return False

            l += 1  
            r -= 1
        
        return True

    # Check if a character is alphanumeric using ASCII values
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))

