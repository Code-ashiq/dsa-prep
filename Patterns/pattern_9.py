class Solution:
    def pattern_9(self,n):
        for i in range(1, n+1):
            for j in range(n-i):
                print(" ", end="")
            for k in range(2 * i -1):
                print("*", end="")
            print()

        for i in range(n, 0, -1):
            for j in range(n-i):
                print(" ", end="")
            for k in range(2 * i -1):
                print("*", end="")
            print()
    #ALTERNATE SOLUTION
    def pattern_9_alt(self,num):

        # Upper pyramid
        for i in range(1, num + 1):
            spaces = num - i
            stars = 2 * i - 1

            print(" " * spaces + "*" * stars)

        # Lower inverted pyramid
        for i in range(num, 0, -1):
            spaces = num - i
            stars = 2 * i - 1

            print(" " * spaces + "*" * stars)

sol = Solution()

sol.pattern_9_alt(5)
