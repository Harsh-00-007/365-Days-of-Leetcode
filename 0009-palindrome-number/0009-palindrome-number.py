class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = 0
        if x == 0:
            return True
        while x>0:
            last = x % 10
            reverse = (reverse*10) + last
            x = x//10
        return reverse==num