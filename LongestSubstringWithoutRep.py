
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,1
        seenValues = {}
        count = 1
        maxCount = 1
        if len(s) < r:
            return 0
        seenValues[s[l]] = 1
        while r < len(s):
            if s[r] not in seenValues:
                seenValues[s[r]] = 1
                count += 1
                if count > maxCount:
                    maxCount = count
            else:
                l = r
                seenValues = {}
                seenValues[s[l]] = 1
                count = 1
            r += 1

        return maxCount



x = Solution()
s="dvdf"
print(x.lengthOfLongestSubstring(s))