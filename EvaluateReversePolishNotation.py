from math import ceil
class Solution:
    def evalRPN(self, tokens) -> int:
        opList = set(["+","-","/","*"])
        stacky = []
        for token in tokens:
            if token not in list(opList):
                stacky.append(token)
            else:
                op2 = int(stacky.pop())
                op1 = int(stacky.pop())
                if token == "+":
                    stacky.append(op1+op2)
                elif token == "-":
                    stacky.append(op1-op2)
                elif token == "*":
                    stacky.append(op1*op2)
                elif token == "/":
                    if op1 * op2 < 0:
                        stacky.append(ceil(op1/op2))
                    else:
                        stacky.append(op1//op2)
        return int(stacky.pop())



sol = Solution()
print(sol.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))   