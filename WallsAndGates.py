class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addRoom(r,c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited or grid[r][c] == -1):
                return #invalid room
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c]) #add treasure to queue
                    visited.add((r,c)) #add treasure to visited
        
        dist = 0 #starting distance
        while q:
            for i in range(len(q)): #each layer / step of the q
                r, c = q.popleft()
                grid[r][c] = dist

                addRoom(r + 1, c)
                addRoom(r, c + 1)
                addRoom(r - 1, c)
                addRoom(r, c - 1)

            dist += 1

