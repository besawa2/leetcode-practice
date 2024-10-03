class Solution:
    def generateParenthesis(self, n: int):
        res = []
        #if num of close = n we append to res
        #if num of open < n we add open
        #if num of close < open we add close
        def helper(pop,openCount,closedCount):
            if closedCount == n:
                    res.append(pop)
            if openCount < n:
                    helper(pop + "(", openCount+1, closedCount)
            if openCount > closedCount:
                    helper(pop + ")",openCount,closedCount+1)
        helper("",0,0)
        return res
sol = Solution()
print(sol.generateParenthesis(n=3))