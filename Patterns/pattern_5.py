class Solution:
    def pattern_5(self,n):
        for i in range(n, 0, -1):
            print("*" * i)

sol = Solution()
sol.pattern_5(5)