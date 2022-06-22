class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_x = list(reversed(list(str(x))))
        if reversed_x == list(str(x)):
            return True