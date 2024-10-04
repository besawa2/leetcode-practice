from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        stack = []
        pair = sorted([[p,s] for p, s in zip(position, speed)])
        for i in range(len(pair)):
            turnsToEnd = (target- pair[i][0]) / pair[i][1]
            #if stack and stack[-1] > turnsToEnd:
            while stack and stack[-1] <= turnsToEnd:
                stack.pop()
            stack.append(turnsToEnd)
        return len(stack)
    
    
sol = Solution()
print(sol.carFleet(target=10,
position=[1,4],
speed=[3,2]
))
        