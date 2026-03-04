class Solution:
    def pattern_6(self,n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end="")
            print()

sol = Solution()
sol.pattern_6(5)