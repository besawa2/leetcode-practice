#left decision - if valid, we'll add s[i] 
## to check if its valid palindrome, with two pointer solution
## if it is, we'll append a copy of our partial to res
# clean up partial by popping if we just appended 
#right decision - dont add s[i], call recursive on the next step s[i+1]

class Solution:
    def partition(self, s: str):
        res = []
        partial = []

        def isValid(possiblePalindrome):
            if len(possiblePalindrome) == 0:
                return False
            l, r = 0, len(possiblePalindrome) - 1
            isPalindrome = False
            while l < r:
                if possiblePalindrome[l] != possiblePalindrome[r]:
                    return isPalindrome
                l += 1
                r -= 1
            isPalindrome = True
            return isPalindrome

        def backtrack(i, currentBuild, partial): # i - index
            ## partition -- all previously built strings
            ## currentBuild -- string that we're building
            ## make sure we dont go out of bounds
            if i > len(s) -1 :
                if currentBuild != "":
                    return
                for part in partial:
                    if not isValid(part):
                        return
                res.append(partial)
                return
            
            currentBuild += s[i]

            #LEFT - add currentBuild into PARTIAL array
            partial.append(currentBuild)
            backtrack(i+1, "", partial[:]) #  currentBuild needs to be reset because current build is already in partial, and in left side we dont want to build up currentbuild

            partial.pop()
            #RIGHT -- continue building string
            backtrack(i+1, currentBuild, partial)
        

        
            
            
        backtrack(0,"", partial)
        return res

s = Solution()
input = "aab"
print(s.partition(input))