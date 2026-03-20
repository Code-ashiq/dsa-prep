class Solution:
    def pattern_12(self, n):
        #rows
        for i in range(1, n+1):

            # Left side
            for j in range(1, i+1):
                print(j, end="")

            # Spaces
            for j in range(2 * (n -i)):
                print(" ", end="")

            # Right side
            for j in range(i, 0, -1):
                print(j, end="")

            print() # Move to next line

sol = Solution()
sol.pattern_12(9)