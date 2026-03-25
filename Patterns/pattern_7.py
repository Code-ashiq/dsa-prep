# Given an integer n. You need to recreate the pattern given below for any value of N.
# Let's say for N = 5, the pattern should look like as below:
#
#     *
#    ***
#   *****
#  *******
# *********

class Solution:
    def pattern_7(self, n):
        for i in range(1, n+1):
            #print spaces
            for j in range(n-i):
                print(" ", end="")
            for k in range(2 * i -1):
                print("*", end="")
            print()

sol = Solution()
sol.pattern_7(5)
