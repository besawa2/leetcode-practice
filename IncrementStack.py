class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.incrementArray = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        else:
            print("stack is full")

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        print("Popping", self.incrementArray[len(self.stack)-1] + self.stack[-1])
        answer = self.incrementArray[len(self.stack)-1] + self.stack.pop()

        self.increment(len(self.stack),self.incrementArray[len(self.stack)])
        self.incrementArray[len(self.stack)] = 0
        return answer

    def print(self):
        print(self.stack)
        print(self.incrementArray)

    def increment(self, k: int, val: int) -> None:
        k = min(k,len(self.stack))-1
        if k < 0:
            return
        self.incrementArray[k] += val 

        
# ["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
# [[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
cs = CustomStack(3)
cs.push(1)
cs.push(2)
cs.pop()
cs.push(2)
cs.push(3)
cs.push(4)
cs.increment(5, 100)
cs.increment(2, 100)
cs.pop()
cs.pop()
cs.pop()
cs.pop()

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)