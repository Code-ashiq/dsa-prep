class Solution:
    def pattern_8(self, n):
        # No of rows
        for i in range(n, 0, -1):
            # Printing spaces
            for j in range(n-i):
                print(" ", end="")
            for k in range(2 * i-1):
                print("*", end="")
            print()

sol = Solution()
sol.pattern_8(5)