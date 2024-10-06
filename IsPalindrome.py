
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lAlNumHelper = 0
        rAlNumHelper = len(s)-1
        for i in range(len(s)):
            L = s[lAlNumHelper + i]
            R = s[rAlNumHelper-i]
            if lAlNumHelper+i >= rAlNumHelper-i:
                    return True
            while not L.isalnum():
                lAlNumHelper+=1
                if lAlNumHelper + i <len(s):
                    L = s[lAlNumHelper + i]

            if lAlNumHelper+i >= rAlNumHelper-i:
                    return True
            while not R.isalnum():
                rAlNumHelper -=1
                if rAlNumHelper -i > len(s):
                    R = s[rAlNumHelper-i]

            if lAlNumHelper+i >= rAlNumHelper-i:
                    return True
            if L.isalnum() and R.isalnum():
                print("can do work")
                if str.upper(L) != str.upper(R):
                    return False
                

        return False
    
sol = Solution()
print(sol.isPalindrome(s="Was it a car or a cat I saw?"
))
