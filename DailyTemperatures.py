class Solution:
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temp,i))
        return res

sol = Solution()
print(sol.dailyTemperatures(temperatures = [30,38,30,36,35,40,28]))
