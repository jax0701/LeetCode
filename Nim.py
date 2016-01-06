class Solution:
    def canWinNim(self,n):
        return bool(n%4)

test = Solution()
print test.canWinNim(9)
