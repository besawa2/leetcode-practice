class Solution:
    def generateParenthesis(self, n: int):
        stack = ["("]
        res = []
        #if num of close = n we append to res
        #if num of open < n we add open
        #if num of close < open we add close
        while stack:
            pop = stack.pop()
            if pop.count(")") == n:
                res.append(pop)
            if pop.count("(") < n:
                stack.append(pop+"(")
            if pop.count("(") > pop.count(")"):
                stack.append(pop+")")
        return res
    
sol = Solution()
print(sol.generateParenthesis(n=3))