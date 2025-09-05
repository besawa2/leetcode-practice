class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1Count = {}
        for i in range(len(s1)):
            s1Count[s1[i]] = s1Count.get(s1[i], 0) + 1
        s2Count = {}
        l = 0
        s2Count[s2[l]] = 1
        for r in range(1,len(s2)):
            if s1Count == s2Count:
                return True
            s2Count[s2[r]] = s2Count.get(s2[r], 0) + 1   
            while (r - l) == len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1
        if s1Count == s2Count:
            return True
        return False


sol = Solution()
s1="adc"
s2="dcda"
print(sol.checkInclusion(s1,s2))