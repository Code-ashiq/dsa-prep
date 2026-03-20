# Given an integer n. You need to recreate the pattern given below for any value of N.
# Let's say for N = 5, the pattern should look like as below:

# *
# **
# ***
# ****
# *****

class Solution:
    def pattern_2(self, n):
        for i in range(n+1):
            print("*" * i)

sol = Solution()
sol.pattern_2(5)