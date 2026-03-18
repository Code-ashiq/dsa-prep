class Solution:
    def pattern_11(self, n):
        for i in range(1, n+1):
            val = i % 2

            for j in range(i):
                print(val, end=" ")
                val = 1 - val
            print()

sol = Solution()
sol.pattern_11(5)