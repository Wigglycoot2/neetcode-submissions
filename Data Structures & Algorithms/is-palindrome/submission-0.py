class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(filter(str.isalnum, s))

        left = 0
        right = len(clean)-1

        while left < right:
            if clean[left].lower() != clean[right].lower():
                return False
            left+=1
            right-=1

        return True